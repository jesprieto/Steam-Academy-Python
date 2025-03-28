import random

# Lista de animales
animales = ["perro", "gato", "elefante", "jirafa", "león", "tigre", "mono", "pingüino"]

print("¡Bienvenido al juego de adivinar el animal!")
print("Estoy pensando en un animal...")

# Seleccionar un animal al azar
animal_secreto = random.choice(animales)


while True:
    # Pedir al usuario que adivine
    intento = input("\nAdivina qué animal estoy pensando: ").lower()
    
    # Comprobar si adivinó
    if intento == animal_secreto:
        print("\n¡Felicitaciones! ¡Has adivinado correctamente!")
        break
    else:
        print("\nIncorrecto. ¡Intenta de nuevo!")
        print("Pista: El animal tiene", len(animal_secreto), "letras")