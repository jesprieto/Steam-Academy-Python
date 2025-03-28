import random
import time

def elegir_opcion(opciones):
    """Función para pedir al usuario una opción válida."""
    while True:
        try:
            opcion = int(input("Elige una opción: "))
            if opcion not in opciones:
                raise ValueError("Opción no válida. Intenta de nuevo.")
            return opcion
        except ValueError as e:
            print(f"❌ Error: {e}")

def batalla(alien, escudos_jugador, combustible):
    """Simula una batalla entre la nave y un alienígena."""
    print(f"\n👾 ¡Un {alien} se acerca a tu nave! Prepárate para la batalla.")
    vida_alien = random.randint(10, 30)
    
    while escudos_jugador > 0 and vida_alien > 0:
        try:
            print(f"\nEscudos de la nave: 🛡️ {escudos_jugador} | Vida del {alien}: 👾 {vida_alien}")
            ataque = int(input("📌 Elige tu ataque (1: Disparo láser ⚡ | 2: Misil pesado 💥): "))
            if ataque not in [1, 2]:
                raise ValueError("Debes elegir 1 o 2.")

            if ataque == 1:
                dano = random.randint(5, 10)
                combustible -= 5  # Consume combustible
            else:
                dano = random.randint(10, 20)
                combustible -= 10  # Consume más combustible

            vida_alien -= dano
            print(f"🔥 Has hecho {dano} de daño al {alien}!")
            print(f"Combustible restante: ⛽ {combustible}")

            if vida_alien > 0:
                dano_recibido = random.randint(5, 15)
                escudos_jugador -= dano_recibido
                print(f"💥 El {alien} ataca tu nave y reduce tus escudos en {dano_recibido}!")

        except ValueError as e:
            print(f"❌ Error: {e}")

    if escudos_jugador > 0:
        print(f"\n🎉 ¡Has derrotado al {alien}!")
        return escudos_jugador, combustible
    else:
        print("\n💥 Tu nave ha sido destruida... Fin del juego.")
        exit()

def evento_aleatorio(escudos_jugador, combustible):
    """Genera un evento aleatorio durante la exploración."""
    eventos = [
        ("fallo_técnico", "🚨 ¡Fallo técnico! Pierdes 10 de combustible."),
        ("recurso", "💰 Encuentras un asteroide rico en recursos. Ganas 20 de combustible."),
        ("alien", "👾 ¡Un alienígena hostil aparece!"),
        ("nada", "🌌 No encuentras nada interesante...")
    ]
    evento, mensaje = random.choice(eventos)
    print(f"\n{mensaje}")

    if evento == "fallo_técnico":
        combustible -= 10
    elif evento == "recurso":
        combustible += 20
    elif evento == "alien":
        escudos_jugador, combustible = batalla("Alienígena", escudos_jugador, combustible)
    
    return escudos_jugador, combustible

def juego():
    """Función principal del juego."""
    escudos_jugador = 50
    combustible = 100
    print("\n🚀 Bienvenido a la EXPLORACIÓN ESPACIAL 🌌")
    time.sleep(1)
    print("\nEstás en una misión en el espacio profundo. Debes sobrevivir y encontrar el camino de regreso a la Tierra.")
    
    print("\n¿Qué deseas hacer?")
    print("1️⃣ Explorar el sector actual.")
    print("2️⃣ Saltar a otro sector (consume 20 de combustible).")
    
    opcion = elegir_opcion([1, 2])
    
    if opcion == 2:
        combustible -= 20
        print(f"\n⏩ Saltas a otro sector. Combustible restante: ⛽ {combustible}")
    
    while combustible > 0 and escudos_jugador > 0:
        print("\n🛸 Explorando el sector...")
        time.sleep(2)
        escudos_jugador, combustible = evento_aleatorio(escudos_jugador, combustible)
        
        if combustible <= 0:
            print("\n⛽ ¡Te has quedado sin combustible! Tu nave queda a la deriva... Fin del juego.")
            break
        elif escudos_jugador <= 0:
            print("\n💥 Tus escudos han fallado. La nave es destruida... Fin del juego.")
            break
        
        print(f"\nEscudos: 🛡️ {escudos_jugador} | Combustible: ⛽ {combustible}")
        print("1️⃣ Continuar explorando.")
        print("2️⃣ Intentar regresar a la Tierra (necesitas al menos 30 de combustible).")
        
        opcion = elegir_opcion([1, 2])
        
        if opcion == 2:
            if combustible >= 30:
                print("\n🌍 ¡Logras regresar a la Tierra! Misión cumplida. 🏆")
                break
            else:
                print("\n🚫 No tienes suficiente combustible para regresar. Debes seguir explorando.")

    if combustible <= 0 or escudos_jugador <= 0:
        print("\n💀 Fin del juego. La misión ha fracasado.")


juego()