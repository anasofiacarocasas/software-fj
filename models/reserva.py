from exceptions.custom_exceptions import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.duracion <= 0:
            raise ReservaError("La duración debe ser mayor que cero")

        self.estado = "Confirmada"

    def cancelar(self):

        self.estado = "Cancelada"

    def procesar(self):

        try:

            self.confirmar()

        except Exception as e:

            raise ReservaError(
                "Error procesando la reserva"
            ) from e

        else:

            return "Reserva realizada correctamente"

        finally:

            print("Proceso de reserva finalizado")