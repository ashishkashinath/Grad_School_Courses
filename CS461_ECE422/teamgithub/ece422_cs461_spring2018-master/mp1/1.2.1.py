# print "linhcao2\x00\x00A\x2B"
# a = raw_input()
# Need to fill up 5 more bytes in name to overflow grade
a = 'netid'
print a + "\x00" * (10 - len(a)) + "A+"
