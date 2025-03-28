
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