import re

def validar_cedula(cedula):
    if cedula.isdigit() and 8 <= len(cedula) <= 10:
        return True
    return False

def validar_email(email):
    if re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        return True
    return False

def validar_calificaciones(calificaciones):
    try:
        for cal in calificaciones:
            if not (0 <= float(cal) <= 5):
                return False
        return True
    except ValueError:
        return False

def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 2)

def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"

def crear_estudiante(cedula, nombre, email, calificaciones):
    if not validar_cedula(cedula):
        return None
    if not validar_email(email):
        return None
    if not validar_calificaciones(calificaciones):
        return None
    promedio = calcular_promedio(calificaciones)
    return {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio,
        "desempeño": clasificar_desempeño(promedio)
    }

def listar_estudiantes(estudiantes):
    print("Cédula    | Nombre        | Promedio | Desempeño")
    print("-" * 50)
    for est in estudiantes:
        print(f"{est['cedula']:<10} | {est['nombre']:<13} | {est['promedio']:<8} | {est['desempeño']}")

def main():
    estudiantes = []
    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            cal_str = input("Calificaciones (separadas por coma): ")
            calificaciones = [float(c.strip()) for c in cal_str.split(',')]
            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)
            if estudiante:
                estudiantes.append(estudiante)
                print(f"Estudiante agregado exitosamente. Promedio: {estudiante['promedio']} | Desempeño: {estudiante['desempeño']}")
            else:
                print("Datos inválidos. No se pudo agregar el estudiante.")
        elif opcion == "2":
            if estudiantes:
                listar_estudiantes(estudiantes)
            else:
                print("No hay estudiantes registrados.")
        elif opcion == "3":
            cedula_buscar = input("Cédula a buscar: ")
            encontrado = False
            for est in estudiantes:
                if est['cedula'] == cedula_buscar:
                    print(f"{est['nombre']} | Promedio: {est['promedio']} | Desempeño: {est['desempeño']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Estudiante no encontrado.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
