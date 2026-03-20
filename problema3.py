def contar_caracteres(texto):
    return len(texto)

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def contar_oraciones(texto):
    oraciones = [s.strip() for s in texto.replace('!', '.').replace('?', '.').split('.') if s.strip()]
    return len(oraciones)

def palabra_mas_larga(texto):
    palabras = texto.split()
    if not palabras:
        return ""
    return max(palabras, key=len)

def palabra_mas_corta(texto):
    palabras = texto.split()
    if not palabras:
        return ""
    return min(palabras, key=len)

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    return sum(1 for c in texto if c in vocales)

def contar_consonantes(texto):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for c in texto if c in consonantes)

def main():
    texto = input("Ingresa un texto para analizar: ").strip()
    if not texto:
        print("El texto no puede estar vacío.")
        return
    
    print("\nEstadísticas del texto:")
    print(f"Total de caracteres: {contar_caracteres(texto)}")
    print(f"Total de palabras: {contar_palabras(texto)}")
    print(f"Total de oraciones: {contar_oraciones(texto)}")
    print(f"Palabra más larga: '{palabra_mas_larga(texto)}'")
    print(f"Palabra más corta: '{palabra_mas_corta(texto)}'")
    print(f"Número de vocales: {contar_vocales(texto)}")
    print(f"Número de consonantes: {contar_consonantes(texto)}")

if __name__ == "__main__":
    main()