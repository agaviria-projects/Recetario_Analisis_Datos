"""
referencia_limpieza.py
Archivo de consulta rápida para limpieza de datos con pandas
"""

import pandas as pd

# 1. Cargar archivos Excel
archivo = "datos.xlsx"
df = pd.read_excel(archivo, sheet_name="Hoja1")

# 2. Ver primeros datos
print(df.head())

# 3. Eliminar duplicados
# Elimina filas duplicadas basadas en todas las columnas
df.drop_duplicates(inplace=True)

# Elimina duplicados basados en una columna clave
df.drop_duplicates(subset=["id"], inplace=True)

# 4. Eliminar filas con valores nulos en una columna específica
df.dropna(subset=["nombre"], inplace=True)

# 5. Rellenar valores nulos con texto o número
df["nombre"] = df["nombre"].fillna("Sin nombre")
df["edad"] = df["edad"].fillna(0)

# 6. Convertir columna de texto a fecha
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

# 7. Reemplazar valores específicos
df["ciudad"] = df["ciudad"].replace("Medellin", "MEDELLÍN")

# 8. Cambiar tipo de dato
df["edad"] = df["edad"].astype(int)

# 9. Exportar a Excel
df.to_excel("archivo_limpio.xlsx", index=False)

## 10. Cargar el archivo Excel cuando contiene 3 hojas en un libro
archivo = 'datos_ejemplo.xlsx'
ventas = pd.read_excel(archivo, sheet_name='ventas')
clientes=pd.read_excel(archivo,sheet_name='clientes')
productos=pd.read_excel(archivo,sheet_name='productos')

# 11. Limpiezas básicas
# Eliminar nulos si los hay
ventas.dropna(inplace=True)
clientes.dropna(inplace=True)
productos.dropna(inplace=True)

# 12. Quitar espacios por si hay errores de digitación
clientes["nombre_cliente"] = clientes["nombre_cliente"].str.strip()
productos["categoria"] = productos["categoria"].str.strip()

# Verificación rápida
print("Ventas:")
print(ventas.head())
print("\nClientes:")
print(clientes.head())
print("\nProductos:")
print(productos.head())

# 13. Guardar cada tabla en su propio archivo
ventas.to_excel('ventas_limpias.xlsx', index=False)
clientes.to_excel('clientes_limpios.xlsx', index=False)
productos.to_excel('productos_limpios.xlsx', index=False)

# 14. Renombrar columna mal escrita
df.rename(columns={"mbre clien": "Nombre cliente"}, inplace=True)

#15. Normalizar mayúsculas/minúsculas
df['Categoria'] = df['Categoria'].str.title()    # Hombre, Mujer...
df['Ciudad'] = df['Ciudad'].str.capitalize()     # Medellin, Bogotá...

#16. Eliminar filas completamente vacias
df.dropna(how='all', inplace=True)

print("✅ Limpieza de datos completada.")

# 🧼 Buenas prácticas de limpieza
#1. Normalizar y estructurar primero (espacios, formato, fechas)

#2. Eliminar duplicados clave ANTES de eliminar nulos
#df.drop_duplicates(subset=['Nombre cliente', 'Categoria'], keep='first', inplace=True)

#3. Luego sí eliminar nulos en columnas críticas (fechas, cantidades, precios)
#df.dropna(subset=['Fecha compra', 'Cantidad', 'Precio Unitario'], inplace=True)