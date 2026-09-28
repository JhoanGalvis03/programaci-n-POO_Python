from vehiculo import Vehiculo


class Carro(Vehiculo):
    """Carro particular: sobrescribe métodos que cambian según el tipo de vehículo."""

    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)

    def aceleracion_y_frenado(self):
        return "Aceleración rápida y frenado deportivo con ABS."

    def climatizacion(self):
        return "Climatización automática de doble zona."

    def luces(self):
        return "Luces LED delanteras y traseras con luz diurna."

    def sistema_ventanas(self):
        return "Ventanas eléctricas con función de subida/bajada automática."