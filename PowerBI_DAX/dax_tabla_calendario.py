"""
dax_tabla_calendario.py
==================================
📅 Script DAX para crear tabla calendario en Power BI
Autor: Héctor Gaviria
Uso: Ideal para usar con medidas DAX que requieren contexto temporal.
"""

# --------------------------------------------
# 🧱 Crear tabla calendario con DAX (auto rango)
# --------------------------------------------

# DAX:
# Calendario = CALENDAR(MIN(Ventas[fecha]), MAX(Ventas[fecha]))

# --------------------------------------------
# 🧩 Agregar columnas útiles (opcional)
# --------------------------------------------

# Año = YEAR('Calendario'[Date])
# Mes = FORMAT('Calendario'[Date], "MMMM")
# AñoMes = FORMAT('Calendario'[Date], "YYYY-MM")
# Día = DAY('Calendario'[Date])
# DíaSemana = FORMAT('Calendario'[Date], "dddd")
# Trimestre = "Q" & FORMAT('Calendario'[Date], "Q")

# --------------------------------------------
# 🧪 Medidas que usan la tabla calendario
# --------------------------------------------

# Total Ventas Año Actual (versión simple, suficiente para dashboards básicos)
# CALCULATE([Total Ventas], YEAR('Calendario'[Date]) = YEAR(TODAY()))

# Total Ventas Año Anterior =
# CALCULATE([Total Ventas], SAMEPERIODLASTYEAR('Calendario'[Date]))

# Total Ventas Acumuladas Año =
# TOTALYTD([Total Ventas], 'Calendario'[Date])

# Total Ventas Año Actual (versión robusta usando FILTER + ALL)
# CALCULATE(
#     [Total Ventas],
#     FILTER(ALL('Calendario'), YEAR('Calendario'[Date]) = YEAR(TODAY()))
# )

# --------------------------------------------
# 🔗 Recuerda: Relacionar 'Calendario'[Date] con Ventas[fecha]
# Tipo de relación: 1 a muchos, simple, activa.
