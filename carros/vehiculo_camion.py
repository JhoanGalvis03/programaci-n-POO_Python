from vehiculo import Vehiculo


class Camion(Vehiculo):
    """Camión de carga: sobrescribe métodos que cambian según el tipo de vehículo."""

    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)

    def aceleracion_y_frenado(self):
        return "Aceleración progresiva y frenado reforzado por el peso de la carga."

    def sistema_direccion(self):
        return "Dirección hidráulica asistida para mayor maniobrabilidad."

    def climatizacion(self):
        return "Climatización básica solo en la cabina del conductor."

    def sistema_espejos(self):
        return "Espejos laterales grandes y ajustables eléctricamente para ver la carga."