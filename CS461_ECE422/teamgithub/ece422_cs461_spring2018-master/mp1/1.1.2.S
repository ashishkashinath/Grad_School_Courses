	.global your_asm_fn
	.section .text

	your_asm_fn:

	push    %ebp
	mov     %esp,%ebp

	/*Make space for 3 integers = 12 bytes */
	subl    $12,%esp

	/*Push values 0xc001f00d, 0xc105ed, 0xacce55ed onto the stack
	Learning:
	SP points to the next empty slot*/

	movl $0xc001f00d, 8(%esp)
	movl $0xc105ed, 4(%esp)
	movl $0xacce55ed, (%esp)

	call practice

	leave
	ret
