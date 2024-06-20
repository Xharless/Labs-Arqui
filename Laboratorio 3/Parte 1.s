.data 
	valores: .word 3, 5, 1, 5, 2 	@lista
	n: .word 5 	@cantidad de datos
	resultado: .word 1 	@resultado
.text
.global main

main:
	mov r0, #0
	mov r1, #0

	@almacenar valores
	ldr r3, =valores
	ldr r4, =resultado

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
