🧠 RUTA 1 – PYTHON (desde cero, con lógica)
Etapa	Tema	Enfoque lógico
✅ 1	Variables, tipos de datos	Qué es una variable, cómo la usamos en la vida real
✅ 2	Condicionales (if, else)	Cómo tomar decisiones automáticas
✅ 3	Ciclos (for, while)	Repetir tareas como un robot
✅ 4	Listas, tuplas, diccionarios	Cómo guardar y buscar información
✅ 5	Funciones propias	Reutilizar código como en una calculadora
✅ 6	Librerías (pandas)	Limpiar archivos como si fueras un filtro de Excel
✅ 7	Proyecto mini: limpieza real	Aplicar toda la lógica aprendida

# 1. Una variable en programación es como una caja con nombre donde guardas un valor que puede cambiar.
# 👉 Cómo declarar una variable
nombre = "Juan"         # str
edad = 28               # int
precio = 19.99          # float
es_activo = True        # bool
sin_dato = None         # NoneType

# 👉 Saber el tipo
print(type(precio))

= no significa "igual", sino asignación.
Es decir: "guarda este valor en esta variable".

# 2.condicional Es una instrucción que dice:"Si algo es verdadero, haz esto. Si no, haz otra cosa."
# 👉 Condicionales en Python
if edad >= 18:
    print("Adulto")
else:
    print("Menor")

# 👉 Condición múltiple
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

Operador	Significado
==	        Igual a
!=	        Distinto de
>	        Mayor que
<	        Menor que
>=	        Mayor o igual que
<=	        Menor o igual que

# operadores 
AND : Debe cumplir todas las condiciones
OR : Una de las dos condiciones se debe cumplir

# 3.Ciclos: Un ciclo o bucle sirve para ejecutar una acción una y otra vez, mientras se cumpla una condición o se recorra una lista.

🧠 Ejemplo de la vida real:

    Revisar cada cliente de una lista.

    Calcular el IVA para cada producto.

    Limpiar cada fila de un archivo.

# Ciclo for –  recorre cada elemento de una lista, uno por uno.
frutas = ["manzana", "pera", "banana"]

for fruta in frutas:
    print("🍎 Fruta:", fruta)

Para cada elemento dentro de la lista frutas, llama a ese elemento fruta, y haz lo siguiente..."

# Ciclo while – repite mientras una condición se cumpla.
contador = 1

while contador <= 5:
    print("🔁 Repetición:", contador)
    contador += 1

# for es ideal para recorrer listas, tuplas, diccionarios.
# while es útil cuando no sabes cuántas veces se repetirá algo.

# 👉 Recorrer una lista con for
# 👉 for con variable temporal color
colores = ["Rojo", "Verde", "Azul"]

for color in colores:
    print("El color es:", color)

# 👉 Usar range
for i in range(1, 6):
    print("Número:", i)

# 👉 Bucle while
x = 0
while x < 3:
    print("Intento:", x)
    x += 1

# 4.Listas, Tuplas y Diccionarios
Estructura	    ¿Qué es?    	¿Para qué sirve?    	            ¿Se puede modificar?
list	        Lista	        Almacenar varios datos en orden 	✅ Sí
tuple	        Tupla	        Como lista, pero protegida	        ❌ No
dict	        Diccionario 	Almacenar datos con clave → valor	✅ Sí    

#  LISTAS – list
Es como una caja ordenada con varios compartimentos.
frutas = ["manzana", "pera", "banana"]

print(frutas[0])  # "manzana"
print(len(frutas))  # 3

frutas.append("kiwi")  # Agregar al final
frutas.remove("pera")  # Quitar un elemento

# La función len() devuelve la longitud (cantidad de elementos) de una estructura:
esta diciendo: Esa lista llamada frutas tiene 3 elementos.

# TUPLAS – tuple
 Son como las listas, pero no se pueden modificar.
 coordenadas = (10, 20)

print(coordenadas[1])  # 20
# coordenadas[0] = 5 ❌ Esto da error: las tuplas no se modifican

💡 Se usan cuando no quieres que los datos se cambien por accidente.

# DICCIONARIOS – dict
 Guardan información con clave → valor. Muy útil para datos de personas, productos, API, JSON, etc.

cliente = {
    "nombre": "Héctor",
    "edad": 35,
    "ciudad": "Medellín"
}

