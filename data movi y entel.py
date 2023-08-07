# Ruta del archivo de entrada y salida
ruta_archivo_entrada =r"C:\Users\wduran\Downloads\TABLON_AVAR_28012021.txt"
ruta_archivo_salida = "C:/Users\wduran\Desktop/GitHub Scripts/Python Exercises/Python-Exercises/nuevo_archivo.txt"

# Leer el contenido del archivo de entrada
with open(ruta_archivo_entrada, "r") as archivo_entrada:
    contenido = archivo_entrada.read()

# Reemplazar el separador "~" por una coma ","
contenido_modificado = contenido.replace("~", ",")

# Escribir el contenido modificado en el nuevo archivo de salida
with open(ruta_archivo_salida, "w") as archivo_salida:
    archivo_salida.write(contenido_modificado)

print("Proceso completado. El archivo modificado se ha guardado en:", ruta_archivo_salida)


