"""
Una chocolatería lanzará un nuevo producto el cual viene presentado en barras de N Segmentos.
Las barras solo vienen en tamaño que son potencia de 2, es decir, {1,2,4,8,16,32,64,128,256}

Realizar un programa para realizar una prueba de calidad de dicho producto, pero par ello 
tienes que probar al menos K Segmentos

EL problema es que la barra solo se puede partirt a la mitad,

Dicho programa determinará el número de veces que quebrarás la barra para obtener exactamente K segmentos.

La salida será el tamaño mínimo de barras que se tendrá que pedir para tomar los K segmentos y 
el segundo número es el número de veces que tendrás que romper la barra
Ej1: Entrada:5 Salida 8,3
Ej2: Entrada:6 Salida 8,2
"""
def probarYQuebrar(k):
    tamanio = 1
    while(tamanio <= k):
        tamanio = tamanio * 2
    segmentos = 0
    partidas = 0
    tempTamanio = tamanio
    while(segmentos != k):
        partidas += 1
        tempTamanio = tempTamanio / 2
        if(tempTamanio + segmentos <=k):
            segmentos = segmentos + tempTamanio
    return tamanio, partidas

segmentosATomar = int(input('Ingrese la cantidad de segmentos a tomar:\n'))
print(probarYQuebrar(segmentosATomar))