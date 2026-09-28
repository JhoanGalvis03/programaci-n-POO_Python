class Vehiculo:
    """Clase base: atributos y métodos comunes a cualquier vehículo."""

    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    def arrancar(self):
        return f"El vehículo {self.modelo} arranca con motor {self.motor}."

    def apagar(self):
        return f"El vehículo {self.modelo} se apaga correctamente."

    def aceleracion_y_frenado(self):
        return "Acelera y frena de forma estándar."

    def sistema_direccion(self):
        return "Cuenta con sistema de dirección convencional."

    def climatizacion(self):
        return "Climatización básica disponible."

    def luces(self):
        return "Luces delanteras y traseras estándar."

    def sistema_ventanas(self):
        return "Ventanas de accionamiento manual o eléctrico."

    def sistema_espejos(self):
        return "Espejos laterales ajustables manualmente."

    def __str__(self):
        return (f"Vehiculo(modelo={self.modelo}, color={self.color}, motor={self.motor}, "
                f"puertas={self.num_puertas}, pasajeros={self.capacidad_pasajeros}, "
                f"combustible={self.tipo_combustible})")