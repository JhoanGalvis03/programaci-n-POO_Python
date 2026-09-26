from botella import Botella


class BotellaVidrio(Botella):
    """Botella de vidrio: sobrescribe los métodos que cambian según el material."""

    def __init__(self, capacidad, forma, diseño, tapa, grabados):
        super().__init__("Vidrio", capacidad, forma, diseño, tapa, grabados)

    def compatibilidad_bebidas(self):
        return "Compatible con bebidas calientes y frías sin alterar el sabor."

    def reutilizacion(self):
        return "Alta reutilización: soporta múltiples lavados y rellenados."

    def transparencia(self):
        return "Transparencia alta: permite ver el contenido con claridad."

    def manejo(self):
        return "Manejo cuidadoso: es frágil y más pesada que otros materiales."