from senalDiscreta import SenalDiscreta

#Funcion que calcula la pendiente que es usada para la interpolación
#Recibe un valor y1, un valor y2 y el factor de interpolacion
def obtenerPendiente(y1,y2,factor):
    return float((y2-y1)/(factor))

#Esta funcion recibe un numero y devuelve un float con solo un decimal
def a1decimal(n):
    return float(int(n*10))/10

#Función que calcula la interpolacion
#Recibe como parámetros un objeto de tipo señaldiscreta y el factor de interpolacion
def obtenerInterpolacion(xn,factor):
    x = xn.obtener_datos()
    y = []
    # solo funciona para listas del mismo tamaño
    for i in range(0, len(x)-1):
        m = obtenerPendiente(x[i],x[i+1],factor)
        y.append(x[i])
        for j in range(1, factor):
            y.append(a1decimal(float(x[i]+(m*j))))
    print(y)
    y.append(x[i+1])
    return SenalDiscreta(y, xn.obtener_indice_inicio()*factor, xn.es_periodica())

#Función que calcula la diezmacion
#Recibe como parámetros un objeto de tipo señaldiscreta y el factor de diezmacion
def obtenerDiezmacion(xn,factor):
    x = xn.obtener_datos().copy()
    inicio = xn.obtener_indice_inicio()
    origen = xn.obtener_origen()
    index = int(0)
    print(f"Secuencia: {x}, origen {origen}")
    for i in range(len(x)):
        pointer = inicio+i
        if pointer%factor != 0:
            del x[index]
            if pointer >= 0:
                origen -= 1
        else:
            index += 1
    print(f"Secuencia: {x}, origen {origen}")
    return SenalDiscreta(x, -origen, xn.es_periodica())