from tkinter import *
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np

# Archivos de uso común
from senalDiscreta import *

# Archivos que contienen las operaciones ----------------------------- AGREGAR AQUI SUS ARCHIVOS CORRESPONDIENTES A SUS OPERACIONES
from operacionSuma import *
from operacionResta import *
from operacionReflejo import *
from operacionConvolucion import *
from operacionAmplificacionAtenuacion import *
from operacionInterpolacionDiezmacion import *
from operacionDesplazamiento import *

ventana = Tk()

#Entradas de los cuadros de texto al meter una
#secuencia de datos
#L= Left (Izquierda), O= Origen , R = Right(Derecha)
xL = StringVar()
xO = StringVar()
xR = StringVar()

# Opciones
multiplicador = StringVar()
factorInterpolacionDiezmacion = StringVar()
udsDesplazamiento = IntVar()

hL = StringVar()
hO = StringVar()
hR = StringVar()

# Variables para las periocidades

xesperiodica = BooleanVar()
hesperiodica = BooleanVar()

# Varibles para operaciones particulares
opcionreflejo = IntVar() # Opción para decidir en que eje se reflejara

# Con el siguiente algoritmo lo que se hace
# es hacer tanto x(n) como h(n) tengan la
# misma cantidad de elementos en el arreglo
# en caso de que una tenga mas, se acompleta
# con 0's ya sea a la izquierda o derecha
# segun sea el caso
newH = [] # Lista para h(n) de longitud estandar
newX = [] # Lista para x(n) de longitud estandar
puntosEjeH = [] # Lista que contiene los puntos en donde se graficaran las listas en el eje horizontal

def crearVentana():

    ''' Crea la GUI junto con el establecimiento de sus propiedades '''

    global ventana
    #Dimenciones de la pantalla
    ventana.geometry("700x650+350+60")
    ventana.title("Proyecto de Señales")
    #Ajuste de la pantalla
    ventana.resizable(width=True, height=False)

def verInicio():

    '''
    Función para la GUI\n
    Muestra los primeros controles correspondientes a la desición del método de entrada de valores
    '''

    global puntosEjeH,newX,newH
    newH = []
    newX = []
    puntosEjeH = []
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

    ventana.mainloop()

