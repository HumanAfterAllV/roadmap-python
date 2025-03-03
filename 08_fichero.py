import os

class gestor:
    def __init__(self, gestor="gestor.txt"):
        self.gestor = gestor
        
        if not os.path.exists(self.gestor):
            with open(self.gestor, "w") as archivo:
                archivo.write("")


    def agregar_venta(self):
        print("Agregar venta")

        producto = str(input("Introduce el nombre del producto: ")).strip().lower()
        cantidad_vendida = abs(int(input("Introduce la cantidad vendida: ")))
        precio = float(input("Introduce el precio:$"))

        format_producto = producto.replace(" ", "-")

        
        with open("gestor.txt", "a") as archivo:
            archivo.write(f"{format_producto}, {cantidad_vendida}, {precio} \n")

        print("Venta agregada con éxito")

    def leer_documento(self):
        print("Gestor - ventas registradas")

        with open("gestor.txt", "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo")
            print(contenido if contenido else "Contenido vació")

    def actualizar_venta(self):
        print("Actualizar venta")

        with open("gestor.txt", "r") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("Archivo vació")
            return
        
        producto = str(input("Introduce el nombre del producto actualizar: ")).strip().lower()
        
        with open("gestor.txt", "w") as archivo:
            for linea in lineas:
                if producto in linea:
                    new_producto = str(input("Introduce el nombre del producto: "))
                    cantidad_vendida = abs(int(input("Introduce la cantidad vendida: ")))
                    precio = float(input("Introduce el precio:$ "))
                    format_producto = new_producto.replace(" ", "-")
                    archivo.write(f"{format_producto}, {cantidad_vendida}, {precio} \n")
                    print("Producto actualizado")
                else:
                    archivo.write(linea)
    def ventas_totales(self):
        print("Ventas totales")

        total = 0

        with open("gestor.txt", "r") as archivo:
            lineas = archivo.readlines()
    
        if not lineas:
            print("Archivo vació")
            return
        
        for linea in lineas:
            if "----Gestor----" in lineas:
                continue

            partes = linea.strip().split(", ")
            if len(partes) == 3:
                try:
                    cantidad = int(partes[1])
                    precio = float(partes[2])
                    total += cantidad * precio
                except ValueError:
                    print(f"Error al procesar la linea: {linea.strip()}")
        print(f"Total de ventas: {total}")

    def eliminar_venta(self):
        print("Eliminar venta")

        with open("gestor.txt", "r") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("Archivo vació")
            return

        producto = str("Introduce el nombre del producto a eliminar: ").strip().lower()
        format_producto = producto.replace(" ", "-")

        with open("gestor.txt", "w") as archivo:
            for linea in lineas:
                if format_producto not in linea:
                    archivo.write(linea)
        
        print("Venta eliminada con éxito")


def manejar_error(error): 
    if isinstance(error, ValueError):
        print("Error: Debe ingresar un número válido.")
    elif isinstance(error, KeyboardInterrupt):
        print("\nUsuario saliendo del programa por Ctrl + C.")
        exit()  


def menu():

    new_gestor = gestor()
    menu = {
        1: "Agregar venta",
        2: "Modificar venta",
        3: "Ver ventas",
        4: "Calcular ventas totales",
        5: "Eliminar venta",
        6: "Salir"
    }

    while True:
        for key, value in menu.items():
            print(f"{key} - {value}")
        
        try:
            respuesta = abs(int(input("Introduce una opción: ")))

            if respuesta == 1:
                new_gestor.agregar_venta()
            elif respuesta == 2:
                new_gestor.actualizar_venta()
            elif respuesta == 3:
                new_gestor.leer_documento()
            elif respuesta == 4:
                new_gestor.ventas_totales()
            elif respuesta == 5:
                new_gestor.eliminar_venta()
            elif respuesta == 6:
                print("Saliendo del programa")
                if os.path.exists("gestor.txt"):
                    os.remove("gestor.txt")
                break

        except (ValueError) as error:
            manejar_error(error)

        except KeyboardInterrupt:
            manejar_error(KeyboardInterrupt())

        continuar = str(input("¿Deseas continuar s/n?")).strip().lower()

        if continuar == "n":
            print("Saliendo del programa")
            if os.path.exists("gestor.txt"):
                os.remove("gestor.txt")
            break
        else:
            continue
        
             
menu()