#Ejercicio 1
def secuencia(n,m):
    lista = [n]

    while n != 1:
        if n % m != 0:
            return 'Secuencia invalida'
        n = n/m
        lista.append(int(n))
    return lista


n = int(input('n: ')
        )
m = int(input('m: '))

resultado = secuencia(n,m)
print('Resultado'.center(50,'='))
print(f'n: {n}')
print(f'm: {m}')
print(f'secuencia: {resultado}')

