"""
referencia_conexion_excel.py
Plantilla de consulta y exportación a Excel con tabla estructurada.
"""

# 📦 Librerías necesarias
import mysql.connector
import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

# 🔌 1. Conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ventas_integrado"
)

# 🧾 2. Consulta con JOIN
consulta = """
SELECT
  v.id_ventas,
  c.nombre AS cliente,
  c.zona,
  p.nombre AS producto,
  p.categoria,
  v.fecha,
  v.cantidad,
  v.precio_unitario,
  (v.cantidad * v.precio_unitario) AS total_venta
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
JOIN productos p ON v.id_producto = p.id_producto
"""

# 🧮 3. Ejecutar la consulta y convertir a DataFrame
df = pd.read_sql(consulta, conexion)
print(df.head())  # Muestra para verificación

# 📤 4. Exportar a Excel
archivo_excel = "ventas_limpias.xlsx"
df.to_excel(archivo_excel, index=False)

# ✅ 5. Crear tabla estructurada automáticamente (versión optimizada)
def convertir_a_tabla_excel(ruta_archivo, nombre_tabla):
    wb = load_workbook(ruta_archivo)
    ws = wb.active

    max_row = ws.max_row
    max_col = ws.max_column
    col_final = chr(64 + max_col)  # Calcula la última columna (A, B, C...)

    rango = f"A1:{col_final}{max_row}"  # Define el rango A1:col_final
    tabla = Table(displayName=nombre_tabla, ref=rango)
    estilo = TableStyleInfo(name="TableStyleMedium9", showRowStripes=True)
    tabla.tableStyleInfo = estilo
    ws.add_table(tabla)

    wb.save(ruta_archivo)
    print(f"✅ Tabla '{nombre_tabla}' creada en {ruta_archivo}")

# Llamar la función
convertir_a_tabla_excel(archivo_excel, "VentasTabla")

# 🔒 6. Cerrar la conexión
conexion.close()
