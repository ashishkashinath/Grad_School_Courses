import sys
import dpkt
import socket

def tcp_flags(flags):
	ret = ''
	if flags & dpkt.tcp.TH_SYN:
		ret = ret + 'S'
	if flags & dpkt.tcp.TH_ACK:
		ret = ret + 'A'
	return ret

filename = sys.argv[1]
seen = []
	
f = open(filename)
pcap = dpkt.pcap.Reader(f)
	
for ts, buf in pcap:
	eth = dpkt.ethernet.Ethernet(buf)
	ip = eth.data
	if type(ip) != dpkt.ip.IP:
		continue
	tcp = ip.data
	if type(tcp) != dpkt.tcp.TCP:
		continue
	if tcp.dport == 80 and len(tcp.data) > 0:
			try:
				ipAdd = ip.src
				sum = 0
		
				if(ipAdd not in seen):
					seen.append(ipAdd)
					for ts, buf in pcap:
						eth = dpkt.ethernet.Ethernet(buf)
						ip = eth.data
						if type(ip) != dpkt.ip.IP:
							continue
						tcp = ip.data
						if type(tcp) != dpkt.tcp.TCP:
							continue
						if tcp.dport == 80 and len(tcp.data) > 0:
							try:
								if(ipAdd == ip.src and tcp_flags(tcp.flags) == 'S'):
									sum = sum + 1
								if(ipAdd == ip.dst and tcp_flags(tcp.flags) == 'S' + 'A'):
									sum = sum - 3
							except dpkt.dpkt.NeedData:
								continue
							except dpkt.dpkt.UnpackError:
								continue
		
					if(sum > 0):
						print socket.inet_ntoa(ipAdd)
			except dpkt.dpkt.NeedData:
				continue
			except dpkt.dpkt.UnpackError:
				continu
f.close()

if __name__ == "__main__":
	main()
