
.data
n: .word 3                @ Número de discos
buffer: .space 12
.resultado: .word 0       @ Variable para almacenar el resultado

.text
.global main

main:
    ldr r0, =n             @ Cargar dirección de n en r0
    ldr r0, [r0]           @ Cargar el valor de n en r0
    mov r3, r0
    sub r3, r3, #1
    bl recursivo           @ Llamar a la función recursiva
        
recursivo:
    cmp r0, #1             @ Comparar con caso base (n == 1)
    beq caso_base          @ Si n == 1, ir al caso base
    
    sub r0, r0, #1         @ Calcular recursivamente T(n-1)
    bl recursivo
    cmp r3, #0
    beq final
    sub r3, r3, #1
    mov r1, r0             @ Guardar T(n-1) en r1
    mov r2, #2             @ r2 = 2
    mul r1, r1, r2         @ T(n-1) * 2
    add r0, r1, #1         @ T(n) = T(n-1) * 2 + 1
    
    bx lr                  @ Retornar al llamador

caso_base:
    mov r0, #1             @ Caso base: T(1) = 1
    bx lr                  @ Retornar al llamador
final:
    mov r3, r0
    mov r0, #0
    mov r1, #0
    mov r2, r3 @resultado a imprimir
    bl printInt
    wfi
