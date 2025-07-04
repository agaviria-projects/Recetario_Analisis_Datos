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


# 🧠 CLAVE FUNDAMENTAL: Modelo Estrella y Relacionamiento
# 🔹 TABLAS DE DIMENSIONES
Contienen atributos descriptivos
Tienen clave primaria (PK) única e irrepetible
Ejemplos:
    productos: id_producto (PK)
    clientes: id_cliente (PK)

# 🔸 TABLA DE HECHOS
Contiene datos medibles (ventas, cantidades, montos)
Tiene claves foráneas (FK) que apuntan a las dimensiones
Ejemplo:
    ventas: contiene id_producto y id_cliente como FK

# 🧩 ANALOGÍA:
"Las dimensiones son el diccionario, las ventas son las frases que lo consultan."   

# ✅ REGLA DE ORO PARA POWER BI Y SQL:
Clave	            Ubicación	                 Debe ser...
PK (Primary Key)    Tabla dimensión              Única y sin nulos
FK (Foreign Key)	Tabla de hechos	Repetible,   conecta con PK
Relación	        Power BI o SQL	             1:N (Dimensión → Hecho)

# 🧠 En Power BI:
Las relaciones se hacen en la vista de modelo
Las dimensiones van en el eje o filtros
Los hechos se usan para medidas DAX

# ✅ Buenas prácticas
Las PK no deben tener duplicados
Las FK deben coincidir con algún PK existente
Toda tabla de hechos debe tener al menos 1 FK hacia dimensiones
Ideal tener una tabla calendario si hay campos de fecha

# 🧠 DIFERENCIAS ENTRE FUNCIONES DAX:
🔹 Medidas iteradoras (SUMX, AVERAGEX, etc.)
🔸 Medidas columnares/directas (SUM, AVERAGE, etc.)

# ✅ 1. ¿Qué son funciones iteradoras?
Evalúan fila por fila, aplican una operación y luego agregan (suman, promedian, etc.)

🧮 Ejemplos:
Total Ventas = SUMX(ventas, ventas[cantidad] * ventas[precio_unitario])

💡 ¿Por qué SUMX?
Porque no existe una columna con el total ya multiplicado. Entonces DAX va fila por fila y hace la operación.

# ✅ 2. ¿Qué hacen las funciones directas?
Trabajan sobre una columna existente completa.

🧮 Ejemplo:
Cantidad Total = SUM(ventas[cantidad])

✅ Aquí ya existe la columna cantidad, así que no necesitas iterar.

✅ 3. ¿Cuándo usar DIVIDE() en vez de /?

# 👉 DIVIDE(x, y) es mejor que x / y porque:
Si y = 0, no lanza error
Permite definir qué valor mostrar si hay división inválida
🧮 Ejemplo:
Precio Promedio x Unidad = DIVIDE([Total Ventas], [Cantidad Total])

✔ Esto calcula el precio promedio, pero sin errores si la cantidad total es cero.

