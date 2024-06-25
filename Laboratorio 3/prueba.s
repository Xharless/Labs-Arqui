.data
valores: .word 1, 2, 3, 4, 5    
n: .word 5                      

.text
.global main

main:
    ldr r0, =valores           
    ldr r1, =n                 
    ldr r2, [r1]               
    mov r4, #0               
    mov r5, #0                 

    cmp r2, #0                
    beq printear_resultado


loop:
    cmp r5, r2                 
    bge printear_resultado

    lsl r6, r5, #2             
    ldr r6, [r0, r6]          
    add r4, r4, r6             
    add r3, r5, #3             
    cmp r3, r2
    bge printear_resultado    

    lsl r7, r3, #2             
    ldr r7, [r0, r7]         
    cmp r6, r7
    blt salto     
    add r5, r5, #1            
    b loop

salto:
    add r5, r5, #3             
    b loop

printear_resultado:
    mov r0, #0
    mov r1, #0
    mov r2, r4
    bl printInt
    b end

end:
    wfi