print(cliente["nombre"])  # Héctor

cliente["ocupacion"] = "Analista"  # Agregar nuevo campo
cliente["edad"] = 36  # Modificar valor

Las listas son muy usadas en pandas (df["columna"].tolist()).
Las tuplas se usan cuando debes proteger el orden (fechas, coordenadas).
Los diccionarios son base de casi todo en programación moderna: APIs, archivos JSON, incluso respuestas de bases de datos.

# 👉 Listas
colores = ["rojo", "verde", "azul"]
colores.append("amarillo")
print(colores[1])  # verde

# 👉 Tuplas
dias = ("lunes", "martes", "miércoles")

# 👉 Diccionarios
persona = {"nombre": "Carlos", "edad": 40}
persona["edad"] = 41

# 5.Funciones en Python
Una función es un bloque de código que se puede reutilizar para hacer una tarea específica.
es como una calculadora personalizada: tú le das unos datos (entradas), y te devuelve un resultado (salida).
# ✅ Sintaxis básica
def nombre_de_la_funcion(parametros):
    # instrucciones
    return resultado

# Ejemplo
def saludar(nombre):
    return f"Hola, {nombre}!"

mensaje = saludar("Héctor")
print(mensaje)

# Aquí:
    saludar es el nombre de la función.
    "Héctor" es el parámetro.
    return envía de vuelta el resultado.

#  Función sin parámetros
def mostrar_mensaje():
    print("📢 ¡Bienvenido al curso de Python!")

mostrar_mensaje()  # Llamada a la función

# 🧮 Función con cálculo
def calcular_iva(precio, tasa=0.19):
    return precio * (1 + tasa)

total = calcular_iva(100000)
print("💰 Precio con IVA:", total)
✅ Puedes usar parámetros por defecto, como tasa=0.19

Las funciones evitan repetir código y ayudan a organizar mejor los scripts.
Piensa en ellas como acciones reutilizables: limpiar, calcular, validar, convertir.

# 👉 Crear función simple
def saludar(nombre):
    return "Hola, " + nombre

# 👉 Función con cálculo
def calcular_descuento(precio, porcentaje):
    return precio * (1 - porcentaje / 100)

# 6. Librerías en Python (import, pandas, etc.)
¿Qué es una librería?
Una librería es un conjunto de funciones ya creadas por otros desarrolladores para que tú no tengas que programar todo desde cero.
Por ejemplo: en vez de crear tu propia función para leer Excel, usas pandas.read_excel() que ya lo hace por ti.

# ¿Cómo se importa una librería?
import pandas as pd

pandas es la librería.
pd es un alias para escribir menos cada vez que la usas.

# ¿Qué hace pandas?
pandas es la librería más usada para análisis de datos. Sirve para:
Acción	                        Función en pandas
Leer archivos Excel	            pd.read_excel()
Leer CSV	                    pd.read_csv()
Limpiar datos	                .dropna(), .fillna(), etc.
Filtrar datos	                df[df["col"] > 1000]
Agrupar y resumir	            df.groupby()
Exportar archivos	            df.to_excel()

import pandas as pd

# Leer archivo
df = pd.read_excel("ventas.xlsx")

# Mostrar las primeras filas
print(df.head())

# Ver estructura
print(df.info())

# Eliminar nulos
df.dropna(inplace=True)

# ¿Qué es un DataFrame?
Un DataFrame es como una tabla de Excel pero en código.

print(type(df))  # <class 'pandas.core.frame.DataFrame'>

# 🛠 Otras librerías útiles que veremos luego
Librería	            Para qué sirve
openpyxl	            Trabajar con Excel desde Python
matplotlib	            Graficar datos
mysql.connector	        Conectar Python con MySQL
datetime	            Manejar fechas

# Proyecto analisis_entregas.py
Objetivo: Limpiar y analizar entregas usando Python, desde cero.

# ✅ PASO 1: Leer el archivo en un DataFrame
¿Por qué?
Primero necesitas importar pandas y cargar el archivo para poder examinar los datos.

 Lógica:
        Importar la librería pandas.
        Leer el archivo con pd.read_excel().
        Mostrar las primeras filas con .head() para analizar los errores visualmente.

# Importar la libreria
 import pandas as pd

