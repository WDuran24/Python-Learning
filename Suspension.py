import pandas as pd

# Cargar los archivos csv en dataframes
suspension = pd.read_csv((r"C:\Users\wduran\VTR GlobalCom S.A\Nicoll Constanza Aguirre Diaz - dcabello\ARPU Flujo\Suspension Transitoria\Consolidado Suspensiones Inputs\Suspension 202304.csv"),sep=";",encoding='latin-1')
reanudacion = pd.read_csv((r"C:\Users\wduran\VTR GlobalCom S.A\Nicoll Constanza Aguirre Diaz - dcabello\ARPU Flujo\Suspension Transitoria\Consolidado Suspensiones Inputs\Reanudacion 202304.csv"),sep=";",encoding='latin-1')
dx_voluntarias = pd.read_csv((r"C:\Users\wduran\VTR GlobalCom S.A\Nicoll Constanza Aguirre Diaz - dcabello\ARPU Flujo\Suspension Transitoria\Consolidado Suspensiones Inputs\DX Voluntarias 202304.csv"),sep=";",encoding='latin-1')
dx_mora = pd.read_csv((r"C:\Users\wduran\VTR GlobalCom S.A\Nicoll Constanza Aguirre Diaz - dcabello\ARPU Flujo\Suspension Transitoria\Consolidado Suspensiones Inputs\DX por Mora 202304.csv"),sep=";",encoding='latin-1')

# Hacer el join entre suspension y reanudacion, excluyendo los registros que coinciden
suspension_sin_reanudacion = pd.merge(suspension, reanudacion, on=['ID_ACTIVO', 'ID_CTA_FACT'], how='left', indicator=True)
suspension_sin_reanudacion = suspension_sin_reanudacion[suspension_sin_reanudacion['_merge'] == 'left_only']
suspension_sin_reanudacion.drop('_merge', axis=1, inplace=True)

# Hacer el join entre suspension_sin_reanudacion y dx_voluntarias, excluyendo los registros que coinciden
suspension_sin_dx_voluntarias = pd.merge(suspension_sin_reanudacion, dx_voluntarias, on='ID_CLIENTE', how='left', indicator=True)
suspension_sin_dx_voluntarias = suspension_sin_dx_voluntarias[suspension_sin_dx_voluntarias['_merge'] == 'left_only']
suspension_sin_dx_voluntarias.drop('_merge', axis=1, inplace=True)

# Hacer el join entre suspension_sin_dx_voluntariayo s y dx_mora, excluyendo los registros que coinciden
resultado_final = pd.merge(suspension_sin_dx_voluntarias, dx_mora, on='ID_CLIENTE', how='left', indicator=True)
resultado_final = resultado_final[resultado_final['_merge'] == 'left_only']
resultado_final.drop('_merge', axis=1, inplace=True)

# Guardar el resultado final en un archivo csv
resultado_final.to_csv('~/Downloads/Resultado Final.csv', index=False)




