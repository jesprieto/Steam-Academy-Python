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



#---------------------------------------------------------------#
#Tarea de time

# - origen del tiempo de nuestro pc
# print(time.ctime(0)) 

# - Tiempo que ha pasado en Segundos desde el origen
# print(time.time()) 

# - transformas el tiempo en segundos desde el origen en formato legible
# print(time.ctime(time.time()))  

# - Otra manera de imprimir tiempo actual
#tiempo_actual = time.localtime() 
#print(tiempo_actual)

tiempo_actual = time.localtime()
tiempo = time.strftime("%B %d %y %H:%M:%S", tiempo_actual)
print(tiempo)