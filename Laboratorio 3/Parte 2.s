	.data
Entrada: .word 2 @valor de la entrada a ingresar
resultado: .word 1 @valor inicial del resultado para recursividad

.text
.global main

main:
	@inicializar
	ldr r0, =Entrada
	ldr r1, =resultado
	ldr r2, [r0] @valor de la entrada
	ldr r3, [r1] @valor del resultado
	
	mov r4, #2 @numero a elevar
	b elevar

elevar:
	cmp r2,#0 @si contador es 0, finalizar
	beq printear

	mul r3, r3, r4 @multiplica x2

	sub r2, r2, #1
	b elevar

printear:
	sub r3, r3, #1
	
	@valores para el print
	mov r0, #0
	mov r1, #0
	mov r2, r3 @resultado a imprimir
	bl printInt

wfi
