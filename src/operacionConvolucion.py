# from numpy import convolve, zeros
from senalDiscreta import SenalDiscreta
# from math import ceil

# Esta es la interfaz que se debe usar desde otras clases.
# Verifica que tipo de seniales son (periodica y/o finita) y
# llama a la funcion correspondiente
def convolucionar (x, h):
    # Se verifica que tipo de convolucion es y se llama a la funcion
    # correspondiente
    if (not x.es_periodica()) and (not h.es_periodica()):
        return obtener_convolucion_finita(x, h)
    if (x.es_periodica()) and (not h.es_periodica()):
        return obtener_convolucion_periodica(x, h)
    if (not x.es_periodica()) and (h.es_periodica()):
        return obtener_convolucion_periodica(x, h)
    if x.es_periodica() and h.es_periodica():
        return obtener_convolucion_circular(x, h)


# Funcion que obtiene la convolucion entre dos arreglos
# Se usa la tecnica de suma por columnas
def convolucionar_arreglos (arr1, arr2):
    nueva_longitud = len(arr1) + len(arr2) - 1

    # aplicamos el algoritmo de suma de columnas
    # creamos una matriz de 0s de la nueva_longitud x el tamanio del arreglo 2
    resultados = [[0 for i in range(nueva_longitud)] for j in range(len(arr2))]
    for i in range(0, len(arr2)):
        for j in range(0, len(arr1)):
            resultados[i][i + j] = arr2[i] * arr1[j]
    # en resultados se guardan los resultados de las multiplicaciones.
    # por ejemplo:
    #   para [1,2,3] * [5,2]
    #   resultados = [
    #                   [5,10,15,0]
    #                   [0, 2, 4,6]
    #                ]

    # Sumamos por filas la matriz resultados:
    #   para
    #   resultados = [
    #                   [5,10,15,0]
    #                   [0, 2, 4,6]
    #                ]
    #   resultado =     [5,12,19,6]

    resultado = [0 for i in range(nueva_longitud)]
    for i in range(0, len(arr2)):
        for j in range(0, nueva_longitud):
            resultado[j] += resultados[i][j]
    # regresamos el arreglo con el resultado
    return resultado


# Se obtiene la convolucion entre dos senales finitas y = x * h
# se reciben dos seniales (SenalDiscreta) finitas
def obtener_convolucion_finita (x, h):
    # Obtenemos la convolucion entre los dos arreglos
    datos_convolucionados = convolucionar_arreglos(x.obtener_datos(), h.obtener_datos())
    nuevo_indice_inicio = x.obtener_indice_inicio() + h.obtener_indice_inicio()
    return SenalDiscreta(datos_convolucionados, nuevo_indice_inicio, False)


# Se obtiene la convolucion periodica con el algoritmo de clase
# Se reciben dos seniales (SenalDiscreta), una periodica y una finita
def obtener_convolucion_periodica (x, h):
    # se tomara a h como la finita
    if ( x.es_periodica() ):
        x, h = h, x # swap (x, h)
    # x ahora es finita y h periodica

    # Obtenemos los arreglos
    arr1, arr2 = x.obtener_datos(), h.obtener_datos()
    # el periodo es la longitud del arreglo 2
    T = len(arr2)
    nuevo_indice_inicio = x.obtener_indice_inicio() + h.obtener_indice_inicio()

    resultado = convolucionar_arreglos (arr1, arr2)

    # Seguimos con el algoritmo de convolucion periodica
    relleno = T - len(resultado) % T
    resultado.extend([0] * relleno)
    # Acompletamos con 0s el resultado para que se puedan agrupar por grupos
    # de tamanio T = periodo
    convolucion = [0 for i in range(T)]
    for i in range (0, len(resultado)):
        convolucion[i % len(convolucion)] += resultado[i]

    # El indice de inicio es: (nuevo_indice_inicio % T) * -1
    return SenalDiscreta(convolucion, (nuevo_indice_inicio % T) * -1, True)

# Funcion que obtiene la convolucion entre dos seniales discretas
# Ambas seniales son periodicas y de tipo (SenalDiscreta)
def obtener_convolucion_circular (x, h):
    arr1, arr2 = x.obtener_datos(), h.obtener_datos()
    # el periodo es el maximo entre las longitudes de los arreglos
    T = max(len(arr1), len(arr2))

    nuevo_indice_inicio = x.obtener_indice_inicio() + h.obtener_indice_inicio()

    resultado = convolucionar_arreglos (arr1, arr2)

    # Seguimos con el algoritmo de convolucion circular
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