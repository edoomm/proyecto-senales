from tkinter import *

ventana = Tk()
x = StringVar() # Este será el primer arreglo
h = StringVar() # Este será el primer arreglo
y = StringVar() # Este será el primer arreglo

def crearVentana():

    """ Crea la GUI junto con el establecimiento de sus propiedades """

    ventana.geometry("850x600+300+60")
    ventana.title("Prueba")
    ventana.resizable(width=False, height=False)

def principal():

    """ Función principal que contiene el `mainloop` de nuestra GUI y a su vez las declaraciones de los diferentes componentes de la GUI """

    # Entrada x(n)
    Entry(ventana, textvariable=x,width=15, font=("Arial", 12)).place(x=120, y=50)
    # Entrada h(n)
    Entry(ventana, textvariable=h,width=15, font=("Arial", 12)).place(x=120, y=100)
    # Salida y(n)
    Entry(ventana, textvariable=y,width=20, font=("Arial", 12)).place(x=120, y=170)
    # Boton que realiza la suma
    Button(ventana, text=" Suma",cursor="hand2", command=sumar,
                      font=("Arial", 14)).place(x=350, y=50)

    ventana.mainloop()


def sumar():
    """
    Función que realizará la suma y la obtendrá del archivo sumaresta.py
    """
    print("a")

crearVentana()
principal()