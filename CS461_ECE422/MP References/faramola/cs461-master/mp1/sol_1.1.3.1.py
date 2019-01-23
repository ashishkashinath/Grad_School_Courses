import sys 
from Crypto.Hash import SHA256 

def hamming(string_file1, string_file2, output_file):

	# grab the first text to hash
	string1 = None
	with open(string_file1, 'r') as file:
		string1 = file.read().strip()

	# grab the second text to hash
	string2 = None
	with open(string_file2, 'r') as file:
		string2 = file.read().strip()

	# hash them, get the hex and make it an integer
	hex1 = int(SHA256.new(string1).hexdigest(), 16)
	hex2 = int(SHA256.new(string2).hexdigest(), 16)
	
	# compute the hamming distance by XORing them and then counting the 1s in the result
	hamming = hex(bin(hex1 ^ hex2)[2:].count('1'))[2:]

	# write the hex value of the hamming distance.
	with open(output_file, 'w') as file:
		file.write(hamming)

	print 'Hamming Distance Computed!'

def main():
	if(len(sys.argv) != 4):
		print 'Invalid arguments'

	# parse args
	string_file1 = sys.argv[1]
	string_file2 = sys.argv[2]
	output_file = sys.argv[3]

	hamming(string_file1, string_file2, output_file)

if(__name__ == '__main__'):
	main()