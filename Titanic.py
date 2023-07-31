import pandas as pd

# Paso 1: Generar un DataFrame con los datos del fichero
df = pd.read_csv(r"C:\Users\wduran\Downloads\titanic (1).csv")

# Paso 2: Mostrar información básica del DataFrame
print("Dimensiones del DataFrame:", df.shape)
print("Número de datos:", df.size)
print("Nombres de las columnas:", df.columns.tolist())
print("Nombres de las filas (índices):", df.index.tolist())
print("Tipos de datos de las columnas:\n", df.dtypes)
print("Primeras 10 filas:\n", df.head(10))
print("Últimas 10 filas:\n", df.tail(10))

# Paso 3: Mostrar los datos del pasajero con identificador 148
print("Datos del pasajero con identificador 148:")
print(df.loc[147])

# Paso 4: Mostrar las filas pares del DataFrame
print("Filas pares del DataFrame:")
print(df.iloc[::2])

# Paso 5: Mostrar los nombres de las personas que iban en primera clase ordenadas alfabéticamente
first_class_names = df[df['Pclass'] == 1]['Name'].sort_values()
print("Nombres de personas en primera clase ordenados alfabéticamente:")
print(first_class_names)

# Paso 6: Mostrar el porcentaje de personas que sobrevivieron y murieron
survived_percentage = df['Survived'].mean() * 100
died_percentage = 100 - survived_percentage
print("Porcentaje de personas que sobrevivieron:", survived_percentage)
print("Porcentaje de personas que murieron:", died_percentage)

# Paso 7: Mostrar el porcentaje de personas que sobrevivieron en cada clase
survived_by_class = df.groupby('Pclass')['Survived'].mean() * 100
print("Porcentaje de personas que sobrevivieron en cada clase:")
print(survived_by_class)

# Paso 8: Eliminar del DataFrame los pasajeros con edad desconocida
df = df.dropna(subset=['Age'])

# Paso 9: Mostrar la edad media de las mujeres que viajaban en cada clase
mean_age_by_class_sex = df.groupby(['Pclass', 'Sex'])['Age'].mean()
print("Edad media de las mujeres que viajaban en cada clase:")
print(mean_age_by_class_sex)

# Paso 10: Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no
df['Minor'] = df['Age'] < 18

# Paso 11: Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase
survived_by_class_minor = df.groupby(['Pclass', 'Minor'])['Survived'].mean() * 100
print("Porcentaje de menores y mayores de edad que sobrevivieron en cada clase:")
print(survived_by_class_minor)
