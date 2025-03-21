import random

# Lista de palabras
palabras = ["python", "programacion", "ahorcado", "computadora", "teclado"]

# Seleccionar una palabra al azar
palabra_secreta = random.choice(palabras)

# Inicializar variables
intentos_restantes = 6
letras_adivinadas = ["_"] * len(palabra_secreta)

print("¡Bienvenido al juego del ahorcado!")
print(" ".join(letras_adivinadas))  # Mostrar el progreso inicial

while intentos_restantes > 0:
    letra = input("\nIngresa una letra: ").lower()

    if letra in palabra_secreta:
        print(f"¡Correcto! La letra '{letra}' está en la palabra.")
        # Actualizar las letras adivinadas
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                letras_adivinadas[i] = letra
    else:
        print(f"Incorrecto. La letra '{letra}' no está en la palabra.")
        intentos_restantes -= 1

    # Mostrar el progreso actual
    print(" ".join(letras_adivinadas))
    print(f"Intentos restantes: {intentos_restantes}")

    # Verificar si el jugador ha adivinado la palabra
    if "_" not in letras_adivinadas:
        print("\n¡Felicidades! ¡Has adivinado la palabra!")
        break

# Si se agotan los intentos
if intentos_restantes == 0:
    print(f"\n¡Oh no! Te has quedado sin intentos. La palabra era: {palabra_secreta}")