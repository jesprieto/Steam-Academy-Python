
from datetime import datetime
import math  

# Ejercicio 1: Calculadora de Edad
def calcular_edad():
    año_nacimiento = int(input("Ingresa tu año de nacimiento: "))
    año_actual = datetime.now().year
    edad = año_actual - año_nacimiento
    print(f"Tienes {edad} años.")

# Ejercicio 2: Conversión de Temperatura
def convertir_temperatura():
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32 
    print(f"{celsius}°C equivale a {fahrenheit:.2f}°F.")

# Ejercicio 3: Área de un Círculo
def calcular_area_circulo():
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * (radio ** 2)  # Fórmula del área
    print(f"El área del círculo es {area:.2f} unidades cuadradas.")

# Ejercicio 4: Costo de un Viaje
def calcular_costo_viaje():
    precio_gasolina = float(input("Ingresa el precio de la gasolina por litro: "))
    km_recorrer = float(input("Ingresa la distancia a recorrer en km: "))
    consumo_vehiculo = float(input("Ingresa el consumo del vehículo en km/l: "))
    
    costo_total = (km_recorrer / consumo_vehiculo) * precio_gasolina
    print(f"El costo total del viaje será de ${costo_total:.2f}.")



# Ejercicio 5: Conversión de Moneda
def convertir_moneda():
    tasa_cambio = 0.85  # 1 USD = 0.85 EUR
    dolares = float(input("Ingresa la cantidad en dólares: "))
    euros = dolares * tasa_cambio
    print(f"${dolares:.2f} USD equivale a €{euros:.2f} EUR.")

# Ejercicio 6: Promedio de Notas
def calcular_promedio():
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    
    promedio = sum(notas) / len(notas)  # Calcula el promedio
    print(f"El promedio de las notas es {promedio:.2f}.")
calcular_promedio()



# Ejercicio 7: Cálculo de IMC
def calcular_imc():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    
    imc = peso / (altura ** 2)  # Fórmula del IMC
    print(f"Tu IMC es {imc:.2f}.")

    # Clasificación del IMC
    if imc < 18.5:
        print("Clasificación: Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Clasificación: Peso normal")
    else:
        print("Clasificación: Sobrepeso")

# Ejercicio 8: Cálculo de Descuento
def calcular_descuento():
    precio_original = float(input("Ingresa el precio original del producto: "))
    descuento = precio_original * 0.10  # Calcula el 10% de descuento
    precio_final = precio_original - descuento
    print(f"El precio con descuento es: ${precio_final:.2f}.")

# Menú para seleccionar el ejercicio
def menu():
    opciones = {
        1: calcular_edad,
        2: convertir_temperatura,
        3: calcular_area_circulo,
        4: calcular_costo_viaje,
        5: convertir_moneda,
        6: calcular_promedio,
        7: calcular_imc,
        8: calcular_descuento
    }

    while True:
        print("\nSeleccione un ejercicio:")
        print("1. Calculadora de Edad")
        print("2. Conversión de Temperatura")
        print("3. Área de un Círculo")
        print("4. Costo de un Viaje")
        print("5. Conversión de Moneda")
        print("6. Promedio de Notas")
        print("7. Cálculo de IMC")
        print("8. Cálculo de Descuento")
        print("9. Salir")

        opcion = int(input("Ingresa el número de opción: "))

        if opcion == 9:
            print("Saliendo del programa...")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Inténtalo de nuevo.")






# Ejercicio 1: Clasificación de Edad
def clasificar_edad():
    edad = int(input("Ingresa tu edad: "))

    if edad < 12:
        print("Eres un Niño.")
    elif 13 <= edad <= 17:
        print("Eres un Adolescente.")
    elif 18 <= edad <= 59:
        print("Eres un Adulto.")
    else:
        print("Eres un Anciano.")

# Ejercicio 2: Aprobación de un Examen
def verificar_aprobacion():
    nota = float(input("Ingresa tu nota: "))

    if nota >= 60:
        print("Aprobado.")
    else:
        print("Reprobado.")

# Ejercicio 3: Tarifa de Transporte
def calcular_tarifa_transporte():
    edad = int(input("Ingresa tu edad: "))

    if edad < 5:
        print("Viajas Gratis.")
    elif 5 <= edad <= 17 or edad > 60:
        print("Tarifa media.")
    else:
        print("Tarifa completa.")

# Ejercicio 4: Calculadora de Impuestos
def calcular_impuestos():
    salario = float(input("Ingresa tu salario en USD: "))

    if salario > 3000:
        impuesto = salario * 0.15  # 15% de impuesto
    else:
        impuesto = salario * 0.05  # 5% de impuesto

    total = salario - impuesto
    print(f"Impuesto aplicado: ${impuesto:.2f}")
    print(f"Salario después de impuestos: ${total:.2f}")

# Ejercicio 5: Par o Impar
def verificar_paridad():
    numero = int(input("Ingresa un número: "))

    if numero % 2 == 0:
        print("El número es Par.")
    else:
        print("El número es Impar.")

# Ejercicio 6: Descuento por Compras
def calcular_descuento_compra():
    monto = float(input("Ingresa el monto de la compra en USD: "))

    if monto > 100:
        descuento = monto * 0.20  # 20% de descuento
        total = monto - descuento
        print(f"Descuento aplicado: ${descuento:.2f}")
        print(f"Total a pagar: ${total:.2f}")
    else:
        print(f"No hay descuento. Total a pagar: ${monto:.2f}")

# Ejercicio 7: Sistema de Acceso
def verificar_acceso():
    usuario_correcto = "admin"
    contraseña_correcta = "1234"

    usuario = input("Ingresa tu usuario: ")
    contraseña = input("Ingresa tu contraseña: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Acceso concedido.")
    else:
        print("Acceso denegado.")

# Ejercicio 8: Clasificación de Triángulos
def clasificar_triangulo():
    lado1 = float(input("Ingresa el primer lado del triángulo: "))
    lado2 = float(input("Ingresa el segundo lado del triángulo: "))
    lado3 = float(input("Ingresa el tercer lado del triángulo: "))

    if lado1 == lado2 == lado3:
        print("El triángulo es Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es Isósceles.")
    else:
        print("El triángulo es Escaleno.")

# Menú para seleccionar el ejercicio
def menu():
    opciones = {
        1: clasificar_edad,
        2: verificar_aprobacion,
        3: calcular_tarifa_transporte,
        4: calcular_impuestos,
        5: verificar_paridad,
        6: calcular_descuento_compra,
        7: verificar_acceso,
        8: clasificar_triangulo
    }

    while True:
        print("\nSeleccione un ejercicio:")
        print("1. Clasificación de Edad")
        print("2. Aprobación de un Examen")
        print("3. Tarifa de Transporte")
        print("4. Calculadora de Impuestos")
        print("5. Par o Impar")
        print("6. Descuento por Compras")
        print("7. Sistema de Acceso")
        print("8. Clasificación de Triángulos")
        print("9. Salir")

        opcion = int(input("Ingresa el número de opción: "))

        if opcion == 9:
            print("Saliendo del programa...")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Inténtalo de nuevo.")

# Ejecutar el menú
