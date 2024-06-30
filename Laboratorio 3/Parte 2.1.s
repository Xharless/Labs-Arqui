.data
valores: .word 3, 5, 1, 5, 2    @ Lista con los paquetes
n: .word 5                      @ Cantidad de datos

.text
.global main

main:
    ldr r0, =valores           @ Dirección de la lista
    ldr r1, =n                 @ Dirección de la cantidad de paquetes
    ldr r2, [r1]               @ Cargar valor de la cantidad de paquetes
    mov r4, #0                 @ Inicializar el resultado
    mov r5, #0                 @ Inicializar índice

    cmp r2, #0                 @ Comparar caso que tenga 0 valores
    beq printear_resultado

    cmp r2, #1                 @ Comparar caso que tenga 1 valor
    beq final_uno

    b loop

loop:
    cmp r5, r2                 @ Verificar si se ha procesado todos los paquetes
    bge printear_resultado

    @ Calcular la dirección del paquete actual
    mov r7, r5
    lsl r7, r7, #2             @ r7 = r5 * 4 (tamaño de palabra)
    ldr r6, [r0, r7]           @ Cargar el paquete actual
    add r4, r4, r6             @ Acumular el valor del paquete actual

    add r3, r5, #3             @ r3 = r5 + 3 (índice después de saltar dos paquetes)
    cmp r3, r2
    blt procesar_siguiente

    add r5, r5, #3             @ Aquí saltas dos paquetes completos
    b loop

procesar_siguiente:
    add r5, r5, #1
    b loop

final_uno:
    @ Sumar el último paquete si solo hay uno
    ldr r6, [r0]
    add r4, r4, r6
    b printear_resultado

printear_resultado:
    @ Printear el resultado
    mov r0, #0
    mov r1, #0
    mov r2, r4
    bl printInt
    b end

end:
    wfi
