# ==========================================
# Archivo: dax_medidas_basicas.py
# Autor: Héctor Gaviria (Proyecto Power BI)
# Descripción: Medidas DAX usadas en análisis de ventas
# ==========================================

"""
💡 Total de Ventas
TotalVentas = SUMX(Ventas, Ventas[cantidad] * Ventas[precio_unitario])

📌 Se calcula fila por fila y suma: ideal para ventas reales.
"""

""""
Suma el total de una columna si ya existe
"""
# DAX
# Total Ventas = SUM(Ventas[total])

"""
💡 Total Productos Vendidos
Suma total de la cantidad de productos vendidos
"""
# DAX
# Total Productos = SUM(Ventas[cantidad])

"""
💡 Clientes Únicos
Cantidad de clientes distintos que han realizado compras
"""
# DAX
# Clientes Únicos = DISTINCTCOUNT(Ventas[id_cliente])

"""
💡 Promedio por Cliente
Promedio del valor total de ventas dividido entre clientes únicos
"""
# DAX
# Promedio x Cliente = DIVIDE([Total Ventas], [Clientes Únicos])

"""
💡 Total Ventas por Categoría (no requiere medida)
Usar visualización con:
Eje: Productos[categoria]
Valor: [Total Ventas]
"""

"""
🗓️ Ventas del Mes Actual
Suma total de ventas solo del mes actual (basado en la columna de fecha)
"""
# DAX
# Ventas Mes Actual =
# CALCULATE(
#     [Total Ventas],
#     MONTH(Ventas[fecha]) = MONTH(TODAY()) &&
#     YEAR(Ventas[fecha]) = YEAR(TODAY())
# )

"""
🧾 Ticket Promedio por Venta
Promedio del campo total en la tabla de ventas
"""
# DAX
# Ticket Promedio = AVERAGE(Ventas[total])

"""
🧮 Cantidad de Ventas Realizadas
Conteo de filas en la tabla de ventas
"""
# DAX
# Total Ventas Realizadas = COUNTROWS(Ventas)

"""
📊 Ventas Acumuladas (Running Total)
Ventas acumuladas por fecha (ideal para gráficos de línea)
"""
# DAX
# Ventas Acumuladas =
# CALCULATE(
#     [Total Ventas],
#     FILTER(
#         ALL(Ventas[fecha]),
#         Ventas[fecha] <= MAX(Ventas[fecha])
#     )
# )

"""
✅ 1. Medida DAX: Total de entregas 
Total Entregas = COUNTROWS(VentasTabla)
📌 Esta medida cuenta cuántos registros hay (1 por pedido → 1 entrega).
"""


# CLAVE: Entender cómo usar tablas de hechos vs dimensiones en las visualizaciones
#📦 Tabla de Hechos = métricas / cantidades / valores
#→ Ejemplo: ventas[cantidad], ventas[precio_unitario], TotalVentas (DAX)

#📋 Tablas de Dimensiones = descripciones / categorías / filtros
#→ Ejemplo: clientes[ciudad], productos[nombre], calendario[AñoMes]

#✅ ¿Cómo se usan en las visualizaciones?
# Parte del gráfico	        ¿Qué poner?	                ¿De qué tabla viene?
# Eje X / Segmento      	Categorías o fechas    	    Dimensiones (clientes, productos, calendario)
# Valores	                Sumas, totales, medidas	    Hechos (ventas, DAX)
# Filtros                   Ciudades, productos,fechas	Dimensiones

#Regla de oro:✅ "Las dimensiones filtran o agrupan las métricas de la tabla de hechos."

#   Elemento	                        Ubicación en visualización	        ¿Qué tipo de tabla es?	    ¿Por qué?
# 🧠 Tabla de dimensión   
# (cliente, producto, zona, fecha)	    EJE (o FILTRO/SLICER)	                DIMENSIÓN	            Son descripciones o categorías para agrupar
# 📦 Tabla de hechos     
# (envíos, ventas, cantidades)          VALOR (suma, conteo, promedio)      	HECHOS	                Son los números que se agregan