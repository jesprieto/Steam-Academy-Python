#  biblioteca time
import time
def prueba1():


    print("Bienvenido!!")
    time.sleep(5)
    print("Esto es lo que sigue")



def prueba2():
    inicio = time.time() # guardamos el proceso
    time.sleep(2)

    fin = time.time() # Guarda el tiempo despues del proceso
    print(f"el proceso tardo{fin} segundos")


def hora():
    horaActual = time.localtime()
    print(horaActual)
    formato = time.strftime("%m-%d-%Y %H:%M")
    print(formato)

hora()