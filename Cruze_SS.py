import pandas as pd

# Leer el archivo de Excel
df = pd.read_csv("C:/Users/wduran/Downloads/SS y Descuento.csv",sep=";",encoding='latin-1')

# Convertir las columnas de fecha a tipo datetime
df['fecha_estado'] = pd.to_datetime(df['FECHA_ESTADO'])
df['fecha_solicitud'] = pd.to_datetime(df['Fecha Solicitud '])

# Agregar una nueva columna "mes_coincidente" con valores booleanos
df['mes_coincidente'] = df.apply(lambda row: row['fecha_estado'].day == row['fecha_solicitud'].day, axis=1)

# Guardar los cambios en un nuevo archivo de Excel
df.to_excel('SS y Descuentos VF.xlsx', index=False)
