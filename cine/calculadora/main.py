# crea un progama de modularzacion que cree una calculadora de operaciones basicas y que contenga un mendu para elegir
# operaciones basicas
import division
import multiplicacion
import resta
import suma
import time

def calculadora():
    print("Bievenido, a la Calculadora: ")
    time.sleep(2)
    num1 = int(input("Ingrese el primer valor: "))
    num2 = int(input("Ingrese el segundo valor: "))

    while True:
        opciones = int(input("\n "
        "1: Suma \n"
        "2: Resta \n"
        "3: Multiplicacion \n"
        "4: Division \n" ))
        
        if opciones in range(1,5):
            print("su operacion se esta realizando... espere")
            time.sleep(2)
            print("la paciencia es una virtud")
            time.sleep(2)
            if opciones == 1:
                print( suma.sumar(num1,num2))
                break
            elif opciones == 2:
                print(resta.restar(num1,num2))
                break
            elif opciones == 3:
                print(multiplicacion.multiplicar(num1, num2))
                break
            elif opciones == 4:
                print(division.dividir(num1, num2))
                break
            else:
                print("Debe Seleccinoar una opcion valida")
calculadora()







