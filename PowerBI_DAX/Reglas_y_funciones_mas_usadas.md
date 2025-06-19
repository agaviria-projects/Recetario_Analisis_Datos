# 📘 Recetario DAX Power BI – Reglas y Funciones más Usadas

## 🧠 Guía general de reglas

### 🔹 1. Acceso a columnas
- Siempre se usa el formato: `Tabla[Columna]`
```DAX
SUM(ventas[cantidad])
AVERAGE(clientes[edad])
```

### 🔹 2. Acceso a medidas
- No se usa tabla:
```DAX
CALCULATE([Total Ventas])
IF([Total Unidades] > 100, "Alto", "Bajo")
```

### 🔹 3. Dentro de funciones iteradoras (`SUMX`, `AVERAGEX`, etc.)
- Se especifica la tabla que se recorre y sus columnas:
```DAX
SUMX(ventas, ventas[cantidad] * ventas[precio])
```

### 🔹 4. Uso de `RELATED`
- Se usa para traer valores desde una tabla relacionada (relación 1:*)
```DAX
RELATED(productos[precio_unitario])
```
- ✅ No se pone tabla principal dentro de `RELATED()`

### 🔹 5. Uso de `CALCULATE`
- Sirve para modificar el contexto de cálculo
```DAX
CALCULATE([Total Ventas], clientes[region] = "Andina")
```
- ✅ Puedes usar `FILTER(...)` como segundo parámetro para lógica avanzada
```DAX
CALCULATE([Total Ventas], FILTER(clientes, clientes[segmento] = "Mayorista"))
```

---

## 📚 Funciones más usadas por categoría

### ✅ Funciones de agregación
```DAX
SUM(ventas[cantidad])
AVERAGE(ventas[cantidad])
MIN(productos[precio])
MAX(productos[precio])
COUNT(clientes[id_cliente])
```

### ✅ Funciones iterativas
```DAX
SUMX(tabla, expresión)
AVERAGEX(tabla, expresión)
```

### ✅ Funciones lógicas
```DAX
IF(condición, valor_si_verdadero, valor_si_falso)
SWITCH(valor, caso1, resultado1, caso2, resultado2, ...)
```

### ✅ Funciones de relación
```DAX
RELATED(tabla[valor])
RELATEDTABLE(tabla_relacionada)
```

### ✅ Funciones de contexto
```DAX
CALCULATE(medida, filtros)
FILTER(tabla, condición)
ALL(tabla) -- quita filtros de esa tabla
ALLEXCEPT(tabla, columna) -- quita todos los filtros excepto uno
```

### ✅ Funciones de tiempo (requieren tabla calendario)
```DAX
TOTALYTD([Ventas], 'Calendario'[Fecha])
SAMEPERIODLASTYEAR('Calendario'[Fecha])
DATESINPERIOD('Calendario'[Fecha], MAX('Calendario'[Fecha]), -3, MONTH)
```

---

## 📝 Tips extra para recordar

- ✅ Las **medidas** nunca llevan `Tabla[]`, solo el nombre.
- ✅ Siempre define relaciones antes de usar `RELATED`.
- ✅ Usa `SUMX` cuando necesitas multiplicar columnas.
- ❌ No uses columnas "anidadas tipo Table" desde Power Query.

🔹 1. Agrega sección final: Errores comunes en DAX

## ⚠️ Errores comunes

- ❌ Usar [columna] sin tabla → `cantidad` → debe ser `ventas[cantidad]`
- ❌ Intentar usar medida como `CALCULATE(ventas[Total Ventas])` → debe ser `CALCULATE([Total Ventas])`
- ❌ No definir relaciones antes de usar `RELATED()` → da error
- ❌ Usar columnas tipo 'Table' desde Power Query → no compatibles con DAX

🔹 2. Agrega una tabla resumen de funciones por tipo

| Categoría           | Funciones clave                           |
|---------------------|-------------------------------------------|
| Agregación          | SUM, AVERAGE, COUNT, MAX, MIN             |
| Iteración           | SUMX, AVERAGEX                            |
| Relación            | RELATED, RELATEDTABLE                     |
| Filtros y contexto  | CALCULATE, FILTER, ALL, ALLEXCEPT         |
| Tiempo              | TOTALYTD, SAMEPERIODLASTYEAR, DATESINPERIOD |
| Lógicas             | IF, SWITCH                                |