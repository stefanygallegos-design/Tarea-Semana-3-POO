# Clase Mascota

class Mascota:

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("\nInformación de la mascota")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print("Sonido: Guau Guau")
        elif self.especie.lower() == "gato":
            print("Sonido: Miau Miau")
        else:
            print("Sonido: La mascota emite un sonido")
