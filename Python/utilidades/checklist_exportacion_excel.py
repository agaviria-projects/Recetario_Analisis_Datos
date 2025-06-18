"""
✅ CHECKLIST PARA AUTOMATIZACIÓN EN PYTHON (EXPORTAR EXCEL)

Estas 3 preguntas son claves para evitar errores comunes cuando trabajas con:
- exportación de datos
- conexión a bases de datos
- generación de archivos Excel

-----------------------------------
1️⃣ ¿Ya exporté el archivo antes de usarlo o modificarlo?
-----------------------------------

✔️ Significa: Asegúrate de haber ejecutado df.to_excel() antes de intentar abrir o modificar el archivo con openpyxl.

Ejemplo correcto:
    df.to_excel(nombre_archivo, index=False)
    wb = load_workbook(nombre_archivo)

Si te saltas df.to_excel(), saldrá FileNotFoundError.

-----------------------------------
2️⃣ ¿Estoy usando la misma variable (nombre_archivo o archivo_excel) en todos lados?
-----------------------------------

✔️ Significa: Usa una única variable para referirte al nombre del archivo Excel.

Ejemplo correcto:
    archivo_excel = "ventas.xlsx"
    df.to_excel(archivo_excel)
    convertir_a_tabla_excel(archivo_excel, "MiTabla")

❌ Error común:
    df.to_excel(archivo_excel)
    convertir_a_tabla_excel(nombre_archivo)  # nombre_archivo no existe

-----------------------------------
3️⃣ ¿En qué orden se ejecuta cada parte del script?
-----------------------------------

✔️ El orden importa mucho. Este es el flujo correcto:

1. Conectar a la base de datos = conexion = mysql.connector.connect
2. Ejecutar consulta SQL
3. Ejecutar la consulta y convertir a DataFrame = df = pd.read_sql(consulta, conexion)
4. Exportar o Guardar con df.to_excel()
5. Modificar (agregar tabla, estilo, etc)
6. Cerrar conexión

❌ Saltarse o invertir pasos genera errores que a veces son difíciles de detectar.

-----------------------------------

🧠 Recomendación final:
Pega este archivo como referencia en tu carpeta /utilidades o tu recetario.
Siempre consúltalo si algo te falla con archivos, conexiones o nombres mal definidos.
"""
