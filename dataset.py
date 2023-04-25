# Nombre del archivo CSV
nombre_archivo = 'datos_hospital.csv'

# Variable para almacenar los datos del archivo CSV
datos_csv = ''

# Abrir el archivo CSV en modo lectura
with open(nombre_archivo, 'r') as archivo:
    # Leer todo el contenido del archivo CSV y almacenarlo en la variable datos_csv
    datos_csv = archivo.read()

# Imprimir los datos leídos del archivo CSV
print(datos_csv)



