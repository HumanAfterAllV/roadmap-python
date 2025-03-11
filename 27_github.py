import subprocess

def ejecutar_comando_git(comando):
    """
    Ejecuta un comando Git y muestra la salida.
    """
    try:
        resultado = subprocess.run(comando, shell=True, text=True, capture_output=True, check=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as error:
        print(f"❌ Error al ejecutar el comando: {error}")

def menu():
    """
    CLI interactivo para ejecutar comandos de Git.
    """
    opciones = {
        1: "Ver estado del repositorio (git status)",
        2: "Inicializar un nuevo repositorio (git init)",
        3: "Crear una nueva rama (git branch)",
        4: "Cambiar de rama (git checkout)",
        5: "Hacer commit (git add . y git commit)",
        6: "Mostrar historial de commits (git log)",
        7: "Salir"
    }

    while True:
        print("\n📌 CLI de Git - Opciones:")
        for key, value in opciones.items():
            print(f"{key}. {value}")

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("❌ Error: Ingresa un número válido.")
            continue

        if opcion == 1:
            ejecutar_comando_git("git status")
        elif opcion == 2:
            ejecutar_comando_git("git init")
        elif opcion == 3:
            nombre_rama = input("Ingresa el nombre de la nueva rama: ").strip()
            ejecutar_comando_git(f"git branch {nombre_rama}")
        elif opcion == 4:
            nombre_rama = input("Ingresa el nombre de la rama a cambiar: ").strip()
            ejecutar_comando_git(f"git checkout {nombre_rama}")
        elif opcion == 5:
            mensaje = input("Ingresa el mensaje del commit: ").strip()
            ejecutar_comando_git("git add .")
            ejecutar_comando_git(f'git commit -m "{mensaje}"')
        elif opcion == 6:
            ejecutar_comando_git("git log --oneline")
        elif opcion == 7:
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida.")


menu()
