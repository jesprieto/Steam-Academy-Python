import random

def adivina_el_animal():
    animales = ["perro", "gato", "elefante", "león", "tigre", "jirafa", "lobo", "águila", "oso", "serpiente"]
    animal_secreto = random.choice(animales)
    intentos_maximos = 5

    print("Estoy pensando en un animal... ¿Puedes adivinar cuál es?")
    print(f"Tienes {intentos_maximos} intentos para adivinar.")

    for intento in range(1, intentos_maximos + 1):
        respuesta = input(f"Intento {intento}/{intentos_maximos}: ").strip().lower()
        
        if respuesta == animal_secreto:
            print("¡Correcto! Has adivinado el animal.")
            break
        else:
            print("Incorrecto. Intenta de nuevo.")

        if intento == intentos_maximos:
            print(f"Lo siento, se acabaron los intentos. El animal era: {animal_secreto}")


adivina_el_animal()