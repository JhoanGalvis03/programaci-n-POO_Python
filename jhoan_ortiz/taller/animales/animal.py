class Animal:
    """Clase base: atributos y métodos comunes a cualquier animal."""

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def moverse(self):
        return f"{self.nombre} se mueve de forma estándar."

    def comunicacion(self):
        return f"{self.nombre} se comunica con sonidos básicos."

    def reproduccion(self):
        return "Se reproduce según su ciclo natural."

    def alimentarse(self):
        return f"Se alimenta principalmente de una dieta {self.dieta}."

    def adaptacion(self):
        return f"Está adaptado para vivir en su hábitat: {self.habitat}."

    def instintos(self):
        return "Presenta instintos básicos de supervivencia."

    def descanso(self):
        return "Descansa periódicamente para conservar energía."

    def sueño(self):
        return "Duerme según su ritmo natural."

    def interaccion_social(self):
        return "Puede interactuar con otros individuos de su especie."

    def __str__(self):
        return (f"Animal(nombre={self.nombre}, edad={self.edad}, habitat={self.habitat}, "
                f"dieta={self.dieta}, tamaño={self.tamaño}, color={self.color})")