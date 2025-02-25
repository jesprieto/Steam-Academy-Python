import random
def contrasenaAleatoria():
    #Genera una contrase;a de las escogidas
    contrasena = int(input("Ingresa la contrasena"))
    
    if contrasena == contrasenaCorrecta:\
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
        contrasenaAleatoria()
contrasenaAleatoria()