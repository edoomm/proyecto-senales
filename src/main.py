from tkinter import *
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import os # libreria del sistema operativo

ventana = Tk()
#Entradas de los cuadros de texto al meter una
#secuencia de datos
#L= Left (Izquierda), O= Origen , R = Right(Derecha)

xL = StringVar()
xO = StringVar()
xR = StringVar()

hL = StringVar()
hO = StringVar()
hR = StringVar()

# Con el siguiente algoritmo lo que se hace
# es hacer tanto x(n) como h(n) tengan la
# misma cantidad de elementos en el arreglo
# en caso de que una tenga mas, se acompleta
# con 0's ya sea a la izquierda o derecha
# segun sea el caso
newH = []
newX = []
ejeV = []

def crearVentana():
    global ventana
    #Dimenciones de la pantalla
    ventana.geometry("700x650+350+60")
    ventana.title("Proyecto de Señales")
    #Ajuste de la pantalla
    ventana.resizable(width=True, height=False)

def verInicio():
    global ejeV,newX,newH
    newH = []
    newX = []
    ejeV = []


    ###Cree estas variables para poder posicionar
    #de una mejor forma los botones
    #de las funciones basicas
    xPosicion = 100
    yPosicion = 100
    espacio = 65

    #Uso una imagen como fondo, debido a que es la
    #unica forma que encuentro para tapar la
    #ventana anterior, por lo que al crear un
    #nuevo escenario, siempre se tiene que poner esto
    imagenFondo = PhotoImage(file="imgs/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)


    #Etiqueta para escribir en la pantalla
    Label(ventana, text="Entrada:",
          font=("Arial", 30)).place(x=275, y=5)


    Button(ventana, text="Secuencia de valores", cursor="hand2",
           bd=10, background="#b5ead7", height=0, command=introducirValores,
           font=("Arial", 19)).place(x=55, y=70)

    #en donde dice command te debe de dirigir a una pantalla
    #en la cual se puede grabar un audio
    Button(ventana, text="    Señal de audio    ", cursor="hand2",
           bd=10, background="#b5ead7", height=0, command=introducirValores,
           font=("Arial", 19)).place(x=360, y=70)

    Button(ventana, text="Sumar", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio+yPosicion)

    Button(ventana, text="Restar", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion+97, y=espacio + yPosicion)

    #en command debe de diriguirte a la funcion correspondiente
    Button(ventana, text="Amplificación", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*2+yPosicion)

    Button(ventana, text="Atenuación", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion+160, y=espacio * 2 + yPosicion)

    Button(ventana, text="Reflejo", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*3+yPosicion)

    Button(ventana, text="Desplazamiento", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*4+yPosicion)

    Button(ventana, text="Diezmación/Interpolación", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*5+yPosicion)

    Button(ventana, text="Convolución", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*6+yPosicion)

    Button(ventana, text="FFT", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*7+yPosicion)

    ventana.mainloop()

def introducirValores():
    xPosicion = 100
    yPosicion = 100
    espacio = 65

    imagenFondo = PhotoImage(file="imgs/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    Button(ventana, text="↶", cursor="hand2",
           bd=10, background="#ff9aa2", height=0, command=verInicio,
           font=("Arial", 19)).place(x=5, y=5)


    Label(ventana, text="x(n){",
          font=("Arial", 25)).place(x=100, y=15)
    Entry(ventana,justify=RIGHT, textvariable=xL, width=10,
          font=("Arial", 25)).place(x=180, y=20)
    Entry(ventana, textvariable=xO, width=2,
          font=("Arial", 25)).place(x=380, y=20)
    Entry(ventana, textvariable=xR, width=10,
          font=("Arial", 25)).place(x=435, y=20)
    Label(ventana, text="}",
          font=("Arial", 25)).place(x=630, y=15)

    Label(ventana, text="h(n){",
          font=("Arial", 25)).place(x=100, y=75)
    Entry(ventana, justify=RIGHT, textvariable=hL, width=10,
          font=("Arial", 25)).place(x=180, y=80)
    Entry(ventana, textvariable=hO, width=2,
          font=("Arial", 25)).place(x=380, y=80)
    Entry(ventana, textvariable=hR, width=10,
          font=("Arial", 25)).place(x=435, y=80)
    Label(ventana, text="}",
          font=("Arial", 25)).place(x=630, y=75)

    Label(ventana, text="ORIGEN",
          font=("Arial", 10)).place(x=372, y=62)

    Button(ventana, text="Sumar", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio + yPosicion)

    Button(ventana, text="Restar", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=restar,
           font=("Arial", 16)).place(x=xPosicion + 97, y=espacio + yPosicion)

    Button(ventana, text="Amplificación", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio * 2 + yPosicion)

    Button(ventana, text="Atenuación", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion + 160, y=espacio * 2 + yPosicion)

    Button(ventana, text="Reflejo", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*3+yPosicion)

    Button(ventana, text="Desplazamiento", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*4+yPosicion)

    Button(ventana, text="Diezmación/Interpolación", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*5+yPosicion)

    Button(ventana, text="Convolución", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*6+yPosicion)

    Button(ventana, text="FFT", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*7+yPosicion)

    ventana.mainloop()

def sumar():
    global ejeV, newX, newH
    # Uso una imagen como fondo, debido a que es la
    # unica forma que encuentro para tapar la
    # ventana anterior, por lo que al crear un
    # nuevo escenario, siempre se tiene que poner esto
    imagenFondo = PhotoImage(file="imgs/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    #Con el boton regresa al inicio
    Button(ventana, text="↶", cursor="hand2",
           bd=10, background="#ff9aa2", height=0, command=verInicio,
           font=("Arial", 19)).place(x=5, y=5)
    emparejarValores()

    #Algoritmo exclusivo de esta operacion
    suma = []
    for i in range(len(newX)):
        suma.append(newX[i]+newH[i])

    #Se imprimen los arreglos emparejados
    #y el resultado
    resultadoX = "x(n){"
    for e in newX:
        if e != "":
            resultadoX = resultadoX + str(e) + ","
        else:
            resultadoX = resultadoX + str(e)
    resultadoX = resultadoX + "}"

    resultadoH = "h(n){"
    for e in newH:
        if e != "":
            resultadoH = resultadoH + str(e) + ","
        else:
            resultadoH = resultadoH + str(e)
    resultadoH = resultadoH + "}"

    resultadoSuma = "g(n){"
    for e in suma:
        if e != "":
            resultadoSuma = resultadoSuma+str(e)+","
        else:
            resultadoSuma = resultadoSuma + str(e)
    resultadoSuma = resultadoSuma+"}"

    #Titulo de la operacion
    Label(ventana, text="SUMA",
          font=("Arial", 45)).place(x=270, y=50)

    Label(ventana, text=resultadoX,
          font=("Arial", 25)).place(x=50, y=150)

    Label(ventana, text=resultadoH,
          font=("Arial", 25)).place(x=50, y=220)

    Label(ventana, text=resultadoSuma,
          font=("Arial", 25)).place(x=50, y=290)

    #Graficar, para ello los 5 arreglos deben
    #de tener la misma cantidad de elementos
    graficar(ejeV,newX,newH,suma,"Suma")
    ventana.mainloop()

def restar():
    global ejeV, newX, newH
    # Uso una imagen como fondo, debido a que es la
    # unica forma que encuentro para tapar la
    # ventana anterior, por lo que al crear un
    # nuevo escenario, siempre se tiene que poner esto
    imagenFondo = PhotoImage(file="imgs/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    # Con el boton regresa al inicio
    Button(ventana, text="↶", cursor="hand2",
           bd=10, background="#ff9aa2", height=0, command=verInicio,
           font=("Arial", 19)).place(x=5, y=5)
    emparejarValores()

    # Algoritmo exclusivo de esta operacion
    resta = []
    for i in range(len(newX)):
        resta.append(newX[i] - newH[i])

    # Se imprimen los arreglos emparejados
    # y el resultado
    resultadoX = "x(n){"
    for e in newX:
        if e != "":
            resultadoX = resultadoX + str(e) + ","
        else:
            resultadoX = resultadoX + str(e)
    resultadoX = resultadoX + "}"

    resultadoH = "h(n){"
    for e in newH:
        if e != "":
            resultadoH = resultadoH + str(e) + ","
        else:
            resultadoH = resultadoH + str(e)
    resultadoH = resultadoH + "}"

    resultado = "g(n){"
    for e in resta:
        if e != "":
            resultado = resultado + str(e) + ","
        else:
            resultado = resultado + str(e)
    resultado = resultado + "}"

    # Titulo de la operacion
    Label(ventana, text="Resta",
          font=("Arial", 45)).place(x=270, y=50)

    Label(ventana, text=resultadoX,
          font=("Arial", 25)).place(x=50, y=150)

    Label(ventana, text=resultadoH,
          font=("Arial", 25)).place(x=50, y=220)

    Label(ventana, text=resultado,
          font=("Arial", 25)).place(x=50, y=290)

    # Graficar, para ello los 5 arreglos deben
    # de tener la misma cantidad de elementos
    graficar(ejeV, newX, newH, resta,"Resta")
    ventana.mainloop()

def emparejarValores():
    global ejeV,newX,newH
    #la funcion split sirve para separar
    #la cadena cada vez que hay un
    #determinado caracter, aqui en es las ","
    hLAux = hL.get().split(",")
    xLAux = xL.get().split(",")
    hRAux = hR.get().split(",")
    xRAux = xR.get().split(",")


    if len(hLAux)>len(xLAux):
        for i in range(len(hLAux)-len(xLAux)):
            newX.append(float(0))
    if len(xLAux)>len(hLAux):
        for i in range(len(xLAux)-len(hLAux)):
            newH.append(float(0))

    for elemento in xLAux:
        if elemento != "":
            newX.append(float(elemento))
        else:
            newX.append(float(0))
    newX.append(float(xO.get()))
    for elemento in hLAux:
        if elemento != "":
            newH.append(float(elemento))
        else:
            newH.append(float(0))
    newH.append(float(hO.get()))
    print(len(newH))

    #Para guardar el origen se cuenta desde
    #el, y de cuentan la cantidad de elementos
    #a la izquierda etiquetandolos como se
    #encontrarian en la grafica
    for i in range(len(newH)):
        ejeV.append(i*(-1))

    #el arreglo se invierte debido a que en el
    #arreglo tenemos 0,-1,-2 por ejemplo, y se
    #debe de invertir para que quede como en una
    #grafica normal
    ejeV.reverse()

    for elemento in xRAux:
        if elemento != "":
            newX.append(float(elemento))
        else:
            newX.append(float(0))
    for elemento in hRAux:
        if elemento != "":
            newH.append(float(elemento))
        else:
            newH.append(float(0))

    if len(hRAux) > len(xRAux):
        for i in range(len(hRAux) - len(xRAux)):
            newX.append(float(0))
    if len(xRAux) > len(hRAux):
        for i in range(len(xRAux) - len(hRAux)):
            newH.append(float(0))
    for i in range(len(newH)-len(ejeV)):
        ejeV.append(i+1)

def graficar(ejeV,newX,newH, resultado,operacion):
    #ejeV se refiere al eje vertical
    #Los 4 arreglos deben de tener la misma cantida
    #de elementos

    #x(n) en la primera posicion
    plt.subplot(311)
    markerline, stemlines, baseline = plt.stem(ejeV, newX, '-.')
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.ylabel('x(n)')

    #h(n) en la segunda posicion
    plt.subplot(312)
    markerline, stemlines, baseline = plt.stem(ejeV, newH, '-.')
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.ylabel('h(n)')

    #g(n) en la tercer posicion
    plt.subplot(313)
    markerline, stemlines, baseline = plt.stem(ejeV, resultado, '-.')

    # setting property of baseline with color red and linewidth 2
    plt.suptitle(operacion+' x(n) con h(n)')

    plt.setp(baseline)
    plt.ylabel('g(n)')

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.show()

crearVentana()
verInicio()