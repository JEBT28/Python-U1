#Ejercicio 2
def calcularMayor(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

n1 = int(input('Ingrese el primer número: ')[::-1])
n2 = int(input('Ingrese el segundo número: ')[::-1])
print(calcularMayor(n1,n2))