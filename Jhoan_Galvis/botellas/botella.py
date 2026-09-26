class Botella:
    """Clase base: atributos y métodos comunes a cualquier botella."""

    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados

    def contener_liquidos(self):
        return f"Contiene líquidos gracias a su cuerpo de {self.material}."

    def facilitar_vertido(self):
        return f"Su forma {self.forma} facilita el vertido del contenido."

    def cierre_hermetico(self):
        return f"La tapa tipo '{self.tapa}' garantiza un cierre hermético."

    def transporte(self):
        return "Puede transportarse de forma segura."

    def manejo(self):
        return "Permite un manejo cómodo por parte del usuario."

    def compatibilidad_bebidas(self):
        return "Compatibilidad estándar con bebidas frías."

    def reutilizacion(self):
        return "Su nivel de reutilización depende del material."

    def transparencia(self):
        return "Su nivel de transparencia depende del material."

    def __str__(self):
        return (f"Botella(material={self.material}, capacidad={self.capacidad}, "
                f"forma={self.forma}, diseño={self.diseño}, tapa={self.tapa}, "
                f"grabados={self.grabados})")