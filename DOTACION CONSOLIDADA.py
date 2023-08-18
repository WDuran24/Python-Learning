import pandas as pd

# Cargar el dataframe desde el archivo CSV
ini_completas_df = pd.read_csv(r'C:\Users\wduran\Downloads\ini_COMPLETAS.csv', sep=';')

# Cargar el dataframe desde el archivo Excel
dotacion_df = pd.read_excel(r'C:\Users\wduran\Downloads\Dotacion Consolidada (2).xlsx')

# Limpiar los nombres de las columnas
ini_completas_df.columns = ini_completas_df.columns.str.strip()
dotacion_df.columns = dotacion_df.columns.str.strip()

# Crear una nueva columna en ambos dataframes para la concatenación de mes y año
ini_completas_df['MES_ANO'] = ini_completas_df['MES'].astype(str) + '-' + ini_completas_df['ANO'].astype(str)
dotacion_df['MES_ANO'] = dotacion_df['MES'].astype(str) + '-' + dotacion_df['ANO'].astype(str)

# Realizar el join en base a USUARIO y MES_ANO
merged_df = ini_completas_df.merge(
    dotacion_df[['USUARIO', 'MES_ANO', 'Categoria']],
    how='left',
    on=['USUARIO', 'MES_ANO']
)

# Guardar el resultado en un nuevo archivo CSV
merged_df.to_csv(r'C:\Users\wduran\Downloads\Resultado_Join.csv', index=False,sep=';')
