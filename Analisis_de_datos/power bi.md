📊 RUTA 2 – POWER BI (desde cero, explicando lógica visual)
Etapa	Tema	Enfoque lógico
✅ 1	Cargar datos y transformar	Pensar como un Excel automatizado
✅ 2	Crear relaciones	Conectar tablas como piezas de un rompecabezas
✅ 3	DAX básico (SUM, IF)	Crear tus propias columnas y métricas
✅ 4	Visualizaciones	Contar historias con datos (gráficas con sentido)
✅ 5	Tabla calendario	Razonar el tiempo y tendencias
✅ 6	Página ejecutiva con KPIs	Analizar como un gerente
✅ 7	Proyecto mini: dashboard real	Aplicar desde cero a presentación final

# ✅ PASO A PASO – Crear columna registro_incompleto
    Ve a la vista de datos (ícono de tabla en el panel izquierdo 📄)

    En el panel derecho, selecciona la tabla: ventas_unificadas(tabla de hechos)

    Arriba, haz clic en:
    🔁 Modelado > Nueva columna

    En la barra de fórmulas que aparece, escribe el siguiente DAX:

registro_incompleto = IF(ISBLANK(ventas_unificadas[cantidad]), "Sí", "No")

# ISBLANK(...) evalúa si el valor está vacío o nulo
# IF(..., "Sí", "No") convierte el resultado en un texto que puedes usar como filtro o etiqueta

# 🧩 MODELO ESTRELLA EN VISUALIZACIONES
🟦 Dimensiones: son descriptivas → categorías, nombres, fechas, zonas
🟥 Hechos: son numéricos o medibles → cantidades, precios, totales

# 🎯 ¿Dónde va cada una en los visuales?
Tipo de campo	        Origen	            ¿Dónde lo pones en la       Ejemplo
                                            visualización?	
🟦 Dimensión (texto)	Tabla de dimensión	Eje, Segmento,              cliente, producto, ciudad
                                            Leyenda, Filtro	
🟥 Métrica (número)     Tabla de hechos     Valores (medidas)           cantidad,precio_unitario,
                                                                         total_ventas.
📅 Tiempo (fecha)       Tabla calendario    Eje de tiempo               fecha_venta
🟧 Medida calculada(DAX)Tabla de hechos     Valores (como KPIs,tarjetas)total_ventas = SUM(...)
# "Las dimensiones dan contexto (quién, qué, dónde), los hechos dan magnitud (cuánto, cuántas veces)"