# Leer archivo con errores
df = pd.read_excel("entregas_sucias.xlsx")

# Mostrar primeras filas para análisis inicial
print(df.head())  

# 🧠 ¿Qué debes observar?
¿Hay campos vacíos?
¿Fechas mal escritas?
¿Tipos de datos incorrectos?
¿Texto donde debería ir un número?

# ✅ PASO 2: Eliminar registros vacíos
📌 ¿Por qué?
Si falta un dato esencial (como cliente o fecha_entrega), ese registro no se puede analizar.

# 🧠 Lógica:
Usamos dropna() con la opción subset para eliminar solo si esas columnas están vacías.

# Eliminar registros donde cliente o fecha estén vacíos
df.dropna(subset=["cliente", "fecha_entrega"], inplace=True)

# Verificamos el resultado
print("✅ Después de eliminar vacíos importantes:")
print(df)

# ✅ PASO 3: Convertir columna cantidad a número
📌 ¿Por qué?
Hay valores no numéricos como "uno" que causarán errores si intentas multiplicar o analizar.

# 🧠 Lógica:
Usamos pd.to_numeric() para convertir a número.
Usamos errors="coerce" para que si hay un texto raro, lo reemplace con NaN.

# Convertir columna 'cantidad' a número
df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")

# Mostrar para verificar si hay errores convertidos en NaN
print("✅ Después de convertir cantidades:")
print(df)

# ✅ PASO 4: Eliminar filas con cantidad vacía o igual a 0
📌 ¿Por qué?
Si la cantidad quedó como NaN (por ejemplo "uno"), no es válida.
Si la cantidad es 0, no tiene sentido analizar esa entrega (no hubo productos entregados).

# 🧠 Lógica:
Primero eliminamos filas donde cantidad está vacía (NaN).
Luego eliminamos filas donde cantidad == 0.

# Eliminar registros donde cantidad sea NaN
df.dropna(subset=["cantidad"], inplace=True)

# Eliminar registros donde cantidad sea 0
df = df[df["cantidad"] > 0]

# Verificamos el resultado
print("✅ Después de eliminar cantidades inválidas o cero:")
print(df)

# ✅ PASO 5: Arreglar la columna fecha_entrega
📌 ¿Por qué?
Las fechas están en diferentes formatos como "2023/10/01", "01-11-2023", "15 octubre 2023".
Debemos convertirlas todas al tipo de dato datetime.

# 🧠 Lógica:
Usamos pd.to_datetime() para que Python interprete todas las fechas correctamente.
Si alguna fecha es inválida, se convierte en NaT (nulo de tipo fecha).
Después eliminamos esas fechas inválidas.

# Convertir columna de fecha al tipo datetime
df["fecha_entrega"] = pd.to_datetime(df["fecha_entrega"], errors="coerce")

# Eliminar fechas inválidas (NaT)
df.dropna(subset=["fecha_entrega"], inplace=True)

# Verificar formato unificado
print("✅ Después de limpiar fechas:")
print(df)

# ✅ PASO 6: Crear columna estado_entrega
📌 ¿Por qué?
Queremos saber si la entrega fue a tiempo o con retraso, usando la columna dias_retraso.

# 🧠 Lógica:
Si dias_retraso > 0 → "Retrasado"
Si dias_retraso <= 0 → "A tiempo"
Usaremos .apply() con una función para recorrer la columna y asignar el valor adecuado.
# Función para clasificar el estado de entrega
def clasificar_entrega(dias):
    if dias > 0:
        return "Retrasado"
    else:
        return "A tiempo"

# Crear columna nueva usando apply
df["estado_entrega"] = df["dias_retraso"].apply(clasificar_entrega)

# Verificar resultado
print("✅ Estado de entrega agregado:")
print(df)

# ✅ PASO 7: Calcular total_entregado y exportar archivo limpio
📦 Lógica:
Como no tenemos precio_unitario, crearemos una columna total_entregado igual a la cantidad entregada, útil si luego cruzas con otra tabla de productos.    Luego exportamos el archivo limpio con to_excel().

# Crear columna total entregado
df["total_entregado"] = df["cantidad"]  # opcional si luego multiplicas por precio

# Exportar archivo limpio
df.to_excel("entregas_limpias.xlsx", index=False)

print("✅ Archivo limpio exportado correctamente.")