def introducirValores():

    '''
    Función para la GUI\n
    Cambia la ventana al modo de introducir valores con las 3 entradas para x(n) y las otras 3 para h(n)
    '''

    xPosicion = 100
    yPosicion = 100
    espacio = 65

    imagenFondo = PhotoImage(file="imgs/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    Button(ventana, text="↶", cursor="hand2",
           bd=10, background="#ff9aa2", height=0, command=verInicio,
           font=("Arial", 15)).place(x=2, y=5)


    Label(ventana, text="x(n){",
          font=("Arial", 25)).place(x=50, y=15)
    Entry(ventana,justify=RIGHT, textvariable=xL, width=10,
          font=("Arial", 25)).place(x=130, y=20)
    Entry(ventana, textvariable=xO, width=2,
          font=("Arial", 25)).place(x=330, y=20)
    Entry(ventana, textvariable=xR, width=10,
          font=("Arial", 25)).place(x=385, y=20)
    Label(ventana, text="}",
          font=("Arial", 25)).place(x=580, y=15)

    Label(ventana, text="h(n){",
          font=("Arial", 25)).place(x=50, y=75)
    Entry(ventana, justify=RIGHT, textvariable=hL, width=10,
          font=("Arial", 25)).place(x=130, y=80)
    Entry(ventana, textvariable=hO, width=2,
          font=("Arial", 25)).place(x=330, y=80)
    Entry(ventana, textvariable=hR, width=10,
          font=("Arial", 25)).place(x=385, y=80)
    Label(ventana, text="}",
          font=("Arial", 25)).place(x=580, y=75)

    Label(ventana, text="ORIGEN",
          font=("Arial", 10)).place(x=322, y=62)

    Button(ventana, text="Sumar", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=sumar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio + yPosicion)

    Button(ventana, text="Restar", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=restar,
           font=("Arial", 16)).place(x=xPosicion + 97, y=espacio + yPosicion)

    Button(ventana, text="Amplificación / Atenuación", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=amplificarAtenuar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio * 2 + yPosicion)

    Entry(ventana,justify=CENTER, textvariable=multiplicador, width=4,
          font=("Arial", 16)).place(x=385, y=248)

    Label(ventana, text="Multiplicador",
          font=("Arial", 10)).place(x=380, y=225)

    Button(ventana, text="Reflejo en X y Y", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=reflejarEnXyY,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*3+yPosicion)

    Button(ventana, text="Desplazamiento", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=desplazar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*4+yPosicion)

    Entry(ventana,justify=CENTER, textvariable=udsDesplazamiento, width=4,
          font=("Arial", 16)).place(x=285, y=323+53)

    Label(ventana, text="Unidades a desplazar",
          font=("Arial", 10)).place(x=285+5, y=300+53)

    Entry(ventana,justify=CENTER, textvariable=factorInterpolacionDiezmacion, width=4,
          font=("Arial", 16)).place(x=405, y=448)

    Label(ventana, text="Factor de diezmación/interpolación",
          font=("Arial", 10)).place(x=400, y=425)

    Button(ventana, text="Diezmación", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=diezmar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*5+yPosicion)

    Button(ventana, text="Interpolación", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=interpolar,
           font=("Arial", 16)).place(x=xPosicion+145, y=espacio*5+yPosicion)

    Button(ventana, text="Convolución", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=convolusionar,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*6+yPosicion)

    Button(ventana, text="FFT", cursor="hand2",
           bd=8, background="#ffb3cc", height=1, command=fft,
           font=("Arial", 16)).place(x=xPosicion, y=espacio*7+yPosicion)

    Button(ventana, text="Pruebas", command=tests).place(x=xPosicion+15, y=espacio*8+yPosicion)

    #Checkboxes
    Checkbutton(ventana, text="Periodica", variable=xesperiodica).place(x=615, y=25)
    Checkbutton(ventana, text="Periodica", variable=hesperiodica).place(x=615, y=85)

    ventana.mainloop()

def tests():
    """
    Función para hacer pruebas solamente
    """
    print(udsDesplazamiento.get())

def emparejarPuntosEjeHConInicio(senal):
    """
    Empareja los puntos del eje H para graficar con los respectivos de la señal dada
    Parameters:
        senal (SenalDiscreta): La señal resultante de alguna operación de preferencia
    """
    global puntosEjeH

    puntosEjeH = []
    for i in range(senal.obtener_indice_inicio(), senal.obtener_longitud() + senal.obtener_indice_inicio()):
        puntosEjeH.append(i)

