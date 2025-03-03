class Conjuntos():
    def __init__(self):
        self.conjuntos =[]

    def añadir_final(self):
        print("Añadir al final")

        elemento = str(input("Añade un lenguaje de programación: ")).strip().lower()
        format_elemento = elemento.replace(" ", "-")

        self.conjuntos.append(format_elemento)

    def añadir_principio(self):
        print("Añade al principio")

        elemento = str(input("Añade un lenguaje de programación: ")).strip().lower()
        format_elemento = elemento.replace(" ", "-")

        self.conjuntos.insert(0, format_elemento)

    def añadir_elementos_final(self):
        print("Añadir varios elementos al final")

        num_elementos = abs(int(input("¿Cuantos elementos deseas agregar?: ")))
        contador = 0

        while contador != num_elementos:
            elemento = str(input("Introduce un lenguaje de programación: ")).strip().lower()
            format_elemento = elemento.replace(" ", "-")
            self.conjuntos.append(format_elemento)
            contador += 1
    
    def añadir_elementos_posicion(self):
        print("Añadir varios elementos al final y en cierta posición")

        num_elementos = abs(int(input("¿Cuantos elementos deseas agregar?: ")))
        contador = 0

        for idx, elementos in enumerate(self.conjuntos):
            print(f"{idx} - {elementos}")

        posicion = abs(int(input("Introduce la posición: ")))

        if posicion < 0 or posicion > len(self.conjuntos):
            print("Error: Posición fuera de rango")
            return

        while contador != num_elementos:
            elemento = str(input("Introduce un lenguaje de programación: ")).strip().lower()
            format_elemento = elemento.replace(" ", "-")
            self.conjuntos.insert(posicion, format_elemento)
            contador += 1
    

    def eliminar_elemento(self):
        print("Eliminar elemento por posición")

        for idx, elemento in enumerate(self.conjuntos):
            print(f"{idx} - {elemento}")

        elemento = str(input("Introduce elemento a eliminar: ")).strip().lower()

        if elemento in self.conjuntos:
            self.conjuntos.remove(elemento)
        else:
            print("Elemento no existe en la lista")
            
    def actualizar_elemento(self):
        print("Actualizar elemento")

        print("Actualizar elemento")

        for idx, elemento in enumerate(self.conjuntos):
            print(f"{idx} - {elemento}")

        elemento = str(input("Introduce el elemento a actualizar: ")).strip().lower()

        if elemento in self.conjuntos:
            nuevo_elemento = str(input("Introduce el nuevo nombre: ")).strip().lower()
            idx = self.conjuntos.index(elemento)  
            self.conjuntos[idx] = nuevo_elemento
            print("Elemento actualizado con éxito.")
        else:
            print("Error: Elemento no encontrado.")

    def elemento_existe(self):
        print("Buscar elemento: ")

        elemento = str(input("Introduce elemento a buscas: ")).strip().lower()

        print(elemento in self.conjuntos)

    def ver_elementos(self):
        print("Ver elementos")

        if not self.conjuntos:
            print("Lista vacía")
            return

        for idx, elementos in enumerate(self.conjuntos):
            print(f"{idx} - {elementos}")

    def eliminar_todos(self):
        print("Eliminar todos los elementos")

        if not self.conjuntos:
            print("Lista vacía")
            return

        self.conjuntos.clear()
        print("Lista vacía")


def menu():
    new_conjuntos= Conjuntos()
    menu = {
        1: "Añadir al final",
        2: "Añadir al principio",
        3: "Añadir varios elementos al final",
        4: "Añadir elementos por posición",
        5: "Eliminar elementos",
        6: "Actualizar elementos",
        7: "Ver elementos",
        8: "Actualizar elemento",
        9: "Eliminar toda la lista"
    } 

    while True:

        for key, value in menu.items():
            print(f"{key} - {value}")

        try:
            opcion = abs(int(input("Introduce una opción valida: ")))

            if opcion == 1:
                new_conjuntos.añadir_final()
            elif opcion == 2:
                new_conjuntos.añadir_principio()
            elif opcion == 3:
                new_conjuntos.añadir_elementos_final()
            elif opcion == 4:
                new_conjuntos.añadir_elementos_posicion()
            elif opcion == 5:
                new_conjuntos.eliminar_elemento()
            elif opcion == 6:
                new_conjuntos.actualizar_elemento()
            elif opcion == 7:
                new_conjuntos.ver_elementos()
            elif opcion == 8:
                new_conjuntos.actualizar_elemento()
            elif opcion == 9:
                new_conjuntos.eliminar_todos()
            else:
                print("Error: Introduzca una opción valida")

        except ValueError:
            print("Error: Introduzca un valor correcto")

        continuar = str(input("¿Deseas continuar s/n?: ")).strip().lower()

        if continuar == "n":
            print("Saliendo del programa")
            break
        else:
            continue

menu()