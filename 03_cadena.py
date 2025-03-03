def palindromo():
    print("Palíndromo")

    palabra = str(input("Introduce una palabra: ")).strip().lower()
    palabra_revert = ''.join(reversed(palabra))

    if palabra == palabra_revert:
        print(f"{palabra} es un palíndromo")
    else:
        print("No es un palíndromo")

def anagrama():
    print("Anagrama")

    palabra_1 = str(input("Introduce la primer palabra: ")).strip().lower()
    palabra_2 = str(input("Introduce la segunda palabra: ")).strip().lower()

    if len(palabra_1) != len(palabra_2):
        print("No es un anagrama")
    
    pal_ord_1 = ''.join(sorted(palabra_1))
    pal_ord_2 = ''.join(sorted(palabra_2))

    if pal_ord_1 == pal_ord_2:
        print("Es un anagrama")
    else:
        print("No es un anagrama")

def isograma():
    print("Isograma")

    letras = []

    palabra = str(input("Introduce una palabra: ")).strip().lower()

    for letra in palabra:
        if letra in letras:
            print("No es un isogram")
            return
        letras.append(letra)

    print(f"{palabra} es un isograma")   

def menu():
    menu = {
        1: "Palindromo",
        2: "Anagrama",
        3: "Isogram"
    }  
    while True:
        print("Menu")
        for key, value in menu.items():
            print(f"{key} - {value}")

        try:
            opcion = abs(int(input("Introduce una opción: ")))

            if opcion == 1:
                palindromo()
            elif opcion == 2:
                anagrama()
            elif opcion == 3:
                isograma()
            else:
                print("Opción invalida")
        except ValueError:
            print("Error: introduce un valor correcto")
        continuar = str(input("¿Deseas continuar s/n?: ")).strip().lower()
        if continuar == "n":
            print("Saliendo del programa")
            break
        else:
            continue

menu()