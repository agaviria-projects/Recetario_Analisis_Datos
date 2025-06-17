
import pandas as pd
from datetime import datetime
from dateutil import parser

# Paso 1: Cargar archivo
archivo = input("📥 Ingresa el nombre del archivo Excel (Ej: ventas_sucia.xlsx): ")
df = pd.read_excel(archivo)
print("\n✅ Archivo cargado correctamente.\n")

# Limpiar nombres de columnas
df.columns = df.columns.str.strip()

# Validar columnas requeridas
columnas_requeridas = ['Nombre cliente', 'Categoria', 'Ciudad', 'Fecha compra', 'Cantidad', 'Precio Unitario']
faltantes = [col for col in columnas_requeridas if col not in df.columns]
if faltantes:
    print(f"⛔ Faltan columnas requeridas: {faltantes}")
    exit()

# Limpieza técnica
df['Nombre cliente'] = df['Nombre cliente'].fillna("SIN DATO").str.strip().str.title()
df['Categoria'] = df['Categoria'].fillna("SIN DATO").str.strip().str.title()
df['Ciudad'] = df['Ciudad'].fillna("SIN DATO").str.strip().str.capitalize()

# Limpieza robusta de fechas (usando dateutil.parser)
def parse_fecha(valor):
    try:
        return parser.parse(str(valor), dayfirst=True)
    except:
        return pd.NaT

df['Fecha compra'] = df['Fecha compra'].apply(parse_fecha)
df['Fecha compra'] = df['Fecha compra'].dt.strftime('%Y-%m-%d')
df['Fecha compra'] = df['Fecha compra'].fillna("SIN FECHA")

# Limpieza de datos numéricos
df['Cantidad'] = pd.to_numeric(df['Cantidad'], errors='coerce').fillna(0).astype(int)
df['Precio Unitario'] = pd.to_numeric(df['Precio Unitario'], errors='coerce').fillna(0).astype(int)

# Ordenar por registros más completos
df.sort_values(by='Precio Unitario', ascending=False, inplace=True)

# Eliminar duplicados lógicos
df.drop_duplicates(subset=['ID', 'Nombre cliente', 'Categoria', 'Fecha compra', 'Ciudad', 'Cantidad'], keep='first', inplace=True)
df.drop_duplicates(inplace=True)

# Reset índice
df.reset_index(drop=True, inplace=True)

# Exportar archivo limpio
nombre_salida = f"ventas_limpia_validacion_fechas_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
df.to_excel(nombre_salida, index=False)
print(f"\n📤 Archivo limpio guardado como: {nombre_salida}")
