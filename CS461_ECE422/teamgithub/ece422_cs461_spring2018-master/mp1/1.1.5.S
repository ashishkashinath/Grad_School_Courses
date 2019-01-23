.global _main
.section .text

_main:

push    %ebp
mov     %esp,%ebp


/*eax contains the syscall number */
mov $0xb, %eax
/*ebx contains a pointer to filename*/
movl $0xbffffba0, %ebx          /* Some random address */
movl $0x6e69622f, (%ebx)        /* "/bin" */
movl $0x68732f, 4(%ebx)         /* "/sh\x00" */

/*ecx contains array of strings passed to the new program */
/*edx contains is an array of strings of the form key=value passed to the program */
/* We are interested in only calling /bin/sh , so for us %ebx and %ecx have nothing, just need to
terminate them with NULL */

movl $0xbffffab0, %ecx
movl $0xbffffab0, %edx
movl $0x00000000, (%ecx)
movl $0x00000000, (%edx)

int $0x80

leave
ret
