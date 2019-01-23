import sys

# finds a wha collision for the given string 
def wha_collision(msg):
    # hash value of msg
    # assuming there are 2 or more characters in msg that are both upper case or lower case
    # assuming string is not the same everywhere
    wha_hash = str(wha(msg))
    case_idx = [idx for idx in range(len(msg)) if msg[idx].isupper()]
    if len(case_idx) >= 2:
        first_idx = case_idx[0]
        for idx in case_idx[1:]:
            if msg[first_idx] != msg[idx]:
                result = list(msg)
                temp = result[idx]
                result[idx] = msg[first_idx]
                result[first_idx] = temp
                return ''.join(result)

    # try lowercase
    case_idx = [idx for idx in range(len(msg)) if msg[idx].islower()]
    if len(case_idx) >= 2:
        first_idx = case_idx[0]
        for idx in case_idx[1:]:
            if msg[first_idx] != msg[idx]:
                result = list(msg)
                temp = result[idx]
                result[idx] = msg[first_idx]
                result[first_idx] = temp
                return ''.join(result)

    # return reverse if neither of them work
    # need to fix this depending on autograder
    return msg[::-1]


# implements a weak hashing algorithm that takes an input file and computes a hash for it
def wha(msg):

    # take the message we wish to hash
    mask = 0x3FFFFFFF
    outhash = 0

    # apply the weak hashing algorithm
    for char in msg:
        byte = ord(char)
        val = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
        outhash = (outhash & mask) + (val & mask)

    return hex(outhash)

def test():
    assert wha("Hello world!") == hex(0x50b027cf)
    assert wha("I am Groot.") == hex(0x57293cbb)
    assert wha("I am Groot.") == wha("I ma Groot.")
    assert wha("I am Groot.") == wha("I ao Gromt.")
    assert wha("G am fdaijgfwqoijgqeoirjgoiqjeroigjqeraoirgjqIroot.") == wha("I ao fdaijgfwqoijgqeoirjgoiqjeroigjqeraoirgjqGromt.")
    assert wha("Hello world!") == wha("Hello world!")
    assert wha("Hello world") == wha(wha_collision("Hello world"))
    assert wha("requh3rqgoijq j!@dsfjrq! sdjOIJF    EFGGQERGJdsafgwoIJEF AI$") == wha(wha_collision("requh3rqgoijq j!@dsfjrq! sdjOIJF    EFGGQERGJdsafgwoIJEF AI$"))

def main():
    if(len(sys.argv) != 3):
        print 'Invalid arguments'

    # parse the arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as file:
        msg = file.read().strip()

    with open(output_file, 'w') as file:
        file.write(wha(msg))

if(__name__ == '__main__'):
    main()
    # test()
