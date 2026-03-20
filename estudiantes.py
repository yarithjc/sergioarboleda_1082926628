estudiantes = ["yarith","maria", "edwin"]

#agregar un nuevo estudiante al final
estudiantes.append("juan")
print(estudiantes) # ["yarith","maria", "edwin", "juan"]

#obtener la cantidad de estudiantes
print(len(estudiantes)) # 4

#buscar si un estudiante esta en la lista 
if "maria" in estudiantes:
    print("Maria está en la lista")
    
#eliminar un estudiante por nombre
estudiantes.remove("edwin")
print(estudiantes) # ["yarith","maria", "juan"]
