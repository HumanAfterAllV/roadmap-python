def peticion(cadena_1, cadena_2):
    n = 1
    for n in range(101):
        result = ""
        if n % 3 == 0:
            result += cadena_1
        if n %5 == 0:
            result += cadena_2
        print(result or n)

print(peticion("Hola", "Buenas"))
