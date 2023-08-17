import pandas as pd

# Carga los datos desde el archivo CSV
file_path = r"C:\Users\wduran\Downloads\Inhibiciones Completas.csv"
data = pd.read_csv(file_path, sep=';', encoding='latin-1', low_memory=False)

# Convierte la columna de fechas a tipo datetime
data['FECHA_INICIO'] = pd.to_datetime(data['FECHA_INICIO'], format='%d-%m-%Y')

# Crea una nueva columna con el formato del mes
data['MES'] = data['FECHA_INICIO'].dt.strftime('%b-%y')

# Filtra los registros de los últimos 12 meses
last_12_months = data[data['FECHA_INICIO'] >= pd.Timestamp.now() - pd.DateOffset(months=12)]

# Agrupa y cuenta los registros por categoría, mes y cuenta
conteo_por_mes_cuenta = last_12_months.groupby(['CATEGORIA', 'MES', 'CUENTA']).size().reset_index(name='CONTEO')

# Filtra las cuentas que aparecen más de 2 veces en los últimos 12 meses
cuentas_con_mas_de_2_registros = conteo_por_mes_cuenta[conteo_por_mes_cuenta['CONTEO'] > 2]

# Agrupa y cuenta los registros por categoría y mes
conteo_mensual = cuentas_con_mas_de_2_registros.groupby(['CATEGORIA', 'MES'])['CUENTA'].count().reset_index(name='CONTEO_MENSUAL')

# Crea un DataFrame pivot para preparar los datos para el Excel
pivot_data = conteo_mensual.pivot_table(index='CATEGORIA', columns='MES', values='CONTEO_MENSUAL', aggfunc='sum').reset_index()

# Crea un archivo Excel
output_excel = pd.ExcelWriter("Conteo_Cuentas_Mas_De_2_Registros_Mensual.xlsx", engine='xlsxwriter')

# Agrega el DataFrame pivot al archivo Excel
pivot_data.to_excel(output_excel, sheet_name='Conteo_Mensual', index=False)

# Guarda el archivo Excel
output_excel.save()
