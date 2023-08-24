import pandas as pd
import numpy as np
import datetime

# Output para envio a claudio 

#name_in = "Inhibiciones oct 2022 - mar 2023.CSV"
name_in = r"C:\Users\wduran\Downloads\Inhibiciones Completas.csv"
bbdd_in = pd.read_csv(name_in, sep= ';',encoding='latin-1',low_memory=False)

#fecha 
bbdd_in['FECHA_INICIO'] = bbdd_in['FECHA_INICIO'].astype(str)
bbdd_in['FECHA'] = pd.to_datetime(bbdd_in.FECHA_INICIO, format = '%d-%m-%Y').dt.strftime('%Y-%m-%d')
bbdd_in.FECHA = pd.to_datetime(bbdd_in.FECHA)
bbdd_in['Mes'] = bbdd_in['FECHA'].dt.strftime('%b_%y')
bbdd_in['Mes'].unique()

base_mensual = bbdd_in.groupby(['Mes', 'CUENTA']).agg(cuentas_u = ('CUENTA', 'count')).reset_index()
base_mensual_2 = base_mensual.groupby(['CUENTA']).agg(Meses_reit = ('CUENTA', 'count')).reset_index()
base_mensual_3 = base_mensual.pivot(index='CUENTA', columns='Mes', values='cuentas_u').reset_index()
compilado_meses_r = base_mensual_3.merge(base_mensual_2, how = 'left', on = 'CUENTA')
compilado_meses_r = compilado_meses_r.fillna(0)
print(compilado_meses_r)

analisis_ihibiciones = pd.ExcelWriter("Analisis_inhibiciones_MR.xlsx", engine='xlsxwriter')
compilado_meses_r.to_excel(analisis_ihibiciones, sheet_name='meses reiterados', index = False)  
analisis_ihibiciones.save()#CHECKED

#OUTPUT PARA SACAR Q DE INHIBICIONES POR CANAL


#name_in = "Inhibiciones oct 2022 - mar 2023.CSV"
name_in = r"C:\Users\wduran\Downloads\Inhibiciones Completas.csv"
bbdd_in = pd.read_csv(name_in, sep= ';',encoding='latin-1',low_memory=False)

#fecha 
bbdd_in['FECHA_INICIO'] = bbdd_in['FECHA_INICIO'].astype(str)
bbdd_in['FECHA'] = pd.to_datetime(bbdd_in.FECHA_INICIO, format = '%d-%m-%Y').dt.strftime('%Y-%m-%d')
bbdd_in.FECHA = pd.to_datetime(bbdd_in.FECHA)
bbdd_in['MES'] = bbdd_in['FECHA'].dt.strftime('%b_%y')
bbdd_in['MES'].unique()

def conteo_mes_a_mes_por_categoria(dataframe):
    conteo = dataframe.groupby(['MES', 'Categoria'])['USUARIO'].count().reset_index()
    conteo_pivot = conteo.pivot(index='Categoria', columns='MES', values='USUARIO').reset_index()
    return conteo_pivot

conteo_mes_a_mes = conteo_mes_a_mes_por_categoria(bbdd_in)
print(conteo_mes_a_mes)

analisis_ihibiciones_canales = pd.ExcelWriter("Analisis_inhibiciones_canales.xlsx", engine='xlsxwriter')
conteo_mes_a_mes.to_excel(analisis_ihibiciones_canales, sheet_name='conteo canales', index = False)  
analisis_ihibiciones_canales.save()#CHECKED



# OUTPUT DE CONTEO REPETIDOS POR CANAL 

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
conteo_por_mes_cuenta = last_12_months.groupby(['Categoria', 'MES', 'CUENTA']).size().reset_index(name='CONTEO')

# Filtra las cuentas que aparecen más de 2 veces en los últimos 12 meses
cuentas_con_mas_de_2_registros = conteo_por_mes_cuenta[conteo_por_mes_cuenta['CONTEO'] >= 2]

# Agrupa y cuenta los registros por categoría y mes
conteo_mensual = cuentas_con_mas_de_2_registros.groupby(['Categoria', 'MES'])['CUENTA'].count().reset_index(name='CONTEO_MENSUAL')

