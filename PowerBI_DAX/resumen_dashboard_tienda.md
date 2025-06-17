# 📊 Proyecto Completo - Dashboard de Ventas: Tienda de Accesorios

Este proyecto simula un análisis de ventas completo utilizando **MySQL + Power BI**, incluyendo limpieza de datos, conexión directa, medidas DAX, visualizaciones y actualizaciones dinámicas.

---

## ✅ ETAPA 1: CREACIÓN DE BASE DE DATOS EN MYSQL

**1.1. Base de datos y modelo de datos**

- Base: `tienda`
- Tablas:
  - `clientes (dimensión)`
  - `productos (dimensión)`
  - `ventas (tabla de hechos)`

**1.2. Relaciones**
- `ventas.id_cliente → clientes.id_cliente`
- `ventas.id_producto → productos.id_producto`

**1.3. Datos insertados**
- 20 registros por tabla
- Año: 2024 y 2025 (para comparación anual)

---

## ✅ ETAPA 2: CONEXIÓN A POWER BI

**2.1. Habilitar MySQL Connector ODBC**

- Se descargó e instaló `MySQL ODBC 64-bit`.
- En Power BI: Obtener datos → MySQL Database

**2.2. Parámetros usados**
- Servidor: `localhost`
- Base de datos: `tienda`
- Se cargaron las tres tablas

**2.3. Validación de relaciones**
- Modelo estrella validado automáticamente

---

## ✅ ETAPA 3: TABLA CALENDARIO

**Tabla generada con DAX:**

```dax
Calendario = 
ADDCOLUMNS (
    CALENDAR (DATE(2024,1,1), DATE(2025,12,31)),
    "Año", YEAR([Date]),
    "Mes", MONTH([Date]),
    "NombreMes", FORMAT([Date], "MMMM"),
    "AñoMes", FORMAT([Date], "YYYY-MM")
)
```

---

## ✅ ETAPA 4: MEDIDAS DAX

**Básicas**
```dax
TotalVentas = SUMX(Ventas, Ventas[cantidad] * Ventas[precio_unitario])
UnidadesVendidas = SUM(Ventas[cantidad])
ClientesUnicos = DISTINCTCOUNT(Ventas[id_cliente])
```

**Tiempo**
```dax
Ventas LY = CALCULATE([TotalVentas], SAMEPERIODLASTYEAR(Calendario[Date]))
Variacion Anual % = DIVIDE([TotalVentas] - [Ventas LY], [Ventas LY])
Ventas YTD = TOTALYTD([TotalVentas], Calendario[Date])
```

---

## ✅ ETAPA 5: VISUALIZACIONES

### 🟦 Página 1: Resumen Ejecutivo
- Tarjetas: total ventas, promedio por cliente, unidades, clientes únicos
- Gráficos:
  - Columnas por categoría
  - Columnas por ciudad
  - Línea por AñoMes
- Tabla dinámica de clientes

---

### 🟩 Página 2: Detalle por Producto
- Gráfico de barras por nombre de producto
- Gráfico de torta por categoría
- Tabla detallada
- Segmentadores por año, producto y categoría

---

### 🟨 Página 3: Análisis por Ciudad y Cliente
- Gráfico de barras por ciudad
- Tabla detallada por cliente
- Mapa geográfico (habilitado en Opciones > Seguridad)
- Verificación visual de crecimiento en burbujas al insertar nuevos datos

---

### 🟧 Página 4: Tendencias en el Tiempo
- Comparación `TotalVentas` vs `Ventas LY` (gráfico de líneas o barras)
- Área de `Ventas YTD`
- Tarjeta de `% de variación anual`

---

## 🔁 ETAPA 6: ACTUALIZACIÓN Y DINÁMICA

- Se insertaron nuevos registros desde MySQL
- Se analizaron sus efectos en visualizaciones al hacer clic en “Actualizar”
- Se monitoreó el impacto directo en tarjetas, mapas y gráficos temporales

---

## 🎯 Conclusión

Este proyecto demuestra un flujo de análisis **de extremo a extremo**, incluyendo:

- Diseño del modelo relacional
- Conexión dinámica a Power BI
- Medidas avanzadas en DAX
- Visualizaciones interpretables
- Simulación de variaciones temporales y geográficas

Ideal para pruebas técnicas, presentaciones ejecutivas o dashboards reales.
