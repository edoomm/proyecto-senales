from senalDiscreta import SenalDiscreta
import numpy as np
from IPython.display import Audio
from scipy.io.wavfile import read, write

#Constantes:
Frec = 44100

def obtenerSenalDiscretaDesdeGrabacion():
    print() #Aqui necesitamos grabar el WAV de tres segundos y 
    #guardarlo con el nombre de "entrada.wav" en el folder de "src"
    return obtenerSenalDiscretaDesdeAudio() 

def obtenerSenalDiscretaDesdeAudio():
    Fr, data = read("src/entrada.wav") #Leemos archivo obteniendo frecuencia y arreglo con canales
    return SenalDiscreta(data[:,0], 0, False) #Se toma como data solo el primer canal

def obtenerAudioDesdeSenalDiscreta(senal):
    write("src/salida.wav", Frec, np.array(senal.obtener_datos()))

#CODIGO DE PRUEBA:
# senal = obtenerSenalDiscretaDesdeAudio()
# obtenerAudioDesdeSenalDiscreta(senal)