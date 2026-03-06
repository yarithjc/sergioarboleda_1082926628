for multiplicador in range(1, 11):
    print(f"Tabla de multiplicar del {multiplicador}:")
    for multiplicando in range(1, 11):
        resultado = multiplicador * multiplicando
        print(f"{multiplicador} x {multiplicando} = {resultado}")
    print()  # Agrega una línea en blanco después de cada tabla