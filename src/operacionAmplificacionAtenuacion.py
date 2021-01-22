def obtenerAmplificacionAtenuacion(x,multiplicador):
    y = []
    # solo funciona para listas del mismo tamaño
    for i in range(0, len(x)):
        y.append(x[i]*multiplicador)

    return y