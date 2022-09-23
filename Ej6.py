
def listas(lista1,lista2):
    coinciden = []
    noCoinciden = []
    [coinciden.append(val) for val in lista1 if (val in lista2 and not val in coinciden)]
    [lista1.append(val) for val in lista2 if not val in lista1 ]
    [noCoinciden.append(val) for val in lista1 if not val in coinciden]
    return coinciden , noCoinciden

lista1 = ['a','b',2,3]
lista2 = ['c','d',3,4]

coinciden,noCoinciden = listas(lista1,lista2)

print(f'Ejemplo 1'.center(50,'='))
print(f'Salida: {coinciden} {noCoinciden}')

lista1 = ['a','b',2,3]
lista2 = ['c','d',4]

coinciden,noCoinciden = listas(lista1,lista2)

print(f'Ejemplo 2'.center(50,'='))
print(f'Salida: {coinciden} {noCoinciden}')

lista1 = ['a','b',2,2,3]
lista2 = ['c','d',2,'a',4]

coinciden,noCoinciden = listas(lista1,lista2)

print(f'Ejemplo 3'.center(50,'='))
print(f'Salida: {coinciden} {noCoinciden}')