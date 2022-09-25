"""
Crear 10 listas de 10 elementos que dividan los números del 1 al 100
Ejemplo lista1 = [1,2,3,4,5,6,7,8,9,10] lista2 = [11,12,13,14,15,16,17,18,19,20]

Crear una función que reciba un número entero N entre 0 y 9 capturado por el usuario y 
arroje como resultado la suma de todos los elementos en la posición N de las listas

Guardar dicho resultado en una variable e imprimirlo en pantalla
Ej1. Entrada:0  Salida:460
Ej2. Entrada:3: Salida 490
"""
listas = []
for i in range(1,11):
    listas.append([])
    for j in range(1,11):
        listas[i-1].append((10*(i-1)) + j)

def sumarNumsEnPosicion(num):
    suma = 0
    for i in range(0,10):
        suma += listas[i][num]
    return suma

num = int(input('Ingrese un número del 0 al 9:'))
print(sumarNumsEnPosicion(num))