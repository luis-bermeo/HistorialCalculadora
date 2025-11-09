# Versión 4: Logica + Historial + Bucle + Ver historial

while True:
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

    with open("historial.txt", "a") as f:
        f.write(f"{num_a} {op} {num_b} = {resultado}\n")

    continuar = input("¿Quieres hacer otra operación? (s/n): ")
    if continuar.lower() != "s": # Sale del bucle si la respuesta no es 's' (sí)
        break # Detiene el bucle

    #Leer y mostrar el historial
    print("\nHistorial de operaciones:") # Título del historial
    with open("historial.txt", "r") as f: # Abre el archivo en modo "read"
        print(f.read()) # Imprime todo el contenido del archivo