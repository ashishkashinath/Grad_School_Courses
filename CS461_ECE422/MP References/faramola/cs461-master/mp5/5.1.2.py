import pickle

def make_pickle():
	partners = ['fisiaka2', 'tyamamo2']
	with open('5.1.2.1.pickle', 'w') as file:
		pickle.dump(partners, file) 

def unmake_pickle():
	with open('5.1.2.1.pickle', 'r') as file:
		contents = pickle.load(file) 
	return contents

def main():
	make_pickle()
	print unmake_pickle()

if (__name__ == '__main__'):
	main()