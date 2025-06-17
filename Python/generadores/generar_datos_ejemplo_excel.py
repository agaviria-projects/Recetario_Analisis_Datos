import pandas as pd

# Tabla de hechos: VENTAS
ventas = pd.DataFrame({
    'id_venta': range(1, 11),
    'id_cliente': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'id_producto': [101, 102, 103, 104, 105, 101, 102, 103, 104, 105],
    'cantidad': [2, 1, 3, 1, 2, 1, 2, 1, 3, 2],
    'precio_unitario': [5000, 7000, 10000, 6000, 8000, 5000, 7000, 10000, 6000, 8000]
})
ventas['total'] = ventas['cantidad'] * ventas['precio_unitario']

# Dimensión CLIENTES
clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5],
    'nombre_cliente': ['Ana', 'Luis', 'Carlos', 'Marta', 'Julia'],
    'ciudad': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena']
})

# Dimensión PRODUCTOS
productos = pd.DataFrame({
    'id_producto': [101, 102, 103, 104, 105],
    'nombre_producto': ['Mouse', 'Teclado', 'Monitor', 'Webcam', 'Impresora'],
    'categoria': ['Accesorio', 'Accesorio', 'Pantalla', 'Accesorio', 'Oficina']
})

# Guardar en archivo Excel con varias hojas
with pd.ExcelWriter('datos_ejemplo.xlsx', engine='openpyxl') as writer:
    ventas.to_excel(writer, sheet_name='ventas', index=False)
    clientes.to_excel(writer, sheet_name='clientes', index=False)
    productos.to_excel(writer, sheet_name='productos', index=False)

print("✅ Archivo 'datos_ejemplo.xlsx' creado con éxito.")
