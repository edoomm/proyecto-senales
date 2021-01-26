from senalDiscreta import SenalDiscreta
from scipy.fft import fft, fftfreq, fftshift
import numpy
import matplotlib.pyplot as plt

def obtener_FFT(senal): #Obtenemos la FFT de la secuencia
    datosAux = senal.obtener_datos() #Lista auxiliar donde se guardaran los desplazamientos
    array = numpy.array(datosAux) #Convertimos esa lista auxiliar a un arreglo de numpy
    transformada = fft(array) #Obtenemos la fft
    transformada = numpy.around(transformada, 2)
    #graficarFFT(transformada)
    return SenalDiscreta(transformada.tolist(), senal.obtener_indice_inicio(), senal.es_periodica()) #Retornamos la senial

def graficarFFT(transformada):
    yf = transformada
    xf = fftfreq(transformada.size)
    xf = fftshift(xf)
    yplot = fftshift(yf)
    plt.plot(xf, 1 / transformada.size * numpy.abs(yplot))
    plt.grid()
    plt.show()