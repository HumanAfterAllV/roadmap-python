import unittest

lista = {
    "nombre": "Israel",
    "age": 27,
    "birth_date": "03 de abril",
    "programming_languages": ["Ts","Javascript","Python"]
}

def lista_check(lista):
    print("Check")

    claves_esperadas = ["name", "age", "birth_date", "programming_languages"]
    for claves in claves_esperadas:
        if claves not in claves_esperadas:
            print(f"Error: Falta la clave {claves}")
            return
    
    for key, value in lista.items():
        if key == "name" and not isinstance(value, str):
            print("Error: El nombre debe ser un string")

        if key == "age" and not isinstance(value, int):
            print("Error: La edad debe ser un entero")

        if key == "birth_date" and not isinstance(value, str):
            print("Error: La fecha de nacimiento debe ser un string")

        if key == "programming_languages" and not isinstance(value, list):
            print("Error: Los lenguajes de programación deben ser una lista de strings")
        elif key == "programming_languages":
            for lang in value:
                if not isinstance(lang, str):
                    print(f"Error: {lang} en 'programming_languages' debe ser un string")



class TestDiccionario(unittest.TestCase):
    
    def setUp(self):
        self.datos = {
            "usuario": "Juan Pérez",
            "edad": 30,
            "email": "juan@example.com",
            "intereses": ["Programación", "Música", "Deportes"]
        }

    def test_claves_existen(self):
        claves_esperadas = ["usuario", "edad", "email", "intereses"]
        
        for clave in claves_esperadas:
            self.assertIn(clave, self.datos, f"Falta la clave {clave} en el diccionario")

    def test_tipos_de_datos(self):
        self.assertIsInstance(self.datos["usuario"], str, "El usuario debe ser un string")
        self.assertIsInstance(self.datos["edad"], int, "La edad debe ser un número entero")
        self.assertIsInstance(self.datos["email"], str, "El email debe ser un string")
        self.assertIsInstance(self.datos["intereses"], list, "Los intereses deben ser una lista")

    def test_formato_email(self):
        self.assertIn("@", self.datos["email"], "El email debe contener '@'")

if __name__ == "__main__":
    unittest.main()


lista_check(lista)