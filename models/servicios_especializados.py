from models.servicio import Servicio


# Servicio 1
class Sala(Servicio):

    def __init__(self, horas):
        super().__init__("Reserva de Sala")
        self.horas = horas

    def calcular_costo(self, impuesto=0):

        costo_base = self.horas * 50

        return costo_base + (costo_base * impuesto)

    def descripcion(self):

        return f"Reserva de sala por {self.horas} horas"


# Servicio 2
class Equipo(Servicio):

    def __init__(self, dias):
        super().__init__("Alquiler de Equipos")
        self.dias = dias

    def calcular_costo(self, descuento=0):

        costo_base = self.dias * 100

        return costo_base - descuento

    def descripcion(self):

        return f"Alquiler de equipo por {self.dias} días"


# Servicio 3
class Asesoria(Servicio):

    def __init__(self, sesiones):
        super().__init__("Asesoría Especializada")
        self.sesiones = sesiones

    def calcular_costo(self):

        return self.sesiones * 200

    def descripcion(self):

        return f"Asesoría de {self.sesiones} sesiones"