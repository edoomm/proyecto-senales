from senalDiscreta import SenalDiscreta
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
from scipy.io.wavfile import read, write
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

#Constantes and Variables:
formato=pyaudio.paInt16
canal = 1
frecuenciaDeMuestreo = 44100
tamanioVentana = 1024
tiempoGrabado = 3
nombreAudio = ''
audio = pyaudio.PyAudio()
flujo = audio.open(format=formato,channels=canal,rate=frecuenciaDeMuestreo,input=True,frames_per_buffer=tamanioVentana)
#-----------------------------------------------------------------------------------------------------------------------

def setNomebreAudio(nombre): #Establesemos el nombre del archivo de audio
    nombreAudio=nombre
    nombreAudio=nombreAudio+'.wav'

def getNomebreAudio(): #Obtenemos el Archivo de Audio
    return nombreAudio

def setTiempoDeGrabado(tiempo):
    tiempoGrabado=tiempo

def getTiempoDeGrabado():
    return tiempoGrabado

def grabarAudio():
    print('...Grabando')
    senial=[]
    for i in range(int((frecuenciaDeMuestreo/tamanioVentana)*tiempoGrabado+1)):
        data = flujo.read(tamanioVentana)
        senialDato = np.fromstring(data,dtype=np.int16)
        senial.extend(senialDato)

    print('..fin..')

    wavefile = wave.open("entrada.wav",'wb')
    wavefile.setnchannels(canal)
    wavefile.setsampwidth(audio.get_sample_size(formato))
    wavefile.setframerate(frecuenciaDeMuestreo)
    wavefile.writeframes(b''.join(senial))
    wavefile.close()
     
def obtenerSenalDiscretaDesdeAudio():
    grabarAudio()
    Fr, data = read("entrada.wav") #Leemos archivo obteniendo frecuencia y arreglo con canales
    for i in range(40):
        print(data[i])
    return SenalDiscreta(data, 0, False) #Se toma como data solo el primer canal

def obtenerAudioDesdeSenalDiscreta(senal):
    write("salida.wav", frecuenciaDeMuestreo, np.array(senal.obtener_datos()))

def graficarSenalDiscretaDeAudio(senalVieja, senalNueva):
    x = [0]
    datosViejos = senalVieja.obtener_datos()
    datosNuevos = senalNueva.obtener_datos()
    lenAux = len(datosViejos)
    for i in range(0,lenAux):
        x.append(i)
    plt.figure()
    plt.subplot(121)
    plt.plot(x[0:(lenAux-1)], datosViejos[0:(lenAux-1)], 'o')
    plt.subplot(122)
    plt.plot(x[0:(lenAux-1)], datosNuevos[0:(lenAux-1)], 'o')
    plt.show()

#CODIGO DE PRUEBA
# from operacionReflejo import *
# senal = obtenerSenalDiscretaDesdeAudio()
# senal2 = obtener_reflejo(senal,2)
# graficarSenalDiscretaDeAudio(senal, senal2)
# print(len(senal.obtener_datos()))
# obtenerAudioDesdeSenalDiscreta(senal2)