from models.cliente import Cliente
from models.servicios_especializados import Sala, Equipo, Asesoria
from models.reserva import Reserva

from utils.logger import logger


def ejecutar_operacion(numero, descripcion, funcion):

    print(f"\nOPERACION {numero}: {descripcion}")

    try:

        resultado = funcion()

    except Exception as e:

        print(f"ERROR: {e}")

        logger.error(
            f"Operacion {numero} fallo: {e}"
        )

    else:

        if resultado is not None:
            print(resultado)

        logger.info(
            f"Operacion {numero} exitosa"
        )

    finally:

        print("Operacion finalizada")


def main():

    print("\n===== SISTEMA SOFTWARE FJ =====")

    datos = {}

    # 1 Cliente válido
    ejecutar_operacion(
        1,
        "Registro de cliente valido",
        lambda: datos.update({
            "cliente1": Cliente(
                "Yohan",
                "yohan@gmail.com"
            )
        })
    )


    # 2 Cliente inválido
    ejecutar_operacion(
        2,
        "Registro de cliente invalido",
        lambda: Cliente(
            "A",
            "correo_invalido"
        )
    )


    # 3 Servicio válido
    ejecutar_operacion(
        3,
        "Creacion de servicio sala",
        lambda: datos.update({
            "sala": Sala(4)
        })
    )


    # 4 Servicio válido
    ejecutar_operacion(
        4,
        "Creacion de servicio equipo",
        lambda: datos.update({
            "equipo": Equipo(3)
        })
    )


    # 5 Servicio válido
    ejecutar_operacion(
        5,
        "Creacion de servicio asesoria",
        lambda: datos.update({
            "asesoria": Asesoria(2)
        })
    )


    # 6 Servicio incorrecto
    ejecutar_operacion(
        6,
        "Creacion incorrecta de servicio",
        lambda: Sala(-5)
    )


    # 7 Reserva exitosa
    ejecutar_operacion(
        7,
        "Reserva exitosa",
        lambda: Reserva(
            datos["cliente1"],
            datos["sala"],
            4
        ).procesar()
    )


    # 8 Reserva fallida
    ejecutar_operacion(
        8,
        "Reserva fallida",
        lambda: Reserva(
            datos["cliente1"],
            datos["equipo"],
            -2
        ).procesar()
    )


    # 9 Cálculo de costo con impuesto
    ejecutar_operacion(
        9,
        "Calculo de costo sala",
        lambda: datos["sala"].calcular_costo(
            0.19
        )
    )


    # 10 Cálculo de costo con descuento
    ejecutar_operacion(
        10,
        "Calculo de costo equipo",
        lambda: datos["equipo"].calcular_costo(
            20
        )
    )

    print("\n===== SISTEMA FINALIZADO =====")


if __name__ == "__main__":
    main()