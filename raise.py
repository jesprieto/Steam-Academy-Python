# Que es Raise
# Es la forma de como asignamos un error

edad = int(input("Ingrese edad: "))
try:
    if edad < 18:
        raise TypeError("no puedes acceder , debes ser mayor de edad")
except ValueError:
    print("No puedes acceder")