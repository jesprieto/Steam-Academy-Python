# Collect proper garbage type

def TrashCollector():
    try:
        desecho = input("""Ingrese su tipo de basura: 
                           1. Plastico
                           2. Organico
                           3. Papel: """).capitalize()
        match desecho:
            case "1" | "Plastico":
                resultado = "Plastico"
                print(f"Su basura será arrojada al contenedor de {resultado}")
            case "2" | "Organico":
                resultado = "Organico"
                print(f"Su basura será arrojada al contenedor de {resultado}")
            case "3" | "Papel":
                resultado = "Papel"
                print(f"Su basura será arrojada al contenedor de {resultado}")
            case _:
                print("No has seleccionado un tipo de basura válido")
    except ValueError:
        print("Vuelve a seleccionar el tipo de desecho")

TrashCollector()