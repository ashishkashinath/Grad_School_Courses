	.global your_asm_fn
	.section .text

	your_asm_fn:

	push    %ebp
	mov     %esp,%ebp

	/*Make space for 4 integers = 16 bytes */
	subl    $16,%esp

	/*Push values 0xc001f00d, 0xc105ed, 0xacce55ed onto the stack
	Learning:
	SP points to the next empty slot
	$esp + 8 points to $esp + 12

	*/
	movl $0xc001f00d, 12(%esp)
	lea 12(%esp), %edi
	movl %edi, 8(%esp)
	movl $0xc105ed, 4(%esp)
	movl $0xacce55ed, (%esp)

	call practice

	leave
	ret
