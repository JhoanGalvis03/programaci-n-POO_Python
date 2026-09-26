from botella_vidrio import BotellaVidrio
from botella_plastica import BotellaPlastica


def mostrar_info(botella):
    print(botella)
    print("-", botella.contener_liquidos())
    print("-", botella.facilitar_vertido())
    print("-", botella.cierre_hermetico())
    print("-", botella.transporte())
    print("-", botella.manejo())
    print("-", botella.compatibilidad_bebidas())
    print("-", botella.reutilizacion())
    print("-", botella.transparencia())
    print("=" * 60)


if __name__ == "__main__":
    inventario = [
        BotellaVidrio(capacidad="750 ml", forma="Cilíndrica", diseño="Clásico",
                       tapa="Corcho", grabados="Logo de la marca"),
        BotellaPlastica(capacidad="500 ml", forma="Ergonómica", diseño="Moderno",
                         tapa="Rosca", grabados="Sin grabados"),
    ]

    for botella in inventario:
        mostrar_info(botella)