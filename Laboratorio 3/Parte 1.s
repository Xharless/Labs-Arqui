.data 
<<<<<<< HEAD
values: .word 3,5,1,5,2
n: .word 5
.section .bss
result: .word 0
.section .text
=======
	valores: .word 3, 5, 1, 5, 2 	@lista
	n: .word 5 	@cantidad de datos
	resultado: .word 1 	@resultado
.text
>>>>>>> ffaeb8fe36f6d934cd2fb9699683d7af169216b7
.global main

main:
	mov r0, #0
<<<<<<< HEAD
	ldr r1, =result

	ldr r2, =values
	ldr r3, =n
	ldr r3, [r3]

	mov r4, #0

	b loop 
=======
	mov r1, #0

	@almacenar valores
	ldr r3, =valores
	ldr r4, =resultado

>>>>>>> ffaeb8fe36f6d934cd2fb9699683d7af169216b7
loop:
	cmp r0, r3
	bge termino
	
	add r6, r2, r0
	ldr r5, [r6]
	str r5, [r1, r4]

	add r4, r4, #4 
	add r0, r0, #3

	b loop

termino:
<<<<<<< HEAD
	mov r0, #1 
  	mov r7, #1 
 	svc 0 
=======
	mov r0, #1
	ldr r1, =result
	mov r2, r1
	mov r7, #4

	swi 0

	mov r7, #1
	mov r0, #0

	swi 0

>>>>>>> ffaeb8fe36f6d934cd2fb9699683d7af169216b7
wfi
