
# takes an integer and then outputs its hex value as a string 
def to_hex(integer): 
	return hex(integer)[2:]

# takes an integer and then outputs its binary value as a string 
def to_bin(integer):
	return bin(integer)[2:]

def main(): 
	integer = 0
	binary_string = 0

	# open the file with the hex value and process it
	with open('1.1.1.2_value.hex', 'r') as file:
		contents = file.read().strip()

		# convert the contents into an integer and binary
		integer = int(contents, 16)
		binary_string = to_bin(integer)

	# write the answers into their appropriate files
	with open('sol_1.1.1.2_decimal.txt', 'w') as file:
		file.write(str(integer))
	
	with open('sol_1.1.1.2_binary.txt', 'w') as file:
		file.write(binary_string)		

	print 'Conversion complete and written into the appropriate files!'
if(__name__ == '__main__'): 
	main()