from senalDiscreta import SenalDiscreta

def obtener_reflejo(senal, tipoReflejo):
    if(tipoReflejo==1):     #Para reflejo sobre el eje X
        datosAux = senal.obtener_datos()
        for i in range(len(datosAux)):
            datosAux[i] = datosAux[i] * -1
        return SenalDiscreta(datosAux, senal.obtener_indice_inicio(), senal.es_periodica())
    elif(tipoReflejo==2):   #Para reflejo sobre el eje y
        datosAux = senal.obtener_datos()[::-1]
        inicioAux = - len(datosAux) + 1 - senal.obtener_indice_inicio()
        return SenalDiscreta(datosAux, inicioAux, senal.es_periodica())

#CODIGO DE PRUEBA:
# senal1 = SenalDiscreta([1, 2, 3, 4], -2, False)
# print("Senal original:")
# print(senal1)
# print("Reflejo en X:")
# print(obtener_reflejo(senal1, 1))
# print("Reflejo en Y:")
# print(obtener_reflejo(senal1, 2))