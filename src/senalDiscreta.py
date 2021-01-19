class SenalDiscreta:

    # Constructor
    # Si no se envian argumentos, se asignan los valores por defecto
    # Solo un dato = 0, indice de inicio = 0, tipo de senial = finita = no periodica
    def __init__(self, datos = [0], indice_inicio = 0, periodica = False):
        self.datos = datos
        self.indice_inicio = indice_inicio
        self.periodica = periodica # Si es periodica -> True.   Si es finita -> False

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

    def __str__(self):
        return str(self.datos) + " inicio: " + str(self.indice_inicio) + " periodica: " + str(self.periodica)
