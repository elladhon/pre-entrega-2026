
productos = []

while True:
    print("="*40)
    print ("Sistema de gestión de productos")
    print("="*40)
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        nombre_producto = input("Ingrese el nombre del producto: ").strip()
        if nombre_producto == "":
            print("El nombre del producto no puede estar vacío. Intente nuevamente.")
            continue
    
        categoria = input("Ingrese la categoría de productos a mostrar: ").strip()
        if categoria == "":
            print("La categoría no puede estar vacía. Intente nuevamente.")
            continue

        precio_str = input("Ingrese el precio del producto sin centavos: ").strip()
        if not precio_str.isdigit():
            print("El precio debe ser un número. Intente nuevamente.")
            continue
        precio = int(precio_str)

        datos = [nombre_producto.capitalize(), categoria.capitalize(), precio]
        productos.append(datos)
        print(f"Producto '{nombre_producto}' agregado exitosamente.")
        
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos para mostrar.\n\n")
            continue
        else:
            print("\nLista de productos:")
            for i in range(len(productos)):
                print(f"ID:{i+1}\n - Nombre: {productos[i][0]}\n - Categoría: {productos[i][1]}\n - Precio: ${productos[i][2]}")

    elif opcion == "3":
        if len(productos) == 0:
            print("No hay productos para buscar.\n\n")
            continue
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
        encontrado = False
        for i in range(len(productos)):
            if productos[i][0].lower() == nombre_buscar.lower():
                print(f"Producto encontrado - ID:{i+1}\n - Nombre: {productos[i][0]}\n - Categoría: {productos[i][1]}\n - Precio: ${productos[i][2]}")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el producto '{nombre_buscar}'.\n\n")

    elif opcion == "4":
        if len(productos) == 0:
            print("No hay productos para eliminar.\n\n")
            continue
        nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip()
        eliminado = False
        for i in range(len(productos)):
            if productos[i][0].lower() == nombre_eliminar.lower():
                productos.pop(i)
                print(f"Producto '{nombre_eliminar}' eliminado exitosamente.")
                eliminado = True
                break
        if not eliminado:
            print(f"No se encontró el producto '{nombre_eliminar}' para eliminar.\n\n")
    elif opcion == "5":
        print("Saliendo del sistema de gestión de productos.")
        break
    else:
        print("Opción inválida. Ingrese un número entre 1 y 5.")