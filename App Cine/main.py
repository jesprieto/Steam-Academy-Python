import time
import funciones
import asientos
import comida

def seleccionar_funcion():
    while True:
        print("\nFunciones disponibles:")  
        for key, value in funciones.funciones.items():
            print(f"{key}. {value}")

        opcion = input("\nSeleccione el número de la función: ")

        if opcion == "4":
            print("\n❌ ¡Noooo! ¿En serio quieres ver Blancanieves? Eso es un crimen cinéfilo. 😱")
            print("Por favor, escoge una película mejor. 🎬\n")
            time.sleep(2)
        elif opcion in funciones.funciones:
            return opcion
        else:
            print("\n⚠️ Opción inválida. Intente nuevamente. ⚠️\n")
            time.sleep(1)

def seleccionar_asiento():
    while True:
        print("\nAsientos disponibles:")
        for asiento, estado in asientos.asientos.items():
            print(f"{asiento}: {estado}")

        asiento_seleccionado = input("\nSeleccione su asiento: ")

        if asiento_seleccionado in asientos.asientos and asientos.asientos[asiento_seleccionado] == "Disponible":
            
            asientos.asientos[asiento_seleccionado] = "Ocupado"
            print(f"{asiento_seleccionado} es muy Comodo, Buena Elección") 
            break
        else:
            print("\n🚨 Asiento no válido o ya ocupado. Intente nuevamente. 🚨\n")

def seleccionar_comida():
    print("\nOpciones de comida:")
    for key, value in comida.comida.items():
        print(f"{key}. {value}")

    opcion_comida = input("\nSeleccione el número de su elección de comida: ")
    return comida.comida.get(opcion_comida, "Nada")

def main():
    print("🎥 Bienvenido a Python Films, tu cine de confianza 🎬")
    time.sleep(2)

    
    opcion_funcion = seleccionar_funcion()
    funcion_seleccionada = funciones.funciones[opcion_funcion]

    
    asiento_seleccionado = seleccionar_asiento()

 
    comida_seleccionada = seleccionar_comida()

    
    print("\n🎟️ Resumen de su reserva:")
    print(f"🍿 Película: {funcion_seleccionada}")
    print(f"🪑 Asiento: {asiento_seleccionado}")
    print(f"🥤 Comida: {comida_seleccionada}")
    print("\n¡Disfrute su función! 🎬🍿")

main()
