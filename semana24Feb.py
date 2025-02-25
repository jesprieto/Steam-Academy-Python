def bloque1():
            
            contrasena_Ingresada = str(input("Ingrese la contrasena:_______"))
            contrasena_correcta = "1234"
            while contrasena_Ingresada != contrasena_correcta:
                contrasena_Ingresada = str(input("Ingrese la contrasena:_______"))

                if contrasena_Ingresada == contrasena_correcta:
                    print("Acceso Valido")
            
                else:
                    print("Acceso Invalido, vuelva a ingresar")
                
            nombre = str(input("Ingrese su nombre:_______"))
            print(f'Bienvenido', nombre)

bloque1()