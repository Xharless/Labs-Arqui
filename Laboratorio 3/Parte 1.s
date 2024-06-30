.data
valores: .word 3, 5, 1, 5, 2    @lista con los paquetes
n: .word 5                      @cantidad de datos en la lista

.text
.global main

main:
    ldr r0, =valores           @cargar direccion de la lista
    ldr r1, =n                 @cargar direccion de la cantidad de datos
    ldr r2, [r1]               @Cargar valor de la cantidad de paquetes
    mov r4, #0                 @inicializar resultado
    mov r5, #0                 @inicializar indice

    cmp r2, #0                 @comparar caso que tenga 0 valores
    beq printear_resultado

    cmp r2, #1                 @comparar caso que tenga 1 valor
    beq final_uno

    b loop

loop:
    cmp r5, r2                 @verificar si se ha procesado todo
    bge printear_resultado

    @calcular la direccion del actual
    mov r7, r5
    lsl r7, r7, #2             
    ldr r6, [r0, r7]           @cargar el actual
    add r4, r4, r6             @ Acumular el valor del paquete actual

    add r3, r5, #3             @indice despues de saltar dos
    cmp r3, r2
    blt procesar_siguiente

    add r5, r5, #3             @saltar dos
    b loop

procesar_siguiente:
    add r5, r5, #1
    b loop

final_uno:
    @sumar el unico dato
    ldr r6, [r0]
    add r4, r4, r6
    b printear_resultado

printear_resultado:
    @printear resultado
    mov r0, #0
    mov r1, #0
    mov r2, r4
    bl printInt
    b end

end:
    wfi
