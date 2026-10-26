nombre = input("¿Cómo te llamas? ")

while nombre.strip().lower() != "adrian":
    print("Nombre incorrecto, intenta de nuevo.")
    nombre = input("¿Cómo te llamas? ")

alumno = "Adrian"

nota1 = float(input("Escribe la nota 1: "))
nota2 = float(input("Escribe la nota 2: "))
nota3 = float(input("Escribe la nota 3: "))
nota4 = float(input("Escribe la nota 4: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

print("============ Promedio de Notas ============")
print(f"la nota 1 es: {nota1}")
print(f"la nota 2 es: {nota2}")
print(f"la nota 3 es: {nota3}")
print(f"la nota 4 es: {nota4}")
print(f"el promedio es: {promedio}")

if promedio >= 2.9:
    print(f"{alumno} aprobó con un promedio de {promedio}")
else:
    print(f"{alumno} desaprobó con un promedio de {promedio}")