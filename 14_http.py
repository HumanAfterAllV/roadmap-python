import requests

def request_api(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Nombre: {data["name"]}")
        print(f"Peso: {data["weight"]}")
        print(f"Altura: {data["height"]}")
        print(f"Tipo: {[t["type"]["name"] for t in data["types"]]}")
        print(f"Habilidades: {[h["ability"]["name"] for h in data["abilities"]]}")
    else:
        print("Error: No se encontró el Pokémon")

    
while True:
    print("Pokémon")

    try:
        pokemon = str(input("Busca tu Pokémon: ")).strip().lower()

        request_api(pokemon)
    except ValueError:
        print("Error: Opción incorrecta")
    continuar = str(input("¿Deseas buscar otro Pokémon s/n ?: ")).strip().lower()

    if continuar == "n":
        print("Saliendo del programa")
        break
    else:
        continue
    