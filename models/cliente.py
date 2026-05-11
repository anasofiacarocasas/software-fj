from models.entidad import Entidad
from exceptions.custom_exceptions import ClienteError


class Cliente(Entidad):

    def __init__(self, nombre, correo):

        self.__nombre = nombre
        self.__correo = correo

        self.validar()

    def validar(self):

        if len(self.__nombre) < 3:
            raise ClienteError("Nombre demasiado corto")

        if "@" not in self.__correo:
            raise ClienteError("Correo inválido")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__correo}"