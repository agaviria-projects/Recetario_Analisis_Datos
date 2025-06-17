# 🔍 FASE 2 – Limpieza lógica con tolerancia (permite 0 como valor predeterminado)
import pandas as pd

# 1. Cargar archivo
archivo="ventas_sucia.xlsx"
df=pd.read_excel(archivo)

# 1. Rellenar valores nulos en columnas críticas para no perder registros
df['Cantidad'].fillna(0, inplace=True)
df['Precio Unitario'].fillna(0, inplace=True)

# 2. Eliminar duplicados lógicos (mantener la fila más completa)
df.drop_duplicates(subset=['Nombre cliente', 'Categoria', 'Fecha compra'], keep='last', inplace=True)

# 3. Eliminar solo si falta la fecha (imprescindible para análisis)
df.dropna(subset=['Fecha compra'], inplace=True)

# 4. Reiniciar índice
#reset_index() resetea los números del índice:antes el ID seria 0,2,4
#despuest de reset_inde = 0,1,2 No afecta la columna 'ID', solo el índice interno
df.reset_index(drop=True, inplace=True)
