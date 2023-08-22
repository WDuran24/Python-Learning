import pandas as pd
import numpy as np
import datetime

# Output para enviar a Claudio de Inhibiciones 

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
analisis_ihibiciones.save()

#OUTPUT PARA SACAR Q DE INHIBICIONES POR CANAL

def generar_conteo_inhibiciones_totales(bbdd_in):
    conteo_inhibiciones_totales = bbdd_in.groupby(['CATEGORIA'])['CUENTA'].count().reset_index()
    conteo_inhibiciones_totales.rename(columns={'CUENTA': 'Inhibiciones Totales'}, inplace=True)
    return conteo_inhibiciones_totales

#name_in = "Inhibiciones oct 2022 - mar 2023.CSV"
name_in = r"C:\Users\wduran\Downloads\Inhibiciones Completas.csv"
bbdd_in = pd.read_csv(name_in, sep= ';',encoding='latin-1',low_memory=False)

#fecha 
bbdd_in['FECHA_INICIO'] = bbdd_in['FECHA_INICIO'].astype(str)
bbdd_in['FECHA'] = pd.to_datetime(bbdd_in.FECHA_INICIO, format = '%d-%m-%Y').dt.strftime('%Y-%m-%d')
bbdd_in.FECHA = pd.to_datetime(bbdd_in.FECHA)
bbdd_in['MES'] = bbdd_in['FECHA'].dt.strftime('%b_%y')
bbdd_in['MES'].unique()

base_mensual = bbdd_in.groupby(['MES', 'CUENTA']).agg(cuentas_u = ('CUENTA', 'count')).reset_index()
base_mensual_2 = base_mensual.groupby(['CUENTA']).agg(Meses_reit = ('CUENTA', 'count')).reset_index()
base_mensual_3 = base_mensual.pivot(index='CUENTA', columns='MES', values='cuentas_u').reset_index()
compilado_meses_r = base_mensual_3.merge(base_mensual_2, how = 'left', on = 'CUENTA')
compilado_meses_r = compilado_meses_r.fillna(0)
print(compilado_meses_r)
conteo_inhibiciones_totales = generar_conteo_inhibiciones_totales(bbdd_in)
conteo_inhibiciones_reiteradas = generar_conteo_inhibiciones_reiteradas(bbdd_in)
conteo_inhibiciones_fuera_de_plazo = generar_conteo_inhibiciones_fuera_de_plazo(bbdd_in)

# Crear un nuevo archivo Excel
analisis_ihibiciones = pd.ExcelWriter("Analisis_inhibiciones_MR.xlsx", engine='xlsxwriter')

# Agregar las hojas con los conteos a Excel
conteo_inhibiciones_reiteradas.to_excel(analisis_ihibiciones, sheet_name='Inhibiciones Reiteradas', index=False)
conteo_inhibiciones_fuera_de_plazo.to_excel(analisis_ihibiciones, sheet_name='Inhibiciones Fuera de Plazo', index=False)

# Guardar el archivo Excel
analisis_ihibiciones.save()

def conteo_mes_a_mes_por_categoria(dataframe):
    conteo = dataframe.groupby(['MES', 'CATEGORIA'])['ID_ANDES'].count().reset_index()
    conteo_pivot = conteo.pivot(index='CATEGORIA', columns='MES', values='ID_ANDES').reset_index()
    return conteo_pivot

conteo_mes_a_mes = conteo_mes_a_mes_por_categoria(bbdd_in)
print(conteo_mes_a_mes)

analisis_inhibiciones = pd.ExcelWriter("Analisis_inhibiciones_MR_conteo_por_canal.xlsx", engine='xlsxwriter')
compilado_meses_r.to_excel(analisis_inhibiciones, sheet_name='meses reiterados', index=False)
conteo_mes_a_mes.to_excel(analisis_inhibiciones, sheet_name='conteo_mes_a_mes_por_categoria', index=False)
analisis_inhibiciones.save()

#OUTPUT PARA SACAR Q DE INHIBICIONES POR CANAL

def generar_conteo_inhibiciones_totales(bbdd_in):
    conteo_inhibiciones_totales = bbdd_in.groupby(['CATEGORIA'])['CUENTA'].count().reset_index()
    conteo_inhibiciones_totales.rename(columns={'CUENTA': 'Inhibiciones Totales'}, inplace=True)
    return conteo_inhibiciones_totales

#name_in = "Inhibiciones oct 2022 - mar 2023.CSV"
name_in = r"C:\Users\wduran\Downloads\Inhibiciones Completas.csv"
bbdd_in = pd.read_csv(name_in, sep= ';',encoding='latin-1',low_memory=False)

#fecha 
bbdd_in['FECHA_INICIO'] = bbdd_in['FECHA_INICIO'].astype(str)
bbdd_in['FECHA'] = pd.to_datetime(bbdd_in.FECHA_INICIO, format = '%d-%m-%Y').dt.strftime('%Y-%m-%d')
bbdd_in.FECHA = pd.to_datetime(bbdd_in.FECHA)
bbdd_in['MES'] = bbdd_in['FECHA'].dt.strftime('%b_%y')
bbdd_in['MES'].unique()

base_mensual = bbdd_in.groupby(['MES', 'CUENTA']).agg(cuentas_u = ('CUENTA', 'count')).reset_index()
base_mensual_2 = base_mensual.groupby(['CUENTA']).agg(Meses_reit = ('CUENTA', 'count')).reset_index()
base_mensual_3 = base_mensual.pivot(index='CUENTA', columns='MES', values='cuentas_u').reset_index()
compilado_meses_r = base_mensual_3.merge(base_mensual_2, how = 'left', on = 'CUENTA')
compilado_meses_r = compilado_meses_r.fillna(0)
print(compilado_meses_r)
conteo_inhibiciones_totales = generar_conteo_inhibiciones_totales(bbdd_in)
conteo_inhibiciones_reiteradas = generar_conteo_inhibiciones_reiteradas(bbdd_in)
conteo_inhibiciones_fuera_de_plazo = generar_conteo_inhibiciones_fuera_de_plazo(bbdd_in)

