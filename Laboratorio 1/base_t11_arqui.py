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
            resultado = hexa_dec(coordenadas_x,coordenadas_y)
            
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