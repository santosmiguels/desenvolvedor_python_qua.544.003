class Motor:
    def __init__(self, potencia):
        self.__potencia = potencia

    @pro
    def potencia(self):
        return self.__potencia

    @property
    def potencia(self, potencia):
        self.__potencia = potencia

    def info(self):
        return f"Motor de {self.__potencia} CV."

class Carro:
    def __init__(self, modelo, potencia):
        self.__modelo = modelo
        self.__motor = Motor(potencia)

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def model(self, modelo):
        self.__modelo = modelo

    def detalhes(self):
        return f"Carro: {self.__modelo} | {self.__motor.info()}"