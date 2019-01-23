import sys
from Crypto.Cipher import AES

# Magic numbers for keeping the library happy
AES_KEY_SIZE = 64
AES_IV_SIZE = 32

# Breaks a given ciphertext without an AES key and a given IV. Then writes the plaintext to a specified file
def break_weak_AES(ciphertext_file, output_file): 

	# grab the ciphertext from the given file
	ciphertext = None
	with open(ciphertext_file, 'r') as file:
		ciphertext = file.read().strip()

	# the key has 251 leading zeroes so we leverage this 
	plaintext = None 
	IV = hex(0)[2:].zfill(AES_IV_SIZE)
	AES_key = None 

	for key in range(32):
		hexkey = hex(key)[2:].zfill(AES_KEY_SIZE)
		cipher = AES.new(hexkey.decode('hex'), AES.MODE_CBC, IV.decode('hex'))

		decryption = cipher.decrypt(ciphertext.decode('hex'))
		encryption = cipher.encrypt(decryption)

		if(decryption[0] == 'T'):
			plaintext = decryption
			AES_key = hexkey

	# write the plaintext to the specified output file
	with open(output_file, 'w') as file: 
		file.write(AES_key)

	print ('Weak AES was cracked! Here is the key: ' + str(AES_key))
	
def main():

	if(len(sys.argv) != 3):
		print 'Invalid arguments'
		return -1 

	# parse the args
	ciphertext_file = sys.argv[1]
	output_file = sys.argv[2]

	break_weak_AES(ciphertext_file, output_file)

if(__name__ == '__main__'):
	main()