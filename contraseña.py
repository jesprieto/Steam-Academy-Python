          
def contraseña1():
    while True:
        contraseña_correcta = input("Ingresa tu contraseña: ")
        contraseña = "12345"
        if contraseña != contraseña_correcta:
            print("La contraseña no es correcta")
        else:
            print("Contraseña Correcta")
            break  

contraseña1()
