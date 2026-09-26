from botella import Botella


class BotellaPlastica(Botella):
    """Botella de plástico: sobrescribe los métodos que cambian según el material."""

    def __init__(self, capacidad, forma, diseño, tapa, grabados):
        super().__init__("Plástico", capacidad, forma, diseño, tapa, grabados)

    def compatibilidad_bebidas(self):
        return "Ideal para bebidas frías; no se recomienda con líquidos muy calientes."

    def reutilizacion(self):
        return "Reutilización limitada: se recomienda reciclar tras pocos usos."

    def transparencia(self):
        return "Transparencia media, varía según el tipo de plástico."

    def manejo(self):
        return "Manejo fácil y ligero, ideal para transportar."