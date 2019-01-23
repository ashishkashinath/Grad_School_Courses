import sys
from Crypto.Cipher import AES

# decipher a given ciphertext based on specified AES key and IV. Then writes the plaintext to a specified file
def decipher_AES(ciphertext_file, key_file, iv_file, output_file): 
	
	# grab the key from the given file
	key = None
	with open(key_file, 'r') as file: 
		key = file.read().strip()

	# grab the IV from the given file
	IV = None
	with open(iv_file, 'r') as file:
		IV = file.read().strip()

	# grab the ciphertext from the given file
	ciphertext = None
	with open(ciphertext_file, 'r') as file:
		ciphertext = file.read().strip()

	# create the AES cipher object and then decrypt the ciphertext with it
	cipher = AES.new(key.decode('hex'), AES.MODE_CBC, IV.decode('hex'))
	plaintext = cipher.decrypt(ciphertext.decode('hex'))

	# write the plaintext to the specified output file
	with open(output_file, 'w') as file: 
		file.write(plaintext)

	print 'Decrypted!'
	
def main():

	if(len(sys.argv) != 5):
		print 'Invalid arguments'
		return -1 

	# parse the args
	ciphertext_file = sys.argv[1]
	key_file =	sys.argv[2]
	iv_file = sys.argv[3]
	output_file = sys.argv[4]

	decipher_AES(ciphertext_file, key_file, iv_file, output_file)

if(__name__ == '__main__'):
	main()