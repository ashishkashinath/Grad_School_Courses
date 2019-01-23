	.global your_asm_fn
	.section .text

	your_asm_fn:

	push    %ebp
	mov     %esp,%ebp

	/*Make space for 3 integers = 12 bytes */
	subl    $12,%esp

	/*Push values "coolfood", 0xc105ed, 0xacce55ed onto the stack
	Learning:
	SP points to the next empty slot
	c = 0x63
	o = 0x6f
	o = 0x6f
	l = 0x6c
	f = 0x66
	o = 0x6f
	o = 0x6f
	d = 0x64
	\0 = 0x00
	*/


	#First Push the string
	movl $str, -4(%ebp)

	#Copy the value to a very far away memory location
	#Keep that address on the stack
	movl $0xc105ed, 100(%esp)
	lea 100(%esp), %eax
	movl %eax, -8(%ebp)

	#Finally push the value
	movl $0xacce55ed, -12(%ebp)


	call practice
	leave
	ret

	str:
	        .string "coolfood"