# Crear un nuevo archivo Excel
analisis_ihibiciones = pd.ExcelWriter("Analisis_inhibiciones_MR.xlsx", engine='xlsxwriter')

# Agregar las hojas con los conteos a Excel
conteo_inhibiciones_reiteradas.to_excel(analisis_ihibiciones, sheet_name='Inhibiciones Reiteradas', index=False)
conteo_inhibiciones_fuera_de_plazo.to_excel(analisis_ihibiciones, sheet_name='Inhibiciones Fuera de Plazo', index=False)

# Guardar el archivo Excel
analisis_ihibiciones.save()

def conteo_mes_a_mes_por_categoria(dataframe):
    conteo = dataframe.groupby(['MES', 'CATEGORIA'])['ID_ANDES'].count().reset_index()
    conteo_pivot = conteo.pivot(index='CATEGORIA', columns='MES', values='ID_ANDES').reset_index()
    return conteo_pivot

conteo_mes_a_mes = conteo_mes_a_mes_por_categoria(bbdd_in)
print(conteo_mes_a_mes)

analisis_inhibiciones = pd.ExcelWriter("Analisis_inhibiciones_MR_conteo_por_canal.xlsx", engine='xlsxwriter')
compilado_meses_r.to_excel(analisis_inhibiciones, sheet_name='meses reiterados', index=False)
conteo_mes_a_mes.to_excel(analisis_inhibiciones, sheet_name='conteo_mes_a_mes_por_categoria', index=False)
analisis_inhibiciones.save()

#OUTPUT PARA SACAR Q DE INHIBICIONES POR CANAL

def generar_conteo_inhibiciones_totales(bbdd_in):
    conteo_inhibiciones_totales = bbdd_in.groupby(['CATEGORIA'])['CUENTA'].count().reset_index()
    conteo_inhibiciones_totales.rename(columns={'CUENTA': 'Inhibiciones Totales'}, inplace=True)
    return conteo_inhibiciones_totales

#name_in = "Inhibiciones oct 2022 - mar 2023.CSV"
name_in = r"C:\Users\wduran\Downloads\Inhibiciones Completas.csv"
bbdd_in = pd.read_csv(name_in, sep= ';',encoding='latin-1',low_memory=False)

#fecha 
bbdd_in['FECHA_INICIO'] = bbdd_in['FECHA_INICIO'].astype(str)
bbdd_in['FECHA'] = pd.to_datetime(bbdd_in.FECHA_INICIO, format = '%d-%m-%Y').dt.strftime('%Y-%m-%d')
bbdd_in.FECHA = pd.to_datetime(bbdd_in.FECHA)
bbdd_in['MES'] = bbdd_in['FECHA'].dt.strftime('%b_%y')
bbdd_in['MES'].unique()

base_mensual = bbdd_in.groupby(['MES', 'CUENTA']).agg(cuentas_u = ('CUENTA', 'count')).reset_index()
base_mensual_2 = base_mensual.groupby(['CUENTA']).agg(Meses_reit = ('CUENTA', 'count')).reset_index()
base_mensual_3 = base_mensual.pivot(index='CUENTA', columns='MES', values='cuentas_u').reset_index()
compilado_meses_r = base_mensual_3.merge(base_mensual_2, how = 'left', on = 'CUENTA')
compilado_meses_r = compilado_meses_r.fillna(0)
print(compilado_meses_r)
conteo_inhibiciones_totales = generar_conteo_inhibiciones_totales(bbdd_in)
conteo_inhibiciones_reiteradas = generar_conteo_inhibiciones_reiteradas(bbdd_in)
conteo_inhibiciones_fuera_de_plazo = generar_conteo_inhibiciones_fuera_de_plazo(bbdd_in)

# Crear un nuevo archivo Excel
analisis_ihibiciones = pd.ExcelWriter("Analisis_inhibiciones_MR.xlsx", engine='xlsxwriter')

# Agregar las hojas con los conteos a Excel
conteo_inhibiciones_reiteradas.to_excel(analisis_ihibiciones, sheet_name='Inhibiciones Reiteradas', index=False)
conteo_inhibiciones_fuera_de_plazo.to_excel(analisis_ihibiciones, sheet_name='Inhibiciones Fuera de Plazo', index=False)

# Guardar el archivo Excel
analisis_ihibiciones.save()

def conteo_mes_a_mes_por_categoria(dataframe):
    conteo = dataframe.groupby(['MES', 'CATEGORIA'])['ID_ANDES'].count().reset_index()
    conteo_pivot = conteo.pivot(index='CATEGORIA', columns='MES', values='ID_ANDES').reset_index()
    return conteo_pivot

conteo_mes_a_mes = conteo_mes_a_mes_por_categoria(bbdd_in)
print(conteo_mes_a_mes)

analisis_inhibiciones = pd.ExcelWriter("Analisis_inhibiciones_MR_conteo_por_canal.xlsx", engine='xlsxwriter')
compilado_meses_r.to_excel(analisis_inhibiciones, sheet_name='meses reiterados', index=False)
conteo_mes_a_mes.to_excel(analisis_inhibiciones, sheet_name='conteo_mes_a_mes_por_categoria', index=False)
analisis_inhibiciones.save()