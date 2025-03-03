def fibonacci():
    num = abs(int(input("Escribe un numero: ")))

    if num <= 0:
        print("Debe ser mayor a 0")
        return
    a = 0
    b = 1

    print(a)

    if num > 1:
        print(b)

    for i in range(2, num-1):
        temp = a + b
        print(temp)
        a = b
        b = temp
    
def factorial():
    num = abs(int(input("Escribe un numero: ")))

    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print(factorial)


factorial()
