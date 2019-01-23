#!/usr/bin/python2.7
import dpkt
import sys
from collections import defaultdict
import socket

def main():
    if (len(sys.argv) < 2):
        print "error: need argument"
        sys.exit(1)

    filename = sys.argv[1]
    list_ip = analyze_packet(filename)
    for ip in list_ip:
        print ip
    sys.exit(0)

def analyze_packet(filename):
    res = []
    syn_count = defaultdict(int)
    syn_ack_count = defaultdict(int)
    with open(filename, 'r') as fp:
        pcap_reader = dpkt.pcap.Reader(fp)
        for ts, buf in pcap_reader:
            try:
                eth_obj = dpkt.ethernet.Ethernet(buf)
                ip_obj = eth_obj.data
                if isinstance(ip_obj, dpkt.ip.IP):
                    tcp_obj = ip_obj.data
                    if isinstance(tcp_obj, dpkt.tcp.TCP):
                        src_addr = socket.inet_ntoa(ip_obj.src)
                        dst_addr = socket.inet_ntoa(ip_obj.dst)
                        if tcp_obj.flags == 0x2: #SYN flag
                            syn_count[src_addr] += 1
                        elif tcp_obj.flags == 0x12: # SYN-ACK flag
                            syn_ack_count[dst_addr] += 1
            except:
                continue
    for ip_addr in syn_count:
        if ip_addr not in syn_ack_count or syn_count[ip_addr] > (3 * syn_ack_count[ip_addr]):
            res.append(ip_addr)
    return res

if __name__ == '__main__':
    main()
