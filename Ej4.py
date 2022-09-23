
cadena = input("Ingresa la cadena: ")
def calcularFrecuenciaPalabras(cadena):
    listaCadena = cadena.split(" ")
    diccionarioPalabras = {}
    for palabra in listaCadena:
        diccionarioPalabras[palabra] = listaCadena.count(palabra)
    return diccionarioPalabras

def calcularPalabrasMasRepetidas(**karg):
    values = karg.values()
    valorMasAlto = max(values)
    listaPalabrasMasRepetidas = []
    for key,value in karg.items():
        if value == valorMasAlto:
            listaPalabrasMasRepetidas.append(key)
            listaPalabrasMasRepetidas.append(value)
    return tuple(listaPalabrasMasRepetidas)    

resDicc = calcularFrecuenciaPalabras(cadena)

print(calcularPalabrasMasRepetidas(**resDicc))
