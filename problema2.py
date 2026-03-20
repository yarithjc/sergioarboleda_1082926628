def agregar_producto(inventario):
    nombre = input("Ingresa el nombre del producto: ").strip()
    if nombre in inventario:
        print("El producto ya existe.")
        return
    try:
        cantidad = int(input("Ingresa la cantidad: "))
        precio = float(input("Ingresa el precio: "))
        if cantidad <= 0 or precio <= 0:
            print("Cantidad y precio deben ser positivos.")
            return
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print("Producto agregado.")
    except ValueError:
        print("Entrada inválida.")

def ver_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    print("Inventario:")
    for nombre, datos in inventario.items():
        total = datos["cantidad"] * datos["precio"]
        print(f"{nombre}: Cantidad {datos['cantidad']}, Precio {datos['precio']:.2f}, Total {total:.2f}")

def buscar_producto(inventario, nombre):
    if nombre in inventario:
        datos = inventario[nombre]
        total = datos["cantidad"] * datos["precio"]
        print(f"Producto encontrado: {nombre}, Cantidad {datos['cantidad']}, Precio {datos['precio']:.2f}, Total {total:.2f}")
    else:
        print("Producto no encontrado.")

def actualizar_cantidad(inventario, nombre):
    if nombre not in inventario:
        print("Producto no encontrado.")
        return
    try:
        nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
        if nueva_cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        inventario[nombre]["cantidad"] = nueva_cantidad
        print("Cantidad actualizada.")
    except ValueError:
        print("Entrada inválida.")

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def menu():
    inventario = {}
    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            ver_inventario(inventario)
        elif opcion == "3":
            nombre = input("Ingresa el nombre del producto: ").strip()
            buscar_producto(inventario, nombre)
        elif opcion == "4":
            nombre = input("Ingresa el nombre del producto: ").strip()
            actualizar_cantidad(inventario, nombre)
        elif opcion == "5":
            nombre = input("Ingresa el nombre del producto: ").strip()
            eliminar_producto(inventario, nombre)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()