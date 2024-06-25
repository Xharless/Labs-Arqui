.data 
values: .word 3,5,1,5,2
n: .word 5
.section .bss
result: .word 0
.section .text
.global main

main:
	mov r0, #0
	ldr r1, =result

	ldr r2, =values
	ldr r3, =n
	ldr r3, [r3]

	mov r4, #0

	b loop 
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
	mov r0, #1 
  	mov r7, #1 
 	svc 0 
wfi
