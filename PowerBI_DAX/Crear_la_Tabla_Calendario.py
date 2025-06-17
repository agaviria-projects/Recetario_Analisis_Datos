# ✅ Recomendado por buenas prácticas:
# - En Power BI - Modelado - Nueva Tabla
# - Tabla calendario explícita (no usar auto-calendario)
# - Permite usar funciones DAX de inteligencia de tiempo correctamente
# - Puede expandirse con: DíaSemana, NombreDía, Trimestre, etc.

# Calendario = 
# ADDCOLUMNS(
#     CALENDAR(DATE(2024,1,1), DATE(2025,12,31)),
#     "Año", YEAR([Date]),
#     "Mes", MONTH([Date]),
#     "NombreMes", FORMAT([Date], "MMMM"),
#     "MesNumero", FORMAT([Date], "MM"),
#     "AñoMes", FORMAT([Date], "YYYY-MM"),
#     "NombreDia", FORMAT([Date], "dddd"),
#     "NumeroDiaSemana", WEEKDAY([Date], 2),
#     "Trimestre", "Q" & FORMAT([Date], "Q")
# )
#Relacionar con ventas
#Calendario[Date] → ventas[fecha]
