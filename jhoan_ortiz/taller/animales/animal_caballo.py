from animal import Animal


class Caballo(Animal):
    """Caballo: sobrescribe métodos que cambian según el tipo de animal."""

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return f"{self.nombre} corre a galope por la pradera."

    def comunicacion(self):
        return f"{self.nombre} se comunica mediante relinchos y lenguaje corporal."

    def alimentarse(self):
        return "Pastan hierba durante gran parte del día (herbívoro)."

    def interaccion_social(self):
        return "Vive en manadas con jerarquía social definida."