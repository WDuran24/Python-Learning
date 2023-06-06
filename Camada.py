import pandas as pd

# Leer el archivo Excel "inhibiciones febrero"
df_inhibiciones_Febrero = pd.read_excel("C:/Users/wduran/VTR GlobalCom S.A/Nicoll Constanza Aguirre Diaz - dcabello/ARPU Flujo/Piloto Cobranzas VTR/inhibiciones febrero 2023.xlsx")
df_inhibiciones_Marzo = pd.read_excel("C:/Users/wduran/VTR GlobalCom S.A/Nicoll Constanza Aguirre Diaz - dcabello/ARPU Flujo/Piloto Cobranzas VTR/inhibiciones marzo 2023.xlsx")
df_inhibiciones_Abril = pd.read_excel("C:/Users/wduran/VTR GlobalCom S.A/Nicoll Constanza Aguirre Diaz - dcabello/ARPU Flujo/Piloto Cobranzas VTR/inhibiciones abril 2023.xlsx")
df_inhibiciones_Mayo = pd.read_excel("C:/Users/wduran/VTR GlobalCom S.A/Nicoll Constanza Aguirre Diaz - dcabello/ARPU Flujo/Piloto Cobranzas VTR/inhibiciones mayo 2023.xlsx")

# Contar los registros únicos en el campo "rut"
conteo_rut_febrero = df_inhibiciones_Febrero["RUT"].nunique()
print("Conteo de registros únicos en febrero 'rut':", conteo_rut_febrero)
conteo_rut_marzo = df_inhibiciones_Marzo["RUT"].nunique()
print("Conteo de registros únicos en marzo 'rut':", conteo_rut_marzo)
conteo_rut_abril = df_inhibiciones_Abril["RUT"].nunique()
print("Conteo de registros únicos en abril 'rut':", conteo_rut_abril)
conteo_rut_mayo = df_inhibiciones_Mayo["RUT"].nunique()
print("Conteo de registros únicos en mayo 'rut':", conteo_rut_mayo)
# Leer el archivo Excel "tabla E"
df_tabla_e = pd.read_csv("C:/Users/wduran/VTR GlobalCom S.A/Nicoll Constanza Aguirre Diaz - dcabello/Dashboards Nueva Oferta/INPUTS/Tablas E/20230531_StockTotal.csv")

# Contar los registros únicos en el campo "RUT_PERSONA" que también aparecen en "inhibiciones febrero"
camada_febrero = df_tabla_e[df_tabla_e["RUT_PERSONA"].isin(df_inhibiciones_Febrero["RUT"].unique())]["RUT_PERSONA"].nunique()
print("Cantidad de registros únicos de febrero en el campo 'RUT_PERSONA' que aparecen en 'tabla E':", camada_febrero)
camada_marzo = df_tabla_e[df_tabla_e["RUT_PERSONA"].isin(df_inhibiciones_Marzo["RUT"].unique())]["RUT_PERSONA"].nunique()
print("Cantidad de registros únicos de marzo en el campo 'RUT_PERSONA' que aparecen en 'tabla E':", camada_marzo)
camada_abril = df_tabla_e[df_tabla_e["RUT_PERSONA"].isin(df_inhibiciones_Abril["RUT"].unique())]["RUT_PERSONA"].nunique()
print("Cantidad de registros únicos de abril en el campo 'RUT_PERSONA' que aparecen en 'tabla E':", camada_abril)
camada_mayo = df_tabla_e[df_tabla_e["RUT_PERSONA"].isin(df_inhibiciones_Mayo["RUT"].unique())]["RUT_PERSONA"].nunique()
print("Cantidad de registros únicos de mayo en el campo 'RUT_PERSONA' que aparecen en 'tabla E':", camada_mayo)

# Restar para determinar Q de Clientes Desconectados

print("Cantidad de clientes DX en Febrero :",conteo_rut_febrero-camada_febrero)
print("Cantidad de clientes DX en Marzo :",conteo_rut_marzo-camada_marzo)
print("Cantidad de clientes DX en Abril:",conteo_rut_abril-camada_abril)
print("Cantidad de clientes DX en Mayo :",conteo_rut_mayo-camada_mayo)