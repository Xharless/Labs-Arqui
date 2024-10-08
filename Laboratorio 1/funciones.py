import random
from prettytable import PrettyTable


'''
verificar_mapa
———————–
coor_x: int
coor_y: int
mapa: lista
opcion: str
————————
Comprueba que las coordenadas ingresadas esten dentro del mapa,
ademas verifica si la opcion escogida corresponde al barco ha destruir.
Retorna un string indicando si erraste o lo eliminaste.
'''
def verificar_mapa(coor_x, coor_y, mapa, opcion):
    # 'E' de ELIMINATED o ELIMINADO
    # Verifico si la opcion marcada coincide con el barco en cuestion
        
    try:
        if mapa[coor_x][coor_y] == 'X' and opcion == '1':
            mapa[coor_x][coor_y] = 'E'
            return "Barco fuera!!"

        elif mapa[coor_x][coor_y] == 'Y' and opcion == '2':
            mapa[coor_x][coor_y] = 'E'
            return "Barco fuera!!"
            

        elif mapa[coor_x][coor_y] == 'Z' and opcion == '3':
            mapa[coor_x][coor_y] = 'E'
            return "Barco fuera!!"
            

        else:
            return print("Erraste :C")
        
    except:
        print("Te excediste del mapa!!")    


'''
bin_dec
———————–
coor_x: str
coor_y: str
————————
Recorre ambas coordenadas que estan en binario, transformando uno por uno
los numeros a decimal utilizando las potencias del 2. Retorna una tupla con
las coordenadas x e y en int.
'''
def bin_dec(coor_x, coor_y):
    largo_x = len(coor_x) 
    largo_y = len(coor_y)
    x_decimal = 0
    y_decimal = 0
    
    for x in coor_x:
        if largo_x >= 0:
            x_decimal +=  int(x) * 2**(largo_x - 1)
            largo_x -= 1
    
    for y in coor_y:
        if largo_y >= 0:
            y_decimal +=  int(y) * 2**(largo_y - 1)
            largo_y -= 1
    
    return (x_decimal,y_decimal)


'''
octal_dec
———————–
coor_x: str
coor_y: str
————————
Recorre ambas coordenadas que estan en octal, transformando uno por uno
los numeros a decimal utilizando las potencias del 8. Retorna una tupla con
las coordenadas x e y en int.
'''
def octal_dec(coor_x, coor_y):
    largo_x = len(coor_x)
    largo_y = len(coor_y)
    x_decimal = 0
    y_decimal = 0
    
    for x in coor_x:
        if largo_x >= 0:
            x_decimal +=  int(x) * 8**(largo_x - 1)
            largo_x -= 1
    
    for y in coor_y:
        if largo_y >= 0:
            y_decimal +=  int(y) * 8**(largo_y - 1)
            largo_y -= 1

    return (x_decimal,y_decimal)


'''
hexa_dec
———————–
coor_x: str
coor_y: str
————————
Se tiene un diccionario con las letras y su respectivo valor decimal.
Recorre ambas coordenadas que estan en hexadecimal, transformando uno por uno
los numeros a decimal utilizando las potencias del 16, verifica si es una letra
o un numero para utilizar su valor decimal. Retorna una tupla con las coordenadas
x e y en int.
'''
def hexa_dec(coor_x, coor_y):
    letras = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    largo_x = len(coor_x)
    largo_y = len(coor_y)
    x_decimal = 0
    y_decimal = 0

    for x in coor_x:
        if largo_x >= 0:    
            if x.isalpha():
                x_decimal += letras[x] * 16**(largo_x - 1)
                largo_x -= 1  
            else:
                x_decimal += int(x) * 16**(largo_x - 1)
                largo_x -= 1
    
    for y in coor_y:
        if largo_y >= 0:    
            if y.isalpha():
                y_decimal += letras[y] * 16**(largo_y - 1)
                largo_y -= 1  
            else:
                y_decimal += int(y) * 16**(largo_y - 1)
                largo_y -= 1
    
    return (x_decimal,y_decimal)
