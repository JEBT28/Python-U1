#Ejercicio 1
def secuencia(n,m):
    lista = [n]

    while n != 1:
        if n % m != 0:
            return 'Secuencia invalida'
        n = n/m
        lista.append(int(n))
    return lista


n = 125
m = 5

resultado = secuencia(n,m)
print('Prueba'.center(50,'='))
print(f'n: {n}')
print(f'm: {m}')
print(f'secuencia: {resultado}')

n = 30
m = 3

resultado = secuencia(n,m)
print('Prueba'.center(50,'='))
print(f'n: {n}')
print(f'm: {m}')
print(f'secuencia: {resultado}')

n = 256
m = 2

resultado = secuencia(n,m)
print('Prueba'.center(50,'='))
print(f'n: {n}')
print(f'm: {m}')
print(f'secuencia: {resultado}')

n = 256
m = 3

resultado = secuencia(n,m)
print('Prueba'.center(50,'='))
print(f'n: {n}')
print(f'm: {m}')
print(f'secuencia: {resultado}')