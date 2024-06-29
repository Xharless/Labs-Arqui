.data
valores: .word 1, 2, 3, 4, 5    @ Lista con los paquetes
n: .word 5                      @ Cantidad de datos

.text
.global main

main:
    ldr r0, =valores           @ Dirección de la lista
    ldr r1, =n                 @ Dirección de la cantidad de paquetes
    ldr r2, [r1]               @ Cargar valor de la cantidad de paquetes
    mov r4, #0                 @ Inicializar el resultado (suma acumulada)
    mov r5, #0                 @ Inicializar índice

    cmp r2, #0                 @ Comparar caso que tenga 0 valores
    beq printear_resultado

    @ Loop para maximizar la cantidad de datos procesados
loop:
    cmp r5, r2                 @ Verificar si se ha procesado todos los paquetes
    bge printear_resultado

    lsl r6, r5, #2             @ Calcular el desplazamiento (r5 * 4)
    ldr r6, [r0, r6]           @ Cargar el paquete actual (valores[r5])
    add r4, r4, r6             @ Sumar el valor del paquete actual a la suma acumulada

    @ Decidir entre saltar los siguientes dos paquetes o avanzar al siguiente
    add r3, r5, #3             @ r3 = r5 + 3 (índice después de saltar dos paquetes)
    cmp r3, r2
    bge printear_resultado     @ Saltar si no hay más paquetes después

    lsl r7, r3, #2             @ Calcular el desplazamiento (r3 * 4)
    ldr r7, [r0, r7]           @ Cargar el paquete después de saltar dos (valores[r3])

    @ Comparar y decidir si avanzar al siguiente paquete o saltar los siguientes dos
    cmp r6, r7
    blt skip_two_packages      @ Saltar si el paquete siguiente es mayor

    add r5, r5, #1             @ Avanzar al siguiente paquete
    b loop

skip_two_packages:
    add r5, r5, #3             @ Saltar los siguientes dos paquetes
    b loop

printear_resultado:
    @ Printear el resultado
    mov r0, #0
    mov r1, #0
    mov r2, r4
    bl printInt
    b end

end:
    wfi
