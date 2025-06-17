# 🔗 Conexión directa entre Power BI y MySQL (Recetario)

Este documento resume paso a paso cómo conectar Power BI Desktop directamente a una base de datos MySQL local (como XAMPP), ideal para análisis en tiempo real con tablas SQL.

---

## ✅ Requisitos previos

1. Tener Power BI Desktop instalado.
2. Tener MySQL activo (XAMPP o similar).
3. Tener una base de datos creada, por ejemplo: `tienda`.

---

## 🔧 Paso 1: Instalar MySQL Connector/ODBC

- Ir a: https://dev.mysql.com/downloads/connector/odbc/
- Descargar: **Windows (x86, 32-bit), MSI Installer**
- Instalar usando opción `Typical`.

---

## 🔧 Paso 2: Instalar MySQL Connector for .NET

- Ir a: https://dev.mysql.com/downloads/connector/net/
- Descargar: **Connector/NET 8.x (MSI Installer)**
- Instalar (opción `Typical` o `Complete`).

*Esto habilita la conexión desde Power BI a MySQL.*

---

## 🔄 Paso 3: Reiniciar Power BI

- Cierra y vuelve a abrir Power BI Desktop para que reconozca los nuevos conectores.

---

## 🔌 Paso 4: Conectar a MySQL

1. En Power BI, clic en **Obtener datos** > **Base de datos** > **MySQL**.
2. En la ventana de conexión:
   - **Servidor**: `localhost`
   - **Base de datos**: `tienda`
   - Deja vacío "Instrucción SQL"
   - Asegúrate de marcar ✅ "Incluir columnas de relación"
3. Clic en **Aceptar**
4. Selecciona las tablas (`ventas`, `clientes`, `productos`) y haz clic en **Cargar**

---

## 📊 Paso 5: Modelo de datos

- Ir a la vista de modelo (ícono de diagrama)
- Verifica relaciones:
  - `ventas.id_cliente` → `clientes.id_cliente`
  - `ventas.id_producto` → `productos.id_producto`

---

## 📅 Paso 6: Crear tabla Calendario en DAX

1. Ir a pestaña **Modelado > Nueva tabla**
2. Pegar:

```dax
Calendario = 
ADDCOLUMNS(
    CALENDAR(DATE(2024,1,1), DATE(2025,12,31)),
    "Año", YEAR([Date]),
    "Mes", MONTH([Date]),
    "NombreMes", FORMAT([Date], "MMMM"),
    "AñoMes", FORMAT([Date], "YYYY-MM")
)
```

3. Relacionar `Calendario[Date]` con `ventas[fecha]`.

---

¡Listo! Ya puedes crear medidas como `TotalVentas`, `SAMEPERIODLASTYEAR`, `YTD`, etc.

