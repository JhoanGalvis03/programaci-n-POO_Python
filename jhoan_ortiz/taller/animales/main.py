from animal_caballo import Caballo
from animal_pato import Pato


def mostrar_info(animal):
    print(animal)
    print("-", animal.moverse())
    print("-", animal.comunicacion())
    print("-", animal.reproduccion())
    print("-", animal.alimentarse())
    print("-", animal.adaptacion())
    print("-", animal.instintos())
    print("-", animal.descanso())
    print("-", animal.sueño())
    print("-", animal.interaccion_social())
    print("=" * 60)


if __name__ == "__main__":
    inventario = [
        Caballo(nombre="Trueno", edad=5, habitat="Pradera", dieta="herbívora",
                tamaño="Grande", color="Marrón"),
        Pato(nombre="Lucas", edad=2, habitat="Humedal", dieta="omnívora",
             tamaño="Pequeño", color="Verde y café"),
    ]

    for animal in inventario:
        mostrar_info(animal)