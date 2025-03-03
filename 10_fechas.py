from datetime import datetime

new_date = datetime(1997, 4, 3, 3, 45, 0)

# Formatos de fecha
format1 = new_date.strftime("%Y-%m-%d %H:%M:%S")
format2 = new_date.strftime("%d/%m/%Y")
format3 = new_date.strftime("%B %d, %Y")
format4 = new_date.strftime("%I:%M %p")
format5 = new_date.strftime("%A, %d %B %Y")

print(f"Formato 1: {format1}")
print(f"Formato 2: {format2}")
print(f"Formato 3: {format3}")
print(f"Formato 4: {format4}")
print(f"Formato 5: {format5}")