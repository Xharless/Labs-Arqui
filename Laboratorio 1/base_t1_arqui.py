from funciones import *
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
        cordx = random.randint(0,size-1)
        cordy = random.randint(0,size-1)
        tipo = random.randint(0,2)
        tipos = 'XYZ'
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

juego,enemigos = crear_mapa(5,5)
visualizar_mapa(juego)


flag = True
while flag: 
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
        x = bin_dec(coordenadas_x,coordenadas_y)
        print(x)

    elif opcion == "2":
        #funcion octal 
        coordenadas_x = input("Coordenadas en X?: ")
        coordenadas_y = input("Coordenadas en Y?: ")
        x = octal_dec(coordenadas_x,coordenadas_y)
        print(x)

    elif opcion == "3":
        #funcion hexadecimal 
        coordenadas_x = input("Coordenadas en X?: ")
        coordenadas_y = input("Coordenadas en Y?: ")
        x = hexa_dec(coordenadas_x,coordenadas_y)
        print(x)

    elif opcion == "4":
        flag = False

    else:
        print("Escoge una opcion valida")