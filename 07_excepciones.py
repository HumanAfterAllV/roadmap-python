def manejar_error(error): 
    if isinstance(error, ValueError):
        print("Error: Debe ingresar un número válido.")
    elif isinstance(error, ZeroDivisionError):
        print("Error: No se puede dividir entre 0.")
    elif isinstance(error, KeyboardInterrupt):
        print("\nUsuario saliendo del programa por Ctrl + C.")
        exit()  # Termina el programa inmediatamente

while True:
    try: 
        dividendo = float(input("Introduce el dividendo: "))
        divisor = float(input("Introduce el divisor: "))

        resultado = dividendo / divisor
        print(f"{dividendo} / {divisor} = {resultado}")
        
        continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
        if continuar == "n":
            print("Saliendo del programa.")
            break

    except (ValueError, ZeroDivisionError) as error:
        manejar_error(error)
    
    except KeyboardInterrupt:
        manejar_error(KeyboardInterrupt()) 
