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

a = input()