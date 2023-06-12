import pandas as pd

# Leer el archivo LEGAXY
legaxy = pd.read_excel(r"C:\Users\wduran\Downloads\Legacy baja velocidad.xlsx")

# Crear el campo UNION en el DataFrame LEGAXY
legaxy['UNION'] = legaxy['ID_CLIENTE'].astype(str) + '-' + legaxy['ID_VIVIENDA'].astype(str)

# Leer el archivo assets
assets = pd.read_csv(r"C:\Users\wduran\Downloads\Assets Modelo Equipo.csv")

# Crear el campo UNION en el DataFrame assets
assets['UNION'] = assets['ID_CLIENTE'].astype(str) + '-' + assets['ID_VIVIENDA'].astype(str)

# Realizar el join entre los DataFrames legaxy y assets usando el campo UNION
final_legaxy = pd.merge(assets, legaxy, on='UNION',how="left")

# Leer el archivo nomenclatura
nomenclatura = pd.read_excel(r"C:\Users\wduran\Downloads\Nomenclaturas equipos vel max internet Junio 2023.xlsx")

# Realizar el join entre el DataFrame final_legaxy y la tabla nomenclatura usando el campo MODELO_EQUIPO
final_stock_legaxy = pd.merge(final_legaxy, nomenclatura, on='MODELO_EQUIPO',how="inner")

# Seleccionar los campos UNION, MARCA, MODELO y Vel Max
final_stock_legaxy = final_stock_legaxy[['UNION', 'MARCA_EQUIPO', 'MODELO_EQUIPO', 'Vel Max']]

# Guardar el DataFrame final_definitivo en un archivo Excel
final_stock_legaxy.to_excel('final_definitivo.xlsx', index=False)
