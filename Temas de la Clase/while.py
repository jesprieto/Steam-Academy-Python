# como usar while


def ContadorWhile():
    contador = 0

    while contador < 5:
        print(f"El contador es: {contador}")
        contador += 1




def Mientras():
    contador = 0

    while True:
        print(f"El contador es: {contador}")
        contador += 1
        if contador >= 5:
            break


def Contador():
    contador = 0
    while contador < 5:
          contador += 1
          if contador == 3:
                break
          print(f"El contador es: {contador}")


#Listas

def Metodos():
    mi_lista = [1, 2, 3]
    mi_lista.append(4)  # Añade 4 al final de la lista
    print(mi_lista)  # Output: [1, 2, 3, 4]



#Diccionarios
def Diccionario():
    mi_diccionario = {'nombre': 'Juan', 'edad': 25}
    mi_diccionario['edad'] = 26  # Modifica el valor de 'edad'
    print(mi_diccionario)  # Output: {'nombre': 'Juan', 'edad': 26}


#POO
class Persona:
    def __init__(self, nombre, edad): # esto es un objeto y lo de dentro se llama parametro
        self.nombre = nombre # Valor del parametro , en este caso es nombre 
        self.edad = edad

    def saludar(self): # esto es un metodo 
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona = Persona("Ana", 30)
persona.saludar()  # Output: Hola, mi nombre es Ana y tengo 30 años.




