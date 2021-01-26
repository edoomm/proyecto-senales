
from senalDiscreta import SenalDiscreta

def obtener_Desplazamiento(senal,direccion,tamanioDesplazamiento): #Desplazamientos si es 1 se desplaza a la Derecha si es 2 a la izquierda
    desplazamiento=[] #Lista auxiliar donde se guardaran los desplazamientos
    if(direccion==1):     
        datosAux = senal.obtener_datos()
        for i in range(0, tamanioDesplazamiento):
            desplazamiento.append(0)
        datosAux=desplazamiento+datosAux
        return SenalDiscreta(datosAux, senal.obtener_indice_inicio(), senal.es_periodica())
    elif(direccion==2):   
        datosAux = senal.obtener_datos()
        for i in range(0, tamanioDesplazamiento):
            desplazamiento.insert(len(desplazamiento), 0)
        datosAux=datosAux+desplazamiento
        return SenalDiscreta(datosAux, senal.obtener_indice_inicio() - tamanioDesplazamiento, senal.es_periodica())

# x = SenalDiscreta([1,2,3],-2,True)
# print(obtener_Desplazamiento(x, 1, 4))
# print(obtener_Desplazamiento(x, 2, 4))