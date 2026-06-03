# Proyecto: Calculadora Colaborativa en Python

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir para cero"
    return a / b

print("--- CALCULADORA OFICIAL DE GRUPO (ESTUDIANTE A Y B) ---")

print(f"Suma de 5 + 3 = {sumar(5, 3)}")
print(f"Resta de 10 - 4 = {restar(10, 4)}")
print(f"Multiplicación de 4 * 3 = {multiplicar(4, 3)}")
print(f"División de 20 / 5 = {dividir(20, 5)}")
print(f"División de 10 / 0 = {dividir(10, 0)}")