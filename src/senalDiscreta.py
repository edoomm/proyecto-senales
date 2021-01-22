class SenalDiscreta:

    # Constructor
    # Si no se envian argumentos, se asignan los valores por defecto:
    #   (Solo un dato = 0, indice de inicio = 0, tipo de senial = finita = no periodica)
    def __init__(self, datos = [0], indice_inicio = 0, periodica = False):
        self.datos = datos
        self.indice_inicio = indice_inicio
        self.periodica = periodica # Si es periodica -> True.   Si es finita -> False
        # Si es periodica, guardamos el periodo inicial
        if periodica:
            self.periodo = datos

    def es_periodica (self) -> bool:
        if ( self.periodica ):
            return True
        else:
            return False

    def es_finita (self) -> bool:
        if ( self.periodica ):
            return False
        else:
            return True

    def obtener_longitud (self) -> int:
        return len(self.datos)

    def obtener_datos (self):
        return self.datos

    def asignar_datos (self, datos):
        self.datos = datos

    def obtener_indice_inicio (self) -> int:
        return self.indice_inicio

    def obtener_origen (self):
        return self.indice_inicio * -1

    def asignar_indice_inicio (self, indice_inicio):
        self.indice_inicio = indice_inicio

    # Se expanden los datos dependiendo de la senial.
    # Si es finita, se agregan 0s para hacerla de tamanio n
    # Si es periodica, se repiten los valores para obtener una gráfica de tamanio n
    def empatar (self, senial_discreta ):
        origen_1, origen_2 = self.obtener_origen(), senial_discreta.obtener_origen()
        longitud_1, longuitud_2 = self.obtener_longitud(), senial_discreta.obtener_longitud()

        distancia_origen_fin_1 = longitud_1 - origen_1 - 1
        distancia_origen_fin_2 = longuitud_2 - origen_2 - 1

        diferencia_izquierda = abs(origen_1 - origen_2)
        diferencia_derecha = abs( (longitud_1 - origen_1) - (longuitud_2 - origen_2) )

        #lista_izquierda = [0] * diferencia_izquierda
        #lista_derecha = [0] * diferencia_derecha

        if origen_1 < origen_2:
            #auxiliar = self.obtener_datos()
            #auxiliar = lista_izquierda + auxiliar
            #self.asignar_datos(auxiliar)
            self.expandir_izquierda(diferencia_izquierda)
        else:
            #auxiliar = senial_discreta.obtener_datos()
            #auxiliar = lista_izquierda + auxiliar
            #senial_discreta.asignar_datos(auxiliar)
            senial_discreta.expandir_izquierda(diferencia_izquierda)

        if distancia_origen_fin_1 < distancia_origen_fin_2:
            #auxiliar = self.obtener_datos()
            #auxiliar = auxiliar + lista_derecha
            #self.asignar_datos(auxiliar)
            self.expandir_derecha(diferencia_derecha)
        else:
            #auxiliar = senial_discreta.obtener_datos()
            #auxiliar = auxiliar + lista_derecha
            #senial_discreta.asignar_datos(auxiliar)
            senial_discreta.expandir_derecha(diferencia_derecha)

    def expandir_izquierda (self, longitud):
        auxiliar = [0] * longitud
        origen = self.obtener_origen()
        if self.periodica:
            auxiliar = self.datos[0: origen] + self.datos[origen : len(self.datos)]
            auxiliar.reverse()
            for i in range(longitud):
                self.datos.insert(0, auxiliar[i % len(auxiliar)])
        else:
            self.datos = auxiliar + self.datos
        self.indice_inicio -= longitud

    def expandir_derecha (self, longitud):
        auxiliar = [0] * longitud
        origen = self.obtener_origen()
        if self.periodica:
            auxiliar = self.datos[0: origen] + self.datos[origen : len(self.datos)]
            for i in range(longitud):
                self.datos.append(auxiliar[i % len(auxiliar)])
        else:
            self.datos = self.datos + auxiliar

    def __str__(self):
        return str(self.datos) + " inicio: " + str(self.indice_inicio) + " periodica: " + str(self.periodica)