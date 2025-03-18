def ejercicio2():
    numero = int(input("ingrese un  numero: "))
    suma = 0

    for i  in range (1, numero +1):
        suma +=i
    print("la suma de los primeros", numero, "numero es:",suma)




# Tabla de Multiplicar
def ejercicio3():
    n = int(input("ingrese un  numero: "))
    for i in range (1, 11):
        resultado = n * i
        print(n, "x", i , "=", resultado) 


#Contar cuántos números son pares e impares en una lista
def ejercicio4():
    cantidad = int(input("Ingresa la cantidad de numeros: "))


    pares = 0
    impares = 0
    for _ in range(cantidad):
        n =int(input("Ingresa un numero: "))
        if n % 2 == 0:
            pares += 1
        else:
            impares +=1

    print("Numeros pares:", pares)
    print("Numeros pares:", impares)



#Suma de los primeros N números
def ejercicio5():
    N = int(input("Ingresa un número: "))  # Pedimos un número al usuario y lo convertimos en entero

    factorial = 1  # Inicializamos la variable factorial en 1

    for i in range(1, N + 1):  # Iteramos desde 1 hasta N (incluido)
        factorial *= i  # Multiplicamos factorial por i en cada iteración

    print(f"El factorial de {N} es: {factorial}")  # Mostramos el resultado


#Recorrer una lista de nombres
def ejercicio6():
    nombres = input("Ingresa nombres separados por comas: ").split(",")  # Convierte la entrada en una lista

    for nombre in nombres:  # Itera sobre cada elemento de la lista
        print(f"Hola, {nombre.strip()}!")  # Saluda y elimina espacios extra con strip()
