import random
from prettytable import PrettyTable

def crear_mapa(size,cantidad_naves):
    listaposnaves = []
    lista = []
    for i in range(0,size*2):
        row = []
        for j in range(0,size):
            row.append('?')
        lista.append(row)

    for i in range(0,cantidad_naves):
        cordx = random.randint(0,2*size-1)
        cordy = random.randint(0,size-1)
        tipo = random.randint(0,2)
        tipos = 'XYZ'
        if lista[cordx][cordy] != '?':
            print("Coordenadas de nave", i, "colisionaron con otra nave, no se añade al mapa")
            continue
        else:
            lista[cordx][cordy] = tipos[tipo]
            listaposnaves.append((cordx,cordy))

    return(lista,listaposnaves)

def visualizar_mapa(lista):
    tabla = PrettyTable()

    tabla.field_names = [''] + list(range(len(lista[0])))

    for numberfila, row in enumerate(lista):
        row_data = [numberfila] + row
        tabla.add_row(row_data)

    print(tabla)

'''
--------------------------------------------------------------------------
'''

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


tamano = input("Tamano del tablero: ")
cant_enemigos = input("Cantidad de enemigos: ")
cant_bajados = 0

try:
    juego,enemigos = crear_mapa(int(tamano),int(cant_enemigos))

    flag = True
    while flag:
        
        visualizar_mapa(juego) 

        if int(cant_enemigos) == cant_bajados:
            print("")
            print("-----------------------------")
            print("¡HAS GANADO, FELICIDADES!")
            print("-----------------------------")
            break
        
        print("Escoge en que base deseas trabajar: ")
        print("Opcion 1: Base binaria (X)")
        print("Opcion 2: Base octal (Y)")
        print("Opcion 3: Base hexadecimal (Z)")
        print("Opcion 4: Salir")
        print('\n')
        opcion = input("Escoge una opcion: ")
        
        if opcion == "1":
            #funcion binario
            coordenadas_x = input("Coordenadas en X?: ")
            coordenadas_y = input("Coordenadas en Y?: ")
            resultado = bin_dec(coordenadas_x,coordenadas_y)
            
            x = verificar_mapa(resultado[0],resultado[1],juego,opcion)
            if x == "Barco fuera!!":
                print(x)
                cant_bajados+=1

        elif opcion == "2":
            #funcion octal 
            coordenadas_x = input("Coordenadas en X?: ")
            coordenadas_y = input("Coordenadas en Y?: ")
            resultado = octal_dec(coordenadas_x,coordenadas_y)
            
            y = verificar_mapa(resultado[0],resultado[1],juego,opcion)
            if y == "Barco fuera!!":
                print(y)
                cant_bajados+=1

        elif opcion == "3":
            #funcion hexadecimal 
            coordenadas_x = input("Coordenadas en X?: ")
            coordenadas_y = input("Coordenadas en Y?: ")
            resultado = hexa_dec(coordenadas_x.upper(),coordenadas_y.upper())
            
            z = verificar_mapa(resultado[0],resultado[1],juego,opcion)
            if z == "Barco fuera!!":
                print(z)
                cant_bajados+=1


        elif opcion == "4":
            flag = False
        
        else:
            print("Escoge una opcion valida")

except:
    print("Ingresa un numero entero")