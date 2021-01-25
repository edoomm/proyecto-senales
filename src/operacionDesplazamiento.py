
from senalDiscreta import SenalDiscreta

def obtener_Desplazamiento(senal,direccion,tamanioDesplazamiento): #Desplazamientos si es 1 se desplaza a la Derecha si es 2 a la izquierda
    desplazamiento=[] #Lista auxiliar donde se guardaran los desplazamientos
    if(direccion==1):     
        datosAux = senal.obtener_datos()
        for i in tamanioDesplazamiento:
            desplazamiento[i] = 0
        datosAux=desplazamiento+datosAux
        return SenalDiscreta(datosAux, senal.obtener_indice_inicio() + tamanioDesplazamiento, senal.es_periodica())
    elif(direccion==2):   
        datosAux = senal.obtener_datos()
        for i in range(len(datosAux)):
            if(i>=tamanioDesplazamiento):
                desplazamiento.append(datosAux(i))
        return SenalDiscreta(desplazamiento,senal.obtener_indice_inicio - tamanioDesplazamiento , senal.es_periodica())