from senalDiscreta import SenalDiscreta
from manejadorDeSenales import obtenerSenalDiscretaDesdeAudio,obtenerAudioDesdeSenalDiscreta,graficarSenalDiscretaDeAudio

def obtener_Desplazamiento(senal,tamanioDesplazamiento): #Desplazamientos si es 1 se desplaza a la Derecha si es 2 a la izquierda
    desplazamiento=[] #Lista auxiliar donde se guardaran los desplazamientos
    datosAux=[]
    tamanioDesplazamiento*=(-1)
    if(tamanioDesplazamiento>0):     
        datosAux = senal.obtener_datos()
        for i in range(0, tamanioDesplazamiento):
            desplazamiento.append(0)
        desplazamiento=desplazamiento+datosAux
        return SenalDiscreta(desplazamiento, senal.obtener_indice_inicio() - tamanioDesplazamiento, senal.es_periodica())
    elif(tamanioDesplazamiento<0):  
        tamanioDesplazamiento*=(-1) 
        Aux = senal.obtener_datos()[::-1]
        for i in range(tamanioDesplazamiento):
           # desplazamiento.insert(len(desplazamiento), 0)
           Aux.pop()  
        Aux=Aux[::-1]
        for i in range(tamanioDesplazamiento):
            Aux.append(0)
        return SenalDiscreta(Aux, senal.obtener_indice_inicio() + tamanioDesplazamiento, senal.es_periodica())

def DesplazarCompleto(tamanioDesplazamiento):
    senial=obtenerSenalDiscretaDesdeAudio()
    senial2=obtener_Desplazamiento(senial,tamanioDesplazamiento)
    graficarSenalDiscretaDeAudio(senial,senial2)
    obtenerAudioDesdeSenalDiscreta(senial2)


DesplazarCompleto(44100)

# x = SenalDiscreta([1,2,3],-2,True)
# print(obtener_Desplazamiento(x, 1, 4))
# print(obtener_Desplazamiento(x, 2, 4))