# from numpy import convolve, zeros
from SenalDiscreta import *
# from math import ceil

def convolucionar (x, h):
    # Se verifica que tipo de convolucion es y se llama a la función 
    # correspondiente
    if (not x.es_periodica()) and (not h.es_periodica()):
        return obtener_convolucion_finita(x, h)
    if (x.es_periodica()) and (not h.es_periodica()):
        return obtener_convolucion_periodica(x, h)
    if (not x.es_periodica()) and (h.es_periodica()):
        return obtener_convolucion_periodica(x, h)
    if x.es_periodica() and h.es_periodica():
        return obtener_convolucion_circular(x, h)



def convolucionar_arreglos (arr1, arr2):
    T = len(arr2)
    nueva_longitud = len(arr1) + len(arr2) - 1

    # aplicamos el algoritmo de multiplicacion de columnas
    resultados = [[0 for i in range(nueva_longitud)] for j in range(T)]
    for i in range(0, len(arr2)):
        for j in range(0, len(arr1)):
            resultados[i][i + j] = arr2[i] * arr1[j]
    resultado = [0 for i in range(nueva_longitud)]
    for i in range(0, T):
        for j in range(0, nueva_longitud):
            resultado[j] += resultados[i][j]

    return resultado


# Se obtiene la convolucion entre dos senales finitas y = x * h
def obtener_convolucion_finita (x, h):
    y = SenalDiscreta()
    nuevo_indice_inicio = x.obtener_indice_inicio() + h.obtener_indice_inicio()
    y.asignar_datos(convolucionar_arreglos(x.obtener_datos(), h.obtener_datos())) # Convolve es la convolucion finita ya impleementada
    y.asignar_indice_inicio(nuevo_indice_inicio)
    return y


def obtener_convolucion_periodica (x, h):
    # se tomara a h como la finita
    if ( x.es_periodica() ):
        x, h = h, x # swap (x, h)
    # el periodo es la longitud del arreglo

    arr1, arr2 = x.obtener_datos(), h.obtener_datos()
    T = len(arr2)
    nueva_longitud = len(arr1) + len(arr2) - 1
    nuevo_indice_inicio = x.obtener_indice_inicio() + h.obtener_indice_inicio()

    resultado = convolucionar_arreglos (arr1, arr2)

    # Seguimos con el algoritmo de convolucion periodica
    relleno = T - len(resultado) % T
    resultado.extend([0] * relleno)
    convolucion = [0 for i in range(T)]
    for i in range (0, len(resultado)):
        convolucion[i % len(convolucion)] += resultado[i]

    return SenalDiscreta(convolucion, (nuevo_indice_inicio % T) * -1, True)

def obtener_convolucion_circular (x, h):
    arr1, arr2 = x.obtener_datos(), h.obtener_datos()
    # el periodo es la longitud del arreglo
    T = max(len(arr1), len(arr2))

    nuevo_indice_inicio = x.obtener_indice_inicio() + h.obtener_indice_inicio()

    resultado = convolucionar_arreglos (arr1, arr2)

    # Seguimos con el algoritmo de convolucion periodica
    relleno = T - len(resultado) % T
    resultado.extend([0] * relleno)
    convolucion = [0 for i in range(T)]
    for i in range (0, len(resultado)):
        convolucion[i % len(convolucion)] += resultado[i]

    return SenalDiscreta(convolucion, (nuevo_indice_inicio % T) * -1, True)

a = SenalDiscreta([-1,2,7], -1, True)
b = SenalDiscreta([-1,1], 0, True)

y = convolucionar(a, b)


print(y)