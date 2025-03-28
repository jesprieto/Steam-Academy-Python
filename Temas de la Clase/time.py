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

# - Cambiar de formato al tiempo actual con stfftime
#tiempo_actual = time.localtime()
#tiempo = time.strftime("%B %d %y %H:%M:%S", tiempo_actual)
#print(tiempo)

# - Cabiar de formato al tiempo Universal
#tiempo_actual = time.gmtime()
#tiempo = time.strftime("%B %d %y %H:%M:%S", tiempo_actual)
#print(tiempo)


#Str Time - Analiza una cadena de tiempo y devuelve el objeto de tiempo
#cadena_tiempo = '23 February, 2025'
#tiempo = time.strptime(cadena_tiempo, '%d %B, %Y')
#print(tiempo)


#Convierte una tupla de tiempo en una cadena legible
#tiempo_tupla = (2025, 2, 23, 14, 24,0,0,0,0)
#cadena_tiempo = time.asctime(tiempo_tupla)
#print(cadena_tiempo)

# Convierte el tiempo en segundos desde que inicio el tiempo en nuestro pc
#tiempo_tupla = (2025, 2, 23, 14, 24,0,0,0,0)
#cadena_tiempo = time.mktime(tiempo_tupla)
#print(cadena_tiempo)


#------ Ejercicio de Datos:

def solicitudDocumentacon():
    try:
        Archivo = str(input('''Ingrese el nombre del archivo a solicitar: 
                            1. Reporte de Facturas
                            2. Reporte de Compras
                            3. Reporte de Pagos: '''))
        tiempo_actual = time.localtime()
        tiempo = time.strftime("%B %d %y %H:%M:%S", tiempo_actual)
        match Archivo:
            case "1" | "Reporte de Facturas":
                Archivo = "Reporte de Facturas"
                print(f'''
                      --- Su Archivo de {Archivo} 
                      fue solicitado, {tiempo} 
                      Tiempo de Envio: 24 hrs--- ''')
            case "2" | "Reporte de Compras":
                Archivo = "Reporte de Compras"
                print(f'''
                      --- Su Archivo de {Archivo} 
                      fue solicitado, {tiempo} 
                      Tiempo de Envio: 24 hrs ---''')
            case "3" | "Reporte de Pagos":
                Archivo = "Reporte de Pagos"
                print(f'''
                      --- Su Archivo de {Archivo} 
                      fue solicitado, {tiempo} 
                      Tiempo de Envio: 24 hrs--- ''')
    except ValueError:
        print("Ingreso un dato incorrecto")
    except TypeError:
        print("Ingreso un dato incorrecto")

solicitudDocumentacon()