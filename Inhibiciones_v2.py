import pandas as pd
import numpy as np
import datetime

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