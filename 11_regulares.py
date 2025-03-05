import re

regex_email = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'
regex_telefono = r'^\+?\d{1,3}?[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}$'
regex_url = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(:\d{2,5})?(\/\S*)?$'


def validar(cadena, regex):
    return bool(re.match(regex, cadena))

print(validar("correo@example.com", regex_email))
print(validar("123-456-7890", regex_telefono))
print(validar("https://example.com", regex_url))  # ✅ True
