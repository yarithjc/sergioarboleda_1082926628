# Sistema de registro de estudiantes

estudiantes = []

for i in range(5):
    while True:
        nombre = input(f"Nombre del estudiante {i+1}: ")
        try:
            edad = int(input("Edad: "))
            calificacion = float(input("Calificación: "))
            if 5 <= edad <= 100 and 0 <= calificacion <= 5:
                estudiantes.append({'nombre': nombre, 'edad': edad, 'calificacion': calificacion})
                break
            else:
                print("Datos inválidos. La edad debe estar entre 5 y 100, y la calificación entre 0 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa números válidos para edad y calificación.")

# Calcular estadísticas
if estudiantes:
    estudiante_max = max(estudiantes, key=lambda e: e['calificacion'])
    estudiante_min = min(estudiantes, key=lambda e: e['calificacion'])
    promedio = sum(e['calificacion'] for e in estudiantes) / len(estudiantes)

    print("\nEstudiante con la calificación más alta:")
    print(f"Nombre: {estudiante_max['nombre']}, Edad: {estudiante_max['edad']}, Calificación: {estudiante_max['calificacion']}")

    print("\nEstudiante con la calificación más baja:")
    print(f"Nombre: {estudiante_min['nombre']}, Edad: {estudiante_min['edad']}, Calificación: {estudiante_min['calificacion']}")

    print(f"\nCalificación promedio de todos: {promedio:.2f}")
