import random
def bloque1():
            
            contrasena_Ingresada = str(input("Ingrese la contrasena:   "))
            lista=["1234","5678","9120"]
            contrasena_correcta = random.choice(lista)
            if contrasena_Ingresada == contrasena_correcta:
                    print("Acceso Valido")
            
            else:
                    print("Acceso Invalido, vuelva a ingresar")
                    bloque1()
                
            nombre = str(input("Ingrese su nombre:_______"))
            print(f'Bienvenido', nombre)

bloque1()