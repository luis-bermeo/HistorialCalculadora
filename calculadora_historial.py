# Versión 1: Solo la lógica básica de cálculo

num_a = float(input("Número 1: "))
num_b = float(input("Número 2: "))
op = input("Operación (+, -, *, /): ")

if op == "+":
    resultado = num_a + num_b
elif op == "-":
    resultado = num_a - num_b
elif op == "*":
    resultado = num_a * num_b
elif op == "/":
    resultado = num_a / num_b
else:
    resultado = "Operación no válida"

print(f"Resultado: {resultado}")