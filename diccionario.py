persona={"Nombre": "Yarith", "Edad": 17, "Ciudad": "Santa Marta"}

#iterar sobre claves
for clave in persona: 
    print(clave)
    
#iterar sobre pares clave-valor
for clave, valor in persona.items():
    print(clave + ": " + str(valor))