# Crea un DataFrame pivot para preparar los datos para el Excel
pivot_data = conteo_mensual.pivot_table(index='Categoria', columns='MES', values='CONTEO_MENSUAL', aggfunc='sum').reset_index()

# Crea un archivo Excel
output_excel = pd.ExcelWriter("Conteo_Cuentas_Mas_De_2_Registros_Mensual.xlsx", engine='xlsxwriter')

# Agrega el DataFrame pivot al archivo Excel
pivot_data.to_excel(output_excel, sheet_name='Conteo_Mensual', index=False)

# Guarda el archivo Excel- hacer un print 
output_excel.save()

print(conteo_mensual)

#OUTPUT PARA SACAR INHIBICIONES MAYOR A 6 DIAS 

# Carga los datos desde el archivo CSV
file_path = r"C:\Users\wduran\Downloads\Inhibiciones Completas.csv"
data = pd.read_csv(file_path, sep=';', encoding='latin-1', low_memory=False)

# Convierte la columna de fechas a tipo datetime
data['FECHA_INICIO'] = pd.to_datetime(data['FECHA_INICIO'], format='%d-%m-%Y')

# Crea una nueva columna con el formato del mes
data['MES'] = data['FECHA_INICIO'].dt.strftime('%b_%y')

# Filtra los registros con PLAZO mayor a 6
data_plazo_mayor_6 = data[data['PLAZO'] > 6]

# Agrupa y cuenta los registros por categoría, mes y cuenta
conteo_por_mes_cuenta = data_plazo_mayor_6.groupby(['Categoria', 'MES', 'CUENTA']).size().reset_index(name='CONTEO')

# Crea un DataFrame pivot para preparar los datos para el Excel
pivot_data = conteo_por_mes_cuenta.pivot_table(index='Categoria', columns='MES', values='CONTEO', aggfunc='sum').reset_index()

# Crea un archivo Excel
output_excel = pd.ExcelWriter("Conteo_Cuentas_Plazo_Mayor_A_6_Mensual.xlsx", engine='xlsxwriter')

# Agrega el DataFrame pivot al archivo Excel
pivot_data.to_excel(output_excel, sheet_name='Conteo_Mensual', index=False)

print (pivot_data)
# Guarda el archivo Excel
output_excel.save()

#CALCULAR DEUDA TOTAL INHIBIDA 

# Carga los datos desde el archivo CSV
file_path = r"C:\Users\wduran\Downloads\Inhibiciones Completas.csv"
data = pd.read_csv(file_path, sep=';', encoding='latin-1', low_memory=False)

# Convierte la columna de fechas a tipo datetime
data['FECHA_INICIO'] = pd.to_datetime(data['FECHA_INICIO'], format='%d-%m-%Y')

# Crea una nueva columna con el formato del mes
data['MES'] = data['FECHA_INICIO'].dt.strftime('%b_%y')

# Calcula la deuda neta con un 19% de descuento
data['DEUDA_NETA_DESC'] = round(data['DEUDA_NETA'] / 1.19)  # Resta un 19%

# Agrupa y suma la deuda neta descontada por canal, mes y cuenta
suma_deuda_por_mes_canal = data.groupby(['Categoria', 'MES', 'CUENTA'])['DEUDA_NETA_DESC'].sum().reset_index(name='SUMA_DEUDA_DESC')

# Crea un DataFrame pivot para preparar los datos para el Excel
pivot_data = suma_deuda_por_mes_canal.pivot_table(index='Categoria', columns='MES', values='SUMA_DEUDA_DESC', aggfunc='sum').reset_index()

# Crea un archivo Excel
output_excel = pd.ExcelWriter("Suma_Deuda_Descuento_Mensual_Por_Canal.xlsx", engine='xlsxwriter')

# Agrega el DataFrame pivot al archivo Excel
pivot_data.to_excel(output_excel, sheet_name='Suma_Deuda_Mensual_Por_Canal', index=False)

# Guarda el archivo Excel
output_excel.save()

print(pivot_data)