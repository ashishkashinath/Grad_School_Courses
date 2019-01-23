import sys
import urllib2
from Crypto.Cipher import AES

# helper function for checking whether or not the padding is correct
# 500 indicates a padding error while 404 indicates a correct padding but wrong ciphertext
def get_status(u):
    req = urllib2.Request(u)
    try:
        f = urllib2.urlopen(req)
        return f.code
    except urllib2.HTTPError, e:
		return e.code

# Remove the padding, returning an error if bad padding 
def strip_padding(msg):
    padlen = 17 - ord(msg[-1])
    if padlen > 16 or padlen < 1:
        return True, None
    if msg[-padlen:] != ''.join(chr(i) for i in range(16,16-padlen,-1)):
        return True, None
    return False, msg[:-padlen]

# padding oracle attack	
def padding_oracle(ciphertext_file, output_file):

	# grab the ciphertext
	ciphertext = None 

	with open(ciphertext_file, 'r') as file: 
		ciphertext = file.read().strip()

	# pre-processing variables
	request = 'http://192.17.90.133:9990/mp1/fisiaka2/?'
	step = AES.block_size * 2
	blocks = [ciphertext[i:i + step] for i in range(0, len(ciphertext), step)]
	guess_text = ''

	# build the plaintext using the algorithm described by https://www.youtube.com/watch?v=evrgQkULQ5U&feature=youtu.be&t=345 
	# start by decrypting ciphertext_block [1] all the way to ciphertext_block[n]
	
	# iterate over each block 
	plaintext = ''
	for block in range(1, len(blocks)):
		blockA = blocks[block - 1]
		blockB = blocks[block]
		guessed_array = [None] * 16

		# loop for a block pair to use for guessing
		for byte in range(16, 0, -1):
			guess_block = blockA

			# modify the guess block based on previous guesses
			for pad in range(byte, 16):
				byteindex = ((-2 * (pad - byte)) - 2) + len(blockA)
				guess_block = guess_block[:byteindex] + hex(guessed_array[byteindex/2] ^ int(blockA[byteindex:byteindex + 2], 16) ^ pad)[2:].zfill(2) + guess_block[byteindex + 2:]
				
			byteindex = ((-2 * (16 - byte)) - 2) + len(blockA)

			# guess till we find a correct padding and record the guess
			for guess in range(256):
				guess_block = guess_block[:byteindex] + hex(guess ^ int(blockA[byteindex:byteindex + 2], 16) ^ 16)[2:].zfill(2) + guess_block[byteindex + 2:]
				status = get_status(request + guess_block + blockB)

				if(status == 404):
					guessed_array[byte - 1] = guess
					break

		# add the intermediate message			
		for byte in guessed_array:
			plaintext += hex(byte)[2:].zfill(2)

	with open(output_file, 'w') as file: 
		file.write(plaintext.decode('hex'))

	return plaintext.decode('hex')

def main():
	if(len(sys.argv) != 3):
		print 'Invalid arguments'

	# parse args
	ciphertext_file = sys.argv[1]
	output_file = sys.argv[2]

	print 'PLAINTEXT: ' + padding_oracle(ciphertext_file, output_file) 

if(__name__ == '__main__'):
	main()