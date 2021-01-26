class SenalDiscreta:

    # Constructor
    # Si no se envian argumentos, se asignan los valores por defecto:
    #   (Solo un dato = 0, indice de inicio = 0, tipo de senial = finita = no periodica)
    def __init__(self, datos=[0], indice_inicio=0, periodica=False):
        self.datos = datos
        self.indice_inicio = indice_inicio
        self.periodica = periodica  # Si es periodica -> True.   Si es finita -> False
        # Si es periodica, guardamos el periodo inicial
        if periodica:
            # Lista de datos de un periodo de la senial periodica
            self.periodo = datos.copy()

    def es_periodica(self) -> bool:
        if (self.periodica):
            return True
        else:
            return False

    def es_finita(self) -> bool:
        if (self.periodica):
            return False
        else:
            return True

    def obtener_longitud(self) -> int:
        return len(self.datos)

    def obtener_datos(self):
        return self.datos

    def asignar_datos(self, datos):
        self.datos = datos

    def obtener_indice_inicio(self) -> int:
        return self.indice_inicio

    def obtener_origen(self):
        return self.indice_inicio * -1

    def asignar_indice_inicio(self, indice_inicio):
        self.indice_inicio = indice_inicio

    # Se ajustan los tamanios de las seniales para que las dos tengan el mismo
    # tamanio y el mismo origen. Se modifican la señal local como la que se manda
    # por parametro
    def empatar(self, senial_discreta):
        origen_1, origen_2 = self.obtener_origen(), senial_discreta.obtener_origen()
        longitud_1, longuitud_2 = self.obtener_longitud(), senial_discreta.obtener_longitud()

        distancia_origen_fin_1 = longitud_1 - origen_1 - 1
        distancia_origen_fin_2 = longuitud_2 - origen_2 - 1

        diferencia_izquierda = abs(origen_1 - origen_2)
        diferencia_derecha = abs((longitud_1 - origen_1) - (longuitud_2 - origen_2))

        if origen_1 < origen_2:
            self.expandir_izquierda(diferencia_izquierda)
        else:
            # auxiliar = senial_discreta.obtener_datos()
            # auxiliar = lista_izquierda + auxiliar
            # senial_discreta.asignar_datos(auxiliar)
            senial_discreta.expandir_izquierda(diferencia_izquierda)

        if distancia_origen_fin_1 < distancia_origen_fin_2:
            self.expandir_derecha(diferencia_derecha)
        else:
            senial_discreta.expandir_derecha(diferencia_derecha)

    # Expande la senial hacia la izquierda. Se inserta la cantidad de "longitud" elementos
    # a la izquierda. Si es periodica, se expande según el periodo, y si es finita se
    # insertan 0s
    def expandir_izquierda(self, longitud):
        auxiliar = [0] * longitud
        if self.periodica:
            indice = self.indice_inicio - 1
            N = len(self.periodo)  # Periodo de la senial periodica
            for i in range(longitud):
                dato_a_insertar = self.periodo[(indice - i) % N]
                self.datos.insert(0, dato_a_insertar)
        else:
            self.datos = auxiliar + self.datos
        self.indice_inicio -= longitud

    # Expande la senial hacia la derecha. Se inserta la cantidad de "longitud" elementos
    # a la derecha. Si es periodica, se expande según el periodo, y si es finita se
    # insertan 0s
    def expandir_derecha(self, longitud):
        auxiliar = [0] * longitud
        if self.periodica:
            indice_inicio = len(self.datos) % len(self.periodo)
            auxiliar = self.periodo
            for i in range(longitud):
                self.datos.append(auxiliar[(i + indice_inicio) % len(auxiliar)])
        else:
            self.datos = self.datos + auxiliar

    # Expande hacia la izquierda el numero de periodos indicados
    # Si el periodo es N, la longitud de la senial despues de expandirla será
    # len(senial) + N.
    # Recibe el núero de periodos a expandir
    class SenalDiscreta:

        # Constructor
        # Si no se envian argumentos, se asignan los valores por defecto:
        #   (Solo un dato = 0, indice de inicio = 0, tipo de senial = finita = no periodica)
        def __init__(self, datos=[0], indice_inicio=0, periodica=False):
            self.datos = datos
            self.indice_inicio = indice_inicio
            self.periodica = periodica  # Si es periodica -> True.   Si es finita -> False
            # Si es periodica, guardamos el periodo inicial
            if periodica:
                # Lista de datos de un periodo de la senial periodica
                self.periodo = datos.copy()

        def es_periodica(self) -> bool:
            if (self.periodica):
                return True
            else:
                return False

        def es_finita(self) -> bool:
            if (self.periodica):
                return False
            else:
                return True

        def obtener_longitud(self) -> int:
            return len(self.datos)

        def obtener_datos(self):
            return self.datos

        def asignar_datos(self, datos):
            self.datos = datos

        def obtener_indice_inicio(self) -> int:
            return self.indice_inicio

        def obtener_origen(self):
            return self.indice_inicio * -1

        def asignar_indice_inicio(self, indice_inicio):
            self.indice_inicio = indice_inicio

        # Se ajustan los tamanios de las seniales para que las dos tengan el mismo
        # tamanio y el mismo origen. Se modifican la señal local como la que se manda
        # por parametro
        def empatar(self, senial_discreta):
            origen_1, origen_2 = self.obtener_origen(), senial_discreta.obtener_origen()
            longitud_1, longuitud_2 = self.obtener_longitud(), senial_discreta.obtener_longitud()

            distancia_origen_fin_1 = longitud_1 - origen_1 - 1
            distancia_origen_fin_2 = longuitud_2 - origen_2 - 1

            diferencia_izquierda = abs(origen_1 - origen_2)
            diferencia_derecha = abs((longitud_1 - origen_1) - (longuitud_2 - origen_2))

            if origen_1 < origen_2:
                self.expandir_izquierda(diferencia_izquierda)
            else:
                # auxiliar = senial_discreta.obtener_datos()
                # auxiliar = lista_izquierda + auxiliar
                # senial_discreta.asignar_datos(auxiliar)
                senial_discreta.expandir_izquierda(diferencia_izquierda)

            if distancia_origen_fin_1 < distancia_origen_fin_2:
                self.expandir_derecha(diferencia_derecha)
            else:
                senial_discreta.expandir_derecha(diferencia_derecha)

        # Expande la senial hacia la izquierda. Se inserta la cantidad de "longitud" elementos
        # a la izquierda. Si es periodica, se expande según el periodo, y si es finita se
        # insertan 0s
        def expandir_izquierda(self, longitud):
            auxiliar = [0] * longitud
            if self.periodica:
                indice = self.indice_inicio - 1
                N = len(self.periodo)  # Periodo de la senial periodica
                for i in range(longitud):
                    dato_a_insertar = self.periodo[(indice - i) % N]
                    self.datos.insert(0, dato_a_insertar)
            else:
                self.datos = auxiliar + self.datos
            self.indice_inicio -= longitud

        # Expande la senial hacia la derecha. Se inserta la cantidad de "longitud" elementos
        # a la derecha. Si es periodica, se expande según el periodo, y si es finita se
        # insertan 0s
        def expandir_derecha(self, longitud):
            auxiliar = [0] * longitud
            if self.periodica:
                indice_inicio = len(self.datos) % len(self.periodo)
                auxiliar = self.periodo
                for i in range(longitud):
                    self.datos.append(auxiliar[(i + indice_inicio) % len(auxiliar)])
            else:
                self.datos = self.datos + auxiliar

        # Expande hacia la izquierda el numero de periodos indicados
        # Si el periodo es N, la longitud de la senial despues de expandirla será
        # len(senial) + N.
        # Recibe el núero de periodos a expandir
        def expandir_periodo_izquierda(self, periodos):
            auxiliar = self.datos
            for i in range(periodos):
                auxiliar = self.periodo + auxiliar
            self.datos = auxiliar
            self.indice_inicio -= periodos * len(self.periodo)

        # Expande hacia la derecha el numero de periodos indicados
        # Si el periodo es N, la longitud de la senial despues de expandirla será
        # senial.size() + N.
        # Recibe el núero de periodos a expandir
        def expandir_periodo_derecha(self, periodos):
            auxiliar = self.datos
            for i in range(periodos):
                auxiliar = auxiliar + self.periodo
            self.datos = auxiliar

        def __str__(self):
            return str(self.datos) + " inicio: " + str(self.indice_inicio) + " periodica: " + str(self.periodica)

    # x = SenalDiscreta([1,2,3],-2,True)
    # y = SenalDiscreta([1,2,3,4],0,True)
    # print(y)
    # y.expandir_derecha(2)
    # print(y)
    # y.expandir_izquierda(2)
    # print(y)

    # Expande hacia la derecha el numero de periodos indicados
    # Si el periodo es N, la longitud de la senial despues de expandirla será
    # senial.size() + N.
    # Recibe el núero de periodos a expandir
    def expandir_periodo_derecha(self, periodos):
        auxiliar = self.datos
        for i in range(periodos):
            auxiliar = auxiliar + self.periodo
        self.datos = auxiliar

    def __str__(self):
        return str(self.datos) + " inicio: " + str(self.indice_inicio) + " periodica: " + str(self.periodica)


x = SenalDiscreta([1,2,3],-2,True)
y = SenalDiscreta([1,2,3,4],0,True)
print(y)
y.expandir_derecha(5)
print(y)
y.expandir_izquierda(7)
print(y)
