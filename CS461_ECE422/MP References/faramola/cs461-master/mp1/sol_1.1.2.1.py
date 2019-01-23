import sys

# deciphers ciphertext in a given file based on a given key in another file and puts the plaintext into a specified output file
def decipher(ciphertext_file, key_file, output_file): 

	keydict = {}
	char = 'A'

	with open(key_file,'r') as file: 
		subkey = file.read().strip()

		# use a dict to help us figure out the meaning of a letter
		for i in range(len(subkey)):
			keydict[subkey[i]] = char
			char = chr(ord(char) + 1)

	plaintext = ''

	# open the ciphertext file and decipher it using the keydict
	with open(ciphertext_file,'r') as file: 
		ciphertext = file.read().strip()
		for char in ciphertext:
			if(char in keydict):
				plaintext += keydict[char]
			else:
				plaintext += char

	# write the plaintext into the output file specificed 
	with open(output_file,'w') as file:
		file.write(plaintext) 

	print 'Deciphered!'

def main():

	if(len(sys.argv) != 4):
		print 'Invalid arguments'
		return -1 

	# parse the args
	ciphertext_file = sys.argv[1]
	key_file =	sys.argv[2]
	output_file = sys.argv[3]

	decipher(ciphertext_file, key_file, output_file)

if(__name__ == '__main__'):
	main()