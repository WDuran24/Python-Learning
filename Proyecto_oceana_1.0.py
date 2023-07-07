import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

# Función para proyectar los ingresos
def proyectar_ingresos(Habitaciones, baños, Oceanview):
    # Cargar el archivo Excel
    data = pd.read_excel(r"C:\Users\wduran\Desktop\GitHub Scripts\Python Exercises\Python-Exercises\base_de_datos.xlsx")

    # Filtrar las unidades que coinciden con los parámetros ingresados por el usuario
    unidades_filtradas = data[(data['Habitaciones'] == Habitaciones) & (data['Baños'] == baños) & (data['Oceanview'] == Oceanview)]

    # Calcular los ingresos promedio mensuales para las unidades filtradas
    ingresos_promedio_mensuales = unidades_filtradas['Revenue']

    # Crear una lista con las proyecciones de ingresos para los próximos 12 meses
    proyeccion_ingresos = [ingresos_promedio_mensuales.sum()] * 12

    # Generar el gráfico de barras
    meses = ['Mes {}'.format(i) for i in range(1, 13)]
    plt.bar(meses, proyeccion_ingresos)
    plt.xlabel('Mes')
    plt.ylabel('Ingresos')
    plt.title('Proyección de ingresos para los próximos 12 meses')
    plt.show()

# Función para manejar el evento del botón en la interfaz gráfica
def generar_grafico():
    habitaciones = int(habitaciones_entry.get())
    banos = int(banos_entry.get())
    ocean_view = bool(ocean_view_entry.get())
    proyectar_ingresos(habitaciones, banos, ocean_view)

# Crear la interfaz gráfica con Tkinter
root = Tk()
root.title('Proyección de ingresos')

# Etiquetas
Label(root, text='Habitaciones:').grid(row=0, column=0, sticky=W)
Label(root, text='Baños:').grid(row=1, column=0, sticky=W)
Label(root, text='Ocean View:').grid(row=2, column=0, sticky=W)

# Entradas de texto
habitaciones_entry = Entry(root)
habitaciones_entry.grid(row=0, column=1)
banos_entry = Entry(root)
banos_entry.grid(row=1, column=1)
ocean_view_entry = Entry(root)
ocean_view_entry.grid(row=2, column=1)

# Botón para generar el gráfico
Button(root, text='Generar Gráfico', command=generar_grafico).grid(row=3, column=0, columnspan=2)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()

#metros cuadrados,piscina climatizada,max ocupacion,ubicacion, sacar porcentaje de mercado general y dividirlo mensual segun distribucion porcentual.Enero cuanto representa en revenue?
