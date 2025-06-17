"""
recetario_sql_index.py
📄 Índice general de archivos SQL. Útil para saber qué contiene cada script de tu recetario SQL.
"""

recetario_sql = {
    "consultas_basicas.sql": "📘 SELECT, WHERE, ORDER BY, operadores lógicos, alias.",
    "joins_groupby.sql": "🔗 INNER JOIN, LEFT JOIN, GROUP BY con funciones agregadas.",
    "subconsultas_y_alias.sql": "🧠 Subconsultas en SELECT y WHERE, alias de tablas y campos.",
    "practicas_sql_tienda.sql": "🛒 Consultas aplicadas a un modelo de tienda: clientes, productos, ventas."
}

for archivo, descripcion in recetario_sql.items():
    print(f"{archivo}: {descripcion}")
