# Que es Raise
# Es la forma de como asignamos un error

try:
    edad = int(input("Ingrese edad: "))
    
    if edad < 18:
        raise TypeError("No puedes acceder, debes ser mayor de edad")

    print("Acceso permitido.")

except ValueError:
    print("Entrada inválida. Por favor, ingrese un número válido.")
except TypeError as e:
    print(e)



# Abrir  un archivo

rutaArchivo =(input(" Ingrese ruta del archivo: "))

try:
    with open (rutaArchivo, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
        print(" Archivo no existe")
    