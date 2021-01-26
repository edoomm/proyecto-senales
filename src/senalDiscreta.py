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
            self.periodo = datos.copy()
            self.indice_inicio_periodo = indice_inicio

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

    def asignar_indice_inicio (self, indice):
        self.indice_inicio = indice

    def obtener_origen (self):
        return self.indice_inicio * -1

    # Se ajustan los tamanios de las seniales para que las dos tengan el mismo
    # tamanio y el mismo origen. Se modifican la señal local como la que se manda
    # por parametro
    def empatar (self, senial_discreta ):
        origen_1, origen_2 = self.obtener_origen(), senial_discreta.obtener_origen()
        longitud_1, longuitud_2 = self.obtener_longitud(), senial_discreta.obtener_longitud()

        distancia_origen_fin_1 = longitud_1 - origen_1 - 1
        distancia_origen_fin_2 = longuitud_2 - origen_2 - 1

        diferencia_izquierda = abs(origen_1 - origen_2)
        diferencia_derecha = abs( (longitud_1 - origen_1) - (longuitud_2 - origen_2) )

        if origen_1 < origen_2:
            self.expandir_izquierda(diferencia_izquierda)
        else:
            #auxiliar = senial_discreta.obtener_datos()
            #auxiliar = lista_izquierda + auxiliar
            #senial_discreta.asignar_datos(auxiliar)
            senial_discreta.expandir_izquierda(diferencia_izquierda)

        if distancia_origen_fin_1 < distancia_origen_fin_2:
            self.expandir_derecha(diferencia_derecha)
        else:
            senial_discreta.expandir_derecha(diferencia_derecha)

    # Expande la senial hacia la izquierda. Se inserta la cantidad de "longitud" elementos
    # a la izquierda. Si es periodica, se expande según el periodo, y si es finita se
    # insertan 0s
    # [1,.2,3]
    # [2,3,1,.2,3,1] -> [1,2,3,1,.2,3,1,2,3]
    def expandir_izquierda(self, longitud):
        auxiliar = [0] * longitud
        if self.periodica:
            i = self.obtener_origen()
            j = self.indice_inicio_periodo * -1
            for k in range(self.obtener_origen(), 0, -1):
                i -= 1
                j -= 1
            j -= 1
            for k in range(longitud):
                valor = self.periodo[(j - k) % len(self.periodo)]
                self.datos.insert(0, valor)
        else:
            self.datos = auxiliar + self.datos
        self.indice_inicio -= longitud

    # Expande la senial hacia la derecha. Se inserta la cantidad de "longitud" elementos
    # a la derecha. Si es periodica, se expande según el periodo, y si es finita se
    # insertan 0s
    def expandir_derecha (self, longitud):
        auxiliar = [0] * longitud
        if self.periodica:
            auxiliar = []
            desfase = len(self.datos) - self.obtener_origen() - 1
            indice = desfase + abs(self.indice_inicio_periodo) + 1
            N = len(self.periodo)
            for i in range(longitud):
                auxiliar.append(self.periodo[(indice + i) % N])
            self.datos = self.datos + auxiliar
        else:
            self.datos = self.datos + auxiliar

    # Expande hacia la izquierda el numero de periodos indicados
    # Si el periodo es N, la longitud de la senial despues de expandirla será
    # len(senial) + N.
    # Recibe el núero de periodos a expandir
    def expandir_periodo_izquierda (self, periodos):
        n = len(self.periodo)
        self.expandir_izquierda(n)

    # Expande hacia la derecha el numero de periodos indicados
    # Si el periodo es N, la longitud de la senial despues de expandirla será
    # senial.size() + N.
    # Recibe el núero de periodos a expandir
    def expandir_periodo_derecha (self, periodos):
        n = len(self.periodo)
        self.expandir_derecha(n)

    def __str__(self):
        return str(self.datos) + " inicio: " + str(self.indice_inicio) + " periodica: " + str(self.periodica)

y = SenalDiscreta([1,2,3],0, True)
print(y)
y.expandir_izquierda(1)
print(y)
y.expandir_izquierda(1)
print(y)
y.expandir_izquierda(1)
print(y)