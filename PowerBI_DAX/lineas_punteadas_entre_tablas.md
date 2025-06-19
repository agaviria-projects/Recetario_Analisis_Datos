Las líneas punteadas en Power BI indican una relación inactiva entre dos columnas de tablas distintas.

Power BI no puede activar automáticamente dos relaciones entre las mismas tablas al mismo tiempo. En tu caso:

Calendario[Date] está relacionado con:

    VentasTabla[fecha_pedido] ✅ (activa)

    VentasTabla[fecha_entrega] ❌ (inactiva)

Línea continua = relación activa (usada por defecto en visualizaciones y medidas)

Línea punteada = relación inactiva, solo se usa con funciones DAX específicas como:

CALCULATE(
    [Medida],
    USERELATIONSHIP(Calendario[Date], VentasTabla[fecha_entrega])
)
