# Archivo principal

from mascota import Mascota

def main():

    print("=== SISTEMA DE GESTIÓN DE MASCOTAS (POO) ===")

    # Objeto 1
    mascota1 = Mascota("Luna", "Perro", 3)

    # Objeto 2
    mascota2 = Mascota("Milo", "Gato", 2)

    print("\n--- MASCOTA 1 ---")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    print("\n--- MASCOTA 2 ---")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()

if __name__ == "__main__":
    main()
