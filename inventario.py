# Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Solicitar el precio
precio = input("Ingrese el precio del producto: ")

# Validar que el precio sea un número
while not precio.replace('.', '', 1).isdigit():
    print("Error: el precio debe ser un número.")
    precio = input("Ingrese nuevamente el precio: ")

# Convertir el precio a decimal
precio = float(precio)

# Solicitar la cantidad
cantidad = input("Ingrese la cantidad del producto: ")

# Validar que la cantidad sea un número entero
while not cantidad.isdigit():
    print("Error: la cantidad debe ser un número entero.")
    cantidad = input("Ingrese nuevamente la cantidad: ")

# Convertir la cantidad a entero
cantidad = int(cantidad)

# Calcular el costo total
costo_total = precio * cantidad

# Mostrar resultados
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)

