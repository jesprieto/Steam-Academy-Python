import string

def validar_contrasena(contrasena):
    errores = []

    if len(contrasena) < 8:
        errores.append("🔴 La contraseña debe tener al menos 8 caracteres.")
    if not any(c.isupper() for c in contrasena):
        errores.append("🔴 Debe incluir al menos una letra mayúscula.")
    if not any(c.isdigit() for c in contrasena):
        errores.append("🔴 Debe incluir al menos un número.")
    if not any(c in "!@#$%^&*()" for c in contrasena):
        errores.append("🔴 Debe incluir al menos un carácter especial.")

    if errores:
        return False, "\n".join(errores)
    return True, "✅ ¡Tu contraseña es segura!"
