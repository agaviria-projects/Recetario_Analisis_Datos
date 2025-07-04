# 🎯 LOOKUPVALUE en DAX – Equivalente a BUSCARV en Excel

## ✅ ¿Qué hace LOOKUPVALUE?
"""
`LOOKUPVALUE` devuelve el **valor de una columna de otra tabla** cuando **se cumple una condición de coincidencia**.

Es el equivalente a:

🟩 `BUSCARV` en Excel  
🟦 `JOIN` manual entre dos tablas de hechos

"""
## 🧠 Sintaxis general

"""
```DAX
LOOKUPVALUE(
    <columna_que_quieres_traer>,
    <columna_donde_buscar>,
    <valor_que_comparar>
)
"""

##. % Participación por producto
"""
Porcentaje por Producto = 
DIVIDE([Total Ventas], CALCULATE([Total Ventas], ALL(productos)))
"""
##🧠 Esto responde: ¿cuánto representa este producto sobre el total?

## Total ventas solo productos tipo bebida
"""
Ventas Bebidas = 
CALCULATE(
    [Total Ventas],
    productos[categoria] = "Bebida caliente"
)
"""
##🔎 Esto aplica filtro interno a la medida.

## Ventas válidas (cantidad no nula)
"""
Ventas Validadas = 
CALCULATE([Total Ventas], NOT(ISBLANK(ventas[cantidad])))
"""
##Mide solo lo que está completo.

## Condicional: Alta venta vs Baja venta
"""
Clasificación Venta = 
IF([Total Ventas] > 15000, "Alta", "Baja")
"""
## Se puede usar como campo para color, segmentación, etc.


## Medida de ventas del año anterior
"""
Ventas LY = 
CALCULATE([Total Ventas], SAMEPERIODLASTYEAR(Calendario[Date]))
"""

## medida de crecimiento
"""
Crecimiento % = 
DIVIDE([Total Ventas] - [Ventas LY], [Ventas LY])

"""
