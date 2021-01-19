def obtenersuma(x, h):
    y = []
    # solo funciona para listas del mismo tamaño
    if len(x) != len(h):
        return []
    for i in range(0, len(x)):
        y.append(x[i] + h[i])

    return y