from numpy import convolve, zeros
from SenalDiscreta import *
from math import ceil


# Se obtiene la convolucion entre dos senales finitas y = x * h
def obtener_convolucion_finita (x, h):
    y = SenalDiscreta()
    nuevo_indice_inicio = x.obtener_indice_inicio() + h.obtener_indice_inicio()
    y.asignar_datos(convolve(x, h)) # Convolve es la convolucion finita ya impleementada
    y.asignar_indice_inicio(nuevo_indice_inicio)


def obtener_convolucion_periodica (x, h):
    # se tomara a h como la discreta
    if ( x.es_periodica() ):
        x, h = h, x # swap (x, h)
    # el periodo es la longitud del arreglo

    arr1, arr2 = x.obtener_datos(), h.obtener_datos()
    T = len(arr2)
    nueva_longitud = len(arr1) + len(arr2) - 1
    nuevo_indice_inicio = x.obtener_indice_inicio() + h.obtener_indice_inicio()

    # aplicamos el algoritmo de multiplicacion de columnas
    resultados = [[0 for i in range(nueva_longitud)] for j in range(T)]
    for i in range (0, len(arr2)):
        for j in range(0, len(arr1)):
            resultados[i][i + j] = arr2[i] * arr1[j]
    resultado = [0 for i in range(nueva_longitud)]
    for i in range (0, T):
        for j in range (0, nueva_longitud):
            resultado[j] += resultados[i][j]

    # Seguimos con el algoritmo de convolucion periodica
    relleno = T - len(resultado) % T
    resultado.extend([0] * relleno)
    convolucion = [0 for i in range(T)]
    for i in range (0, len(resultado)):
        convolucion[i % len(convolucion)] += resultado[i]

    return SenalDiscreta(convolucion, nuevo_indice_inicio % T, True)


a = SenalDiscreta([5, 0, 4, 2], -2, False)
b = SenalDiscreta([3, 2], 0, True)

y = obtener_convolucion_periodica(a, b)

print(y)