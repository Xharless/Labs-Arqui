.data
	n: .word 3                @num de discos
	buffer: .space 12
	.resultado: .word 0       @variable para almacenar resultado

.text
.global main

main:
    ldr r0, =n             @cargar direccion de n
    ldr r0, [r0]           @cargar el valor de n en r0
    mov r3, r0
    sub r3, r3, #1
    bl recursivo           @llamar a la recursion
        
recursivo:
    cmp r0, #1             @comparar si n = 1
    beq caso_base          
    
    sub r0, r0, #1         @calcular recursivamente T(n-1)
    bl recursivo
    cmp r3, #0
    beq final
    sub r3, r3, #1
    mov r1, r0             @guardar T(n-1) en r1
    mov r2, #2             
    mul r1, r1, r2         @T(n-1) * 2
    add r0, r1, #1         @T(n) = T(n-1) * 2 + 1
    
    bx lr                  

caso_base:
    mov r0, #1             @caso base: T(1) = 1
    bx lr
                  
final:
    mov r3, r0
    mov r0, #0
    mov r1, #0
    mov r2, r3 @resultado a imprimir
    bl printInt
    wfi
