import pandas as pd

# Cargar la base de datos "base pendiente validacion factibilidad"
pendiente_df = pd.read_excel(r"C:\Users\wduran\Downloads\Base Pendiente Validación Factibilidad.xlsx")

# Renombrar el campo IDEN_VIVIENDA a ID_VIVIENDA
pendiente_df.rename(columns={'IDEN_VIVIENDA': 'ID_VIVIENDA'}, inplace=True)

# Cargar la base de datos "data frame competencia" desde un archivo de texto
modelo_df = pd.read_csv(r"C:\Users\wduran\Desktop\GitHub Scripts\Python Exercises\Python-Exercises\DataFrame Competencia.txt", usecols=['MOVISTAR_FIBRA'], delimiter=',')  # Ajusta el delimitador si es necesario

# Realizar el join usando el campo ID_VIVIENDA
output_df = modelo_df.merge(pendiente_df, on='ID_VIVIENDA', how='left')

# Guardar el resultado en un nuevo archivo Excel
output_df.to_excel(r'C:\Users\wduran\Desktop\GitHub Scripts\Python Exercises\Python-Exercises\data_movi_rete.xlsx', index=False)



