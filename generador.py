import random
import string

def generar_contrasena(longitud, usar_mayusculas=True, usar_numeros=True, usar_especiales=True):
    caracteres = list(string.ascii_lowercase)
    
    if usar_mayusculas:
        caracteres += list(string.ascii_uppercase)
    if usar_numeros:
        caracteres += list(string.digits)
    if usar_especiales:
        caracteres += list("!@#$%^&*()")

    if not caracteres:
        raise ValueError("⚠️ ¡Debes seleccionar al menos un tipo de carácter!")

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena
