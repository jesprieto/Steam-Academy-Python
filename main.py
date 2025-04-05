import tkinter as tk
from tkinter import simpledialog, messagebox
from generador import generar_contrasena
from validacion import validar_contrasena

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    try:
        longitud = simpledialog.askinteger("🔢 Longitud", "¿Cuántos caracteres debe tener la contraseña?")
        if not longitud or longitud <= 0:
            raise ValueError("⚠️ Longitud inválida.")

        usar_mayusculas = messagebox.askyesno("🅰️ Mayúsculas", "¿Quieres incluir letras mayúsculas?")
        usar_numeros = messagebox.askyesno("🔢 Números", "¿Quieres incluir números?")
        usar_especiales = messagebox.askyesno("✨ Especiales", "¿Quieres incluir caracteres especiales?")

        contrasena = generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_especiales)
        messagebox.showinfo("🔐 Contraseña Generada", f"Tu nueva contraseña es:\n\n{contrasena}")

        es_segura, resultado = validar_contrasena(contrasena)
        if es_segura:
            messagebox.showinfo("✅ Seguridad", resultado)
        else:
            messagebox.showwarning("⚠️ Atención", resultado)

    except Exception as e:
        messagebox.showerror("❌ Error", str(e))

if __name__ == "__main__":
    main()