def configurarPantalla(operacion, resx, resh, resg):
    """
    Configura la pantalla dependiendo que operación se haga

    Parameters:
        operacion (str): El título de la operación realizada
        resx (str): La secuencia de la señal x(n) con formato {...,#,#,..}
        resh (str): La secuencia de la señal h(n) con formato {...,#,#,..}
        resg (str): La secuencia de la señal g(n) con formato {...,#,#,..}
    """
    # Uso una imagen como fondo, debido a que es la
    # unica forma que encuentro para tapar la
    # ventana anterior, por lo que al crear un
    # nuevo escenario, siempre se tiene que poner esto
    imagenFondo = PhotoImage(file="imgs/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    #Coloca el boton regresa al inicio
    Button(ventana, text="↶", cursor="hand2",
           bd=10, background="#ff9aa2", height=0, command=verInicio,
           font=("Arial", 19)).place(x=5, y=5)

    #Titulo de la operacion
    Label(ventana, text=operacion,
          font=("Arial", 45)).place(x=270, y=50)

    Label(ventana, text=resx,
          font=("Arial", 25)).place(x=50, y=150)

    Label(ventana, text=resh,
          font=("Arial", 25)).place(x=50, y=220)

    Label(ventana, text=resg,
          font=("Arial", 25)).place(x=50, y=290)

"""
Para las operaciones que solo tienen una secuencia de entrada
y una de salida
"""
def configurarPantallaDeUnSoloValor(operacion, xn, gn):
    """
    Configura la pantalla dependiendo que operación se haga

    Parameters:
        operacion (str): El título de la operación realizada
        resx (str): La secuencia de la señal x(n) con formato {...,#,#,..}
        resh (str): La secuencia de la señal h(n) con formato {...,#,#,..}
        resg (str): La secuencia de la señal g(n) con formato {...,#,#,..}
    """
    # Uso una imagen como fondo, debido a que es la
    # unica forma que encuentro para tapar la
    # ventana anterior, por lo que al crear un
    # nuevo escenario, siempre se tiene que poner esto
    imagenFondo = PhotoImage(file="imgs/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    #Coloca el boton regresa al inicio
    Button(ventana, text="↶", cursor="hand2",
           bd=10, background="#ff9aa2", height=0, command=verInicio,
           font=("Arial", 19)).place(x=5, y=5)



    #Se imprimen los arreglos emparejados
    #y el resultado
    resx = "x(n){"
    for e in xn:
        if e != "":
            resx = resx + str(e) + ","
        else:
            resx = resx + str(e)
    resx = resx + "}"

    resg = "g(n){"
    for e in gn:
        if e != "":
            resg = resg+str(e)+","
        else:
            resg = resg + str(e)
    resg = resg+"}"



    #Titulo de la operacion
    Label(ventana, text=operacion,
          font=("Arial", 45)).place(x=240, y=50)

    Label(ventana, text=resx,
          font=("Arial", 25)).place(x=50, y=150)

    Label(ventana, text=resg,
          font=("Arial", 25)).place(x=50, y=290)


def obtenerSecuencia(variable, senal):
    """
    Obtiene la secuencia de una señal dada

    Parameters:
        variable (str): La letra de la variable de la señal
        senal (SenialDiscreta): La señal discreta

    Returns:
        str: Secuencia de una señal en formato {...,#,...}
    """
    secuencia = variable + "(n) = ["
    for e in senal.obtener_datos():
        if e != "":
            secuencia = secuencia + str(e) + ","
        else:
            secuencia = secuencia + str(e)
    secuencia = secuencia + "]"

    return secuencia

# Esta función será el modelo a seguir para las demas operaciones
def sumar():
    """
    Comando asociado al botón "Sumar"
    """
    # Obtiene datos de GUI
    senales = emparejarValores()
    xn = senales[0]
    hn = senales[1]
    # Se realiza la operación
    gn = obtenerSuma(xn, hn) # ------------------LINEA A CAMBIAR

    operacion = "Suma" # ------------------------LINEA A CAMBIAR
    # Se configura la GUI
    configurarPantalla(operacion, obtenerSecuencia("x", xn), obtenerSecuencia("h", hn), obtenerSecuencia("g", gn))
    # Grafica
    graficar(puntosEjeH, xn.obtener_datos(), hn.obtener_datos(), gn.obtener_datos(), operacion)

    ventana.mainloop()

def restar():
    """
    Comando asociado al botón restar
    """
    # Obtiene datos de GUI
    senales = emparejarValores()
    xn = senales[0]
    hn = senales[1]
    # Se realiza la operación
    gn = obtenerResta(xn, hn) # ------------------LINEA A CAMBIAR

    operacion = "Restar" # -----------------------LINEA A CAMBIAR
    # Se configura la GUI
    configurarPantalla(operacion, obtenerSecuencia("x", xn), obtenerSecuencia("h", hn), obtenerSecuencia("g", gn))
    # Grafica
    graficar(puntosEjeH, xn.obtener_datos(), hn.obtener_datos(), gn.obtener_datos(), operacion)

    ventana.mainloop()

def amplificarAtenuar():
    global newX
    concatenarSecuenciaX()
    # Se realiza la operación
    gn = obtenerAmplificacionAtenuacion(newX, float(multiplicador.get())) # ------------------LINEA A CAMBIAR

    if float(multiplicador.get())>1:
        operacion = "Amplificacion"
    else:
        operacion = "Atenuacion" # ------------------------LINEA A CAMBIAR
    # Se configura la GUI
    configurarPantallaDeUnSoloValor(operacion, newX, gn)
    # Grafica
    graficarSolo2(puntosEjeH, newX, gn, operacion)
    ventana.mainloop()

"""
Hice otra función para reflejar al mismo tiempo en X e Y, .
"""
def reflejarEnXyY():
    """
    Comando asociado al botón "reflejar"
    """
    # Obtiene datos de GUI
    senal = concatenarSecuenciaX()
    xn = senal[0]


    # Se realiza la operación
    gnY = obtener_reflejoY(xn)
    gnY = obtener_reflejoY(xn)
    #gnY = obtener_reflejoY(xn)

    datosAux = xn.obtener_datos()
    for i in range(len(datosAux)):
        datosAux[i] = datosAux[i] * -1

    gnX = SenalDiscreta(datosAux, xn.obtener_indice_inicio(), xn.es_periodica())


    operacion = "Reflejar" # ------------------------LINEA A CAMBIAR
    # Se configura la GUI
    configurarPantalla(operacion, obtenerSecuencia("x", xn), obtenerSecuencia("x", gnX), obtenerSecuencia("x", gnY))
    # Grafica
    graficarReflejo(puntosEjeH, gnX.obtener_datos(), gnY.obtener_datos(), operacion)

    ventana.mainloop()

def desplazar():
    """
    Comando asociado al botón "Desplazar"
    """
    # Obtiene datos de GUI
    senales = concatenarSecuenciaX()
    xn = senales[0]
    td = udsDesplazamiento.get()
    # Se realiza la operación
    gn1 = obtener_Desplazamiento(xn, 1, td) # Desplazamiento a la derecha
    gn2 = obtener_Desplazamiento(xn, 2, td) # Desplazamiento a la izquierda

    operacion = "Desplazamiento" # ------------------------LINEA A CAMBIAR
    # Se configura la GUI
    configurarPantalla(operacion, obtenerSecuencia("x", xn), obtenerSecuencia("gn1", gn1), obtenerSecuencia("gn2", gn2))
    # Grafica
    graficar(puntosEjeH, xn.obtener_datos(), gn1.obtener_datos(), gn2.obtener_datos(), operacion)

    ventana.mainloop()

def diezmar():
    """
    Comando asociado al botón "Diezmación"
    """
    # Obtiene datos de GUI
    senales = concatenarSecuenciaX()
    xn = senales[0]
    operacion = "Diezmación"
    if(xn.obtener_indice_inicio() > 0):
        xn.asignar_indice_inicio(-xn.obtener_indice_inicio())
    # Se realiza la operación
    gn = obtenerDiezmacion(xn, int(factorInterpolacionDiezmacion.get()))
    # Se configura la GUI
    configurarPantallaDeUnSoloValor(operacion, xn.obtener_datos(), gn.obtener_datos())
    # Grafica
    gn.empatar(xn)
    graficarSolo2(range(gn.obtener_longitud()), xn.obtener_datos(), gn.obtener_datos(), operacion)
    ventana.mainloop()

def interpolar():
    """
    Comando asociado al botón "Interpolar"
    """
    #Obtiene datos de la GUI
    seniales = concatenarSecuenciaX()
    xn = seniales[0]
    operacion = "Interpolación"
    if(xn.obtener_indice_inicio() > 0):
        xn.asignar_indice_inicio(-xn.obtener_indice_inicio())
    # Se realiza la operación
    gn = obtenerInterpolacion(xn, int(factorInterpolacionDiezmacion.get()))
    # Se configura la GUI
    configurarPantallaDeUnSoloValor(operacion, xn.obtener_datos(), gn.obtener_datos())
    # Grafica
    gn.empatar(xn)
    graficarSolo2(range(gn.obtener_longitud()), xn.obtener_datos(), gn.obtener_datos(), operacion)
    ventana.mainloop()

# La falta de ortografia es adrede, porque ya existe la función sin falta de ortografia jaja
def convolusionar():
    """
    Comando asociado al botón "Convolución"
    """
    # Obtiene datos de GUI
    senales = emparejarValores()
    xn = senales[0]
    hn = senales[1]
    # Se realiza la operación
    gn = convolucionar(xn, hn) # ------------------LINEA A CAMBIAR

    # Se realiza emparejamiento
    xn.empatar(gn)
    hn.empatar(gn)
    emparejarPuntosEjeHConInicio(gn)

    operacion = "Convolución" # ------------------------LINEA A CAMBIAR
    # Se configura la GUI
    configurarPantalla(operacion, obtenerSecuencia("x", xn), obtenerSecuencia("h", hn), obtenerSecuencia("g", gn))
    # Grafica
    graficar(puntosEjeH, xn.obtener_datos(), hn.obtener_datos(), gn.obtener_datos(), operacion)

    ventana.mainloop()

def fft():
    """
    Comando asociado al botón "FFT"
    """
    # Obtiene datos de GUI
    senales = emparejarValores()
    xn = senales[0]
    hn = senales[1]
    # Se realiza la operación
    gn = obtenerSuma(xn, hn) # ------------------LINEA A CAMBIAR

    operacion = "Suma" # ------------------------LINEA A CAMBIAR
    # Se configura la GUI
    configurarPantalla(operacion, obtenerSecuencia("x", xn), obtenerSecuencia("h", hn), obtenerSecuencia("g", gn))
    # Grafica
    graficar(puntosEjeH, xn.obtener_datos(), hn.obtener_datos(), gn.obtener_datos(), operacion)

    ventana.mainloop()

# TODO: Validar valores de las entradas
def emparejarValores():
    
    '''Hace las listas correspondientes a x(n) y h(n) del mismo tamaño y las asigna newX y newH así como prepara los puntos en el eje horizontal de las gráficas para su posterior ploteo

    Returns:
        SenialDiscreta:Devuelve una tupla con objetos de SenialDiscreta que representan a x(n) (posición: 0) y h(n) (posición: 1)

    '''

    global puntosEjeH,newX,newH
    #la funcion split sirve para separar
    #la cadena cada vez que hay un
    #determinado caracter, aqui en es las ","
    hLAux = hL.get().split(",")
    xLAux = xL.get().split(",")
    hRAux = hR.get().split(",")
    xRAux = xR.get().split(",")

    # Se resetea newX, newH y puntosEjeH
    newX = []
    newH = []
    puntosEjeH = []

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

    #Para guardar el origen se cuenta desde
    #el, y de cuentan la cantidad de elementos
    #a la izquierda etiquetandolos como se
    #encontrarian en la grafica
    for i in range(len(newH)):
        puntosEjeH.append(i*(-1))

    #el arreglo se invierte debido a que en el
    #arreglo tenemos 0,-1,-2 por ejemplo, y se
    #debe de invertir para que quede como en una
    #grafica normal
    puntosEjeH.reverse()

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
    for i in range(len(newH)-len(puntosEjeH)):
        puntosEjeH.append(i+1)

    # Cálculo del indice de inicio de las listas
    iinicio = 0
    if len(xLAux) != 0 and len(hLAux) != 0:
        if len(xLAux) > len (hLAux):
            iinicio = -len(xLAux)
        else:
            iinicio = -len(hLAux) 

    xn = SenalDiscreta(newX, iinicio, xesperiodica.get())
    hn = SenalDiscreta(newH, iinicio, hesperiodica.get())
    return [xn, hn]


"""
Para las operaciones que solo requieran una secuencia de
entrada, entonces se utiliza esta funcion, ya que esta
no necesita ser acompletada con 0´s
"""
def concatenarSecuenciaX():
    
    '''Hace las listas correspondientes a x(n) y h(n) del mismo tamaño y las asigna newX y newH así como prepara los puntos en el eje horizontal de las gráficas para su posterior ploteo

    Returns:
        SenialDiscreta:Devuelve una tupla con objetos de SenialDiscreta que representan a x(n) (posición: 0) y h(n) (posición: 1)

    '''

    global puntosEjeH,newX
    #la funcion split sirve para separar
    #la cadena cada vez que hay un
    #determinado caracter, aqui en es las ","
    xLAux = xL.get().split(",")
    xRAux = xR.get().split(",")

    # Se resetea newX, newH y puntosEjeH
    newX = []
    puntosEjeH = []

    for elemento in xLAux:
        if elemento != "":
            newX.append(float(elemento))
        else:
            newX.append(float(0))
    newX.append(float(xO.get()))
    #Para guardar el origen se cuenta desde
    #el, y se cuentan la cantidad de elementos
    #a la izquierda etiquetandolos como se
    #encontrarian en la grafica
    for i in range(len(newX)):
        puntosEjeH.append(i*(-1))

    #el arreglo se invierte debido a que en el
    #arreglo tenemos 0,-1,-2 por ejemplo, y se
    #debe de invertir para que quede como en una
    #grafica normal
    puntosEjeH.reverse()

    for elemento in xRAux:
        if elemento != "":
            newX.append(float(elemento))
        else:
            newX.append(float(0))


    for i in range(len(newX)-len(puntosEjeH)):
        puntosEjeH.append(i+1)

    xn = SenalDiscreta(newX, len(xLAux), xesperiodica.get())

    return [xn]

def graficar(puntosEjeH,newX,newH, resultado,operacion):
    #puntosEjeH se refiere al eje vertical
    #Los 4 arreglos deben de tener la misma cantida
    #de elementos

    #x(n) en la primera posicion
    plt.subplot(311)
    markerline, stemlines, baseline = plt.stem(puntosEjeH, newX, '-.')
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.ylabel('x(n)')

    #h(n) en la segunda posicion
    plt.subplot(312)
    markerline, stemlines, baseline = plt.stem(puntosEjeH, newH, '-.')
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.ylabel('h(n)')

    #g(n) en la tercer posicion
    plt.subplot(313)
    markerline, stemlines, baseline = plt.stem(puntosEjeH, resultado, '-.')

    # setting property of baseline with color red and linewidth 2
    plt.suptitle(operacion+' x(n) con h(n)')

    plt.setp(baseline)
    plt.ylabel('g(n)')

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.show()

"""
Necesitaba una grafica personalizada para el reflejo,
probablemente se puede reutilizar codigo, pero por
cuestiones practicas no lo hice
"""
def graficarReflejo(puntosEjeH,ejeX,ejeY,operacion):
    #puntosEjeH se refiere al eje vertical
    #Los 4 arreglos deben de tener la misma cantida
    #de elementos


    #h(n) en la segunda posicion
    plt.subplot(311)
    markerline, stemlines, baseline = plt.stem(puntosEjeH, ejeX, '-.')
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.ylabel('En X')

    #g(n) en la tercer posicion
    plt.subplot(313)
    markerline, stemlines, baseline = plt.stem(puntosEjeH, ejeY, '-.')

    # setting property of baseline with color red and linewidth 2
    plt.suptitle(operacion+' x(n) en el eje X y Y')

    plt.setp(baseline)
    plt.ylabel('En Y')

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.show()

#Aqui se grafican solo 2 graficas
def graficarSolo2(puntosEjeH,newX,resultado,operacion):
    #puntosEjeH se refiere al eje vertical
    #Los 4 arreglos deben de tener la misma cantida
    #de elementos

    #x(n) en la primera posicion
    plt.subplot(311)
    markerline, stemlines, baseline = plt.stem(puntosEjeH, newX, '-.')
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.ylabel('x(n)')

    #g(n) en la tercer posicion
    plt.subplot(313)
    markerline, stemlines, baseline = plt.stem(puntosEjeH, resultado, '-.')

    # setting property of baseline with color red and linewidth 2
    plt.suptitle(operacion+' x(n) con algo')

    plt.setp(baseline)
    plt.ylabel('g(n)')

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    plt.show()

crearVentana()
verInicio()
