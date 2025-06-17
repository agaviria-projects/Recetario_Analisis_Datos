"""
dax_medidas_tiempo.py
========================
📅 Funciones DAX para análisis temporal
Autor: Héctor Gaviria (Proyecto Power BI)
Descripción: Medidas DAX útiles para calcular ventas por mes, acumuladas, año anterior, etc.
"""

# 📆 Ventas del Mes Actual
# Mide las ventas del mes en curso usando la columna de fecha directamente
# Requiere que la tabla Ventas tenga una columna llamada 'fecha'

# DAX:
# Ventas Mes Actual =
# CALCULATE(
#     [Total Ventas],
#     MONTH(Ventas[fecha]) = MONTH(TODAY()) &&
#     YEAR(Ventas[fecha]) = YEAR(TODAY())
# )


# 📈 Ventas Acumuladas
# Suma acumulativa hasta la fecha seleccionada en el reporte

# DAX:
# Ventas Acumuladas =
# CALCULATE(
#     [Total Ventas],
#     FILTER(
#         ALL(Ventas[fecha]),
#         Ventas[fecha] <= MAX(Ventas[fecha])
#     )
# )


# 🔁 Ventas Año Anterior
# Requiere tener una tabla calendario conectada por la columna 'fecha'
#📌 Compara el valor actual con el mismo mes del año pasado.
# DAX:
# Ventas Año Anterior =
# CALCULATE(
#     [Total Ventas],
#     SAMEPERIODLASTYEAR('Calendario'[Date])
# )

#🟩 C. Variacion Anual % (crecimiento año a año)
#📌 Calcula el porcentaje de variación vs año anterior. Ideal para KPI o gráfico combinado.
#Variacion Anual % = 
#DIVIDE([TotalVentas] - [Ventas LY], [Ventas LY])

#🟧 D. Ventas Acumuladas YTD (Year to Date)
# 📌 Suma acumulada desde enero hasta la fecha seleccionada. Muy usada para dashboards financieros.
#Ventas YTD = 
# TOTALYTD([TotalVentas], Calendario[Date])


