# Clase online
def clasificar_triangulo():
    try:
        lado1 = float(input("Ingresa el primer lado del triángulo: "))
        lado2 = float(input("Ingresa el segundo lado del triángulo: "))
        lado3 = float(input("Ingresa el tercer lado del triángulo: "))
        
        if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
            if lado1 == lado2 == lado3:
                tipo = "equilátero"
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                tipo = "isósceles"
            else:
                tipo = "escaleno"
            print(f"El triángulo es {tipo}.")
        else:
            print("Los valores ingresados no forman un triángulo válido.")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")




def calculadora():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operacion = input("Elige una operación (+, -, *, /): ")
        
        match operacion:
            case '+':
                resultado = num1 + num2
            case '-':
                resultado = num1 - num2
            case '*':
                resultado = num1 * num2
            case '/':
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero.")
                resultado = num1 / num2
            case _:
                raise ValueError("Operación no válida.")
        
        print(f"El resultado es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")




# Conversor de Monedas
def convertir_moneda():
    try:
        monto = float(input("Ingresa el monto en dólares: "))
        moneda = input("Elige la moneda a convertir (EUR, MXN, JPY): ").upper()
        
        tasas_cambio = {
            "EUR": 0.85,  # Ejemplo de tasa de cambio
            "MXN": 20.0,
            "JPY": 110.0
        }
        
        match moneda:
            case "EUR":
                resultado = monto * tasas_cambio["EUR"]
            case "MXN":
                resultado = monto * tasas_cambio["MXN"]
            case "JPY":
                resultado = monto * tasas_cambio["JPY"]
            case _:
                raise ValueError("Moneda no válida.")
        
        print(f"{monto} USD equivale a {resultado:.2f} {moneda}")
    except ValueError as e:
        print(f"Error: {e}")




def evaluar_nota():
    try:
        nota = int(input("Ingresa una nota de 0 a 100: "))
        
        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100.")
        
        match nota:
            case _ if 90 <= nota <= 100:
                mensaje = "Excelente"
            case _ if 80 <= nota <= 89:
                mensaje = "Muy bien"
            case _ if 70 <= nota <= 79:
                mensaje = "Bien"
            case _ if 60 <= nota <= 69:
                mensaje = "Suficiente"
            case _:
                mensaje = "Reprobado"
        
        print(f"Calificación: {mensaje}")
    except ValueError as e:
        print(f"Error: {e}")


