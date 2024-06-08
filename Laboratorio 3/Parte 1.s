.data 
.section .bss
	.lcomm buffer, 4096
	.lcomm numbers, 4096
	.lcomm result, 4096
.text
.global main

main:
	mov r0, #0
	mov r1, #0
	ldr r3, = numbers
	ldr r4, =result
loop:
	ldrb r2, [r3, r0]
	cmp r2, #0
	beq termino
	strb r2, [r4, r1]
	add r1, r1, #1
	add r0, r0, #1
	add r0, r0, #2
	b loop


termino:
	mov r0, #1
	ldr r1, =result
	mov r2, r1
	mov r7, #4
	swi 0
	mov r7, #1
	mov r0, #0
	swi 0
wfi
