import sys 

# decrypts a message from a specified ciphertext, key and modulo file(s) and writes it into a specified output file
def decrypt_RSA(ciphertext_file, key_file, modulo_file, output_file):

	# grab the ciphertext from the file
	ciphertext = None
	with open(ciphertext_file, 'r') as file: 
		ciphertext = file.read().strip()
	ciphertext = int(ciphertext, 16)

	# grab the key from the file
	key = None
	with open(key_file, 'r') as file:
		key = file.read().strip()
	key = int(key, 16)
	
	# grab the modulo from the file
	modulo = None 
	with open(modulo_file, 'r') as file: 
		modulo = file.read().strip()
	modulo = int(modulo, 16)

	# get the message back by decrypting RSA style
	msg = pow(ciphertext, key, modulo)

	# write the msg in hex to the file specified
	with open(output_file, 'w') as file: 
		file.write(hex(msg)[2:len(hex(msg))- 1])

	print 'RSA Decrypted!'

def main():
	if(len(sys.argv) != 5):
		print 'Invalid arguments'
		return -1

	# parse the args
	ciphertext_file = sys.argv[1]
	key_file = sys.argv[2]
	modulo_file = sys.argv[3]
	output_file = sys.argv[4]

	decrypt_RSA(ciphertext_file, key_file, modulo_file, output_file)

if(__name__ == '__main__'):
	main()