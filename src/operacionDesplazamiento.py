from senalDiscreta import SenalDiscreta
from manejadorDeSenales import obtenerSenalDiscretaDesdeAudio,obtenerAudioDesdeSenalDiscreta,graficarSenalDiscretaDeAudio


def desplazar_unidad(senal, n):
    if n < 0: 
        if senal.obtener_origen() > 0:
            nuevo_indice_inicio = senal.obtener_indice_inicio() + 1
            senal.asignar_indice_inicio(nuevo_indice_inicio)
        else:
            senal.expandir_izquierda(1)
            senal.asignar_indice_inicio(0)
    elif n > 0:
        if senal.obtener_origen() < senal.obtener_longitud() - 1:
            senal.asignar_indice_inicio(senal.obtener_indice_inicio() - 1)
        else:
            senal.expandir_derecha(1)
            senal.asignar_indice_inicio(senal.obtener_indice_inicio() - 1)

# Función que se llama desde la GUI
def obtener_desplazamiento (senial, desplazamiento):
    if not senial.es_periodica() and abs(desplazamiento) >= senial.obtener_longitud():
        return SenalDiscreta([0 for i in range(senial.obtener_longitud())], senial.obtener_indice_inicio(), senial.es_periodica())


    if senial.es_periodica():
        desplazamiento*=-1
        datosAux= senial.obtener_datos()[:]
        nuevosDatos = datosAux[-desplazamiento:] + datosAux[:-desplazamiento] 
        return SenalDiscreta(nuevosDatos, senial.obtener_indice_inicio(), senial.es_periodica())
    else:
        datosAux = senial.obtener_datos()[:]
        cerosAux = []
        for i in range(abs(desplazamiento)):
            cerosAux.append(0)
        if(desplazamiento<=0):
            for j in range(abs(desplazamiento)):
                datosAux.pop()
            return SenalDiscreta(cerosAux+datosAux, senial.obtener_indice_inicio(), senial.es_periodica())
        else:
            datosAux = datosAux[::-1]
            for j in range(desplazamiento):
                datosAux.pop()
            datosAux = datosAux[::-1]
            return SenalDiscreta(datosAux+cerosAux, senial.obtener_indice_inicio(), senial.es_periodica())

def Xobtener_desplazamiento (senial, desplazamiento):
    indice_actual = senial.obtener_indice_inicio()
    nuevo_indice = indice_actual - desplazamiento
    if senial.es_periodica():
        if desplazamiento > 0:
            senial.expandir_derecha(abs(desplazamiento))
        else:
            senial.expandir_izquierda(abs(desplazamiento))
            nuevo_indice = indice_actual
        return SenalDiscreta(senial.obtener_datos(), nuevo_indice, senial.es_periodica())
    else:
        auxiliar = [0] * desplazamiento
        if desplazamiento > 0:
            auxiliar =  senial.obtener_datos() + auxiliar
        else:
            auxiliar = auxiliar + senial.obtener_datos()
            nuevo_indice = indice_actual
        return SenalDiscreta(auxiliar, nuevo_indice, senial.es_periodica())


def obtener_Desplazamiento(senal,tamanioDesplazamiento): #Desplazamientos si es 1 se desplaza a la Derecha si es 2 a la izquierda
    desplazamiento=[] #Lista auxiliar donde se guardaran los desplazamientos
    datosAux=[]
    return obtener_desplazamiento(senal, tamanioDesplazamiento)
    if senal.es_periodica():
        return desplazarPeriodica(senal, tamanioDesplazamiento)
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
    else:
        return senal

def desplazarPeriodica(senal, desplazamiento):
    indice_actual = senal.obtener_indice_inicio()
    if desplazamiento < 0:
        senal.expandir_derecha(abs(desplazamiento))
    else:
        senal.expandir_izquierda(abs(desplazamiento))
    senal.asignar_indice_inicio(indice_actual - desplazamiento)
    return senal


def DesplazarCompleto(tamanioDesplazamiento):
    senial=obtenerSenalDiscretaDesdeAudio()
    senial2=obtener_Desplazamiento(senial,tamanioDesplazamiento)
    graficarSenalDiscretaDeAudio(senial, senial2)
    obtenerAudioDesdeSenalDiscreta(senial2)
    graficarSenalDiscretaDeAudio(senial,senial2)

# def desplazarPeriodica(senal, desplazamiento):
#     indice_actual = senal.obtener_indice_inicio()
#     if desplazamiento < 0:
#         senal.expandir_derecha(abs(desplazamiento))
#     else:
#         senal.expandir_izquierda(abs(desplazamiento))
#     senal.asignar_indice_inicio(indice_actual - desplazamiento)
#     return SenalDiscreta(senal.obtener_datos(), senal.obtener_indice_inicio(), senal.es_periodica())

def obtener_DesplazamientoAudio(senal,tamanioDesplazamiento): #Desplazamientos si es 1 se desplaza a la Derecha si es 2 a la izquierda
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

def DesplazarCompletoAudio(tamanioDesplazamiento):
    senial=obtenerSenalDiscretaDesdeAudio()
    senial2=obtener_DesplazamientoAudio(senial,tamanioDesplazamiento)
    obtenerAudioDesdeSenalDiscreta(senial2)
    graficarSenalDiscretaDeAudio(senial,senial2)

