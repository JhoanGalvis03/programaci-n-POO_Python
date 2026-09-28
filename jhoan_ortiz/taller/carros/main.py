from vehiculo_carro import Carro
from vehiculo_camion import Camion


def mostrar_info(vehiculo):
    print(vehiculo)
    print("-", vehiculo.arrancar())
    print("-", vehiculo.apagar())
    print("-", vehiculo.aceleracion_y_frenado())
    print("-", vehiculo.sistema_direccion())
    print("-", vehiculo.climatizacion())
    print("-", vehiculo.luces())
    print("-", vehiculo.sistema_ventanas())
    print("-", vehiculo.sistema_espejos())
    print("=" * 60)


if __name__ == "__main__":
    inventario = [
        Carro(modelo="BMW Serie 5", color="Negro", motor="V6 3.0L",
              num_puertas=4, capacidad_pasajeros=5, tipo_combustible="Gasolina"),
        Camion(modelo="Camión de Carga", color="Blanco", motor="Diésel 4.0L",
               num_puertas=2, capacidad_pasajeros=3, tipo_combustible="Diésel"),
    ]

    for vehiculo in inventario:
        mostrar_info(vehiculo)