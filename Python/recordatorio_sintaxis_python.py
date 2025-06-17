"""
📘 referencia_sintaxis_basica.py
Este archivo contiene ejemplos comentados sobre estructuras clave en Python:
- Tuplas ()
- Listas []
- Diccionarios {}
- Conjuntos
- pandas: para manipular y limpiar datos (el rey del análisis en Python)
- openpyxl: para leer/escribir archivos Excel .xlsx
"""

# --------------------------------
# 🔵 Paréntesis () - Tuplas y funciones
# --------------------------------

# ▶️ Llamar funciones
print("Hola mundo")  # Se usan paréntesis para pasar argumentos

# 🔒 Tupla: estructura ordenada e inmutable
mi_tupla = (10, 20, 30)
print("Tupla:", mi_tupla)

# --------------------------------
# 🟢 Corchetes [] - Listas y acceso
# --------------------------------

# 📝 Lista: colección ordenada y modificable
frutas = ["Manzana", "Banano", "Pera"]
frutas.append("Mango")  # Agregar elemento
print("Lista de frutas:", frutas)

# 🔍 Acceder a un elemento por índice
print("Primera fruta:", frutas[0])

# 📊 Uso en Pandas
# df["columna"]  → Accede a columna por nombre
# df.iloc[0]     → Accede por índice a una fila

# --------------------------------
# 🟠 Llaves {} - Diccionarios y sets
# --------------------------------

# 📖 Diccionario: clave → valor
persona = {"nombre": "Luis", "edad": 30}
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# 🧺 Conjunto: colección sin duplicados
mi_conjunto = {1, 2, 2, 3, 1}
print("Conjunto (sin duplicados):", mi_conjunto)

# --------------------------------
# 📌 Glosario rápido
# --------------------------------
# () → Tuplas o llamadas de funciones
# [] → Listas o selección en pandas
# {} → Diccionarios o conjuntos
# clave:valor → estructura de un diccionario

#Excel Viewer para VSCode
# Permite ver archivos .xlsx y .csv directamente dentro de VS Code
# sin tener que abrir Excel o LibreOffice. Ideal para:
# Validar qué contiene un archivo antes de procesarlo
# Comparar datos antes y después de la limpieza
# Trabajar más rápido sin salir del entorno de desarrollo