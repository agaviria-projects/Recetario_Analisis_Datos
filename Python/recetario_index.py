# recetario_index.py
# Índice general del recetario Python: descripción breve de cada script agrupado por categoría.

recetario = {
    "limpieza_basica": {
        "limpiar_excel_basico.py": "Versión simple para limpiar Excel con pandas (espacios, texto, fechas, duplicados).",
        "limpiar_excel_script.py": "Script interactivo que pide el archivo por input y guarda con nombre dinámico.",
        "limpieza_validacion_fechas.py": "Versión robusta que marca fechas vacías como 'SIN FECHA' y conserva datos importantes."
    },

    "generadores": {
        "generar_datos_ejemplo_excel.py": "Genera archivo Excel con registros sucios (fechas mal, duplicados, mayúsculas, vacíos).",
        "exportar_mysql_excel_estructurado.py": "Ejecuta consulta SQL y exporta el resultado en formato tabla para Power BI."
    },

    "utilidades": {
        "plantilla_procesar_consolidado.py": "Lee archivo con varias hojas (ventas, clientes, productos) y genera tablas separadas limpias.",
        "logica_duplicados_nulos.py": "Contiene funciones auxiliares para limpieza de datos: nulos, duplicados, reemplazos.",
        "ejemplo_tabla_estructurada.py": "Extrae y convierte tabla plana de Excel en tres hojas estructuradas para Power BI."
    }
}

# Mostrar listado formateado
for categoria, archivos in recetario.items():
    print(f"\n📂 {categoria.upper()}")
    for archivo, descripcion in archivos.items():
        print(f" - {archivo}: {descripcion}")

