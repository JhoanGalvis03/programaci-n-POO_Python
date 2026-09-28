from animal import Animal


class Pato(Animal):
    """Pato: sobrescribe métodos que cambian según el tipo de animal."""

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return f"{self.nombre} nada en el agua y también puede caminar y volar."

    def comunicacion(self):
        return f"{self.nombre} se comunica mediante graznidos."

    def alimentarse(self):
        return "Se alimenta de plantas acuáticas, insectos y pequeños peces (omnívoro)."

    def adaptacion(self):
        return "Tiene patas palmeadas y plumas impermeables para el agua."