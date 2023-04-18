import random
import tkinter as tk
from tkinter import messagebox

tables_enabled = []

def generar_datos_aleatorios(num_datos):
    datos = []
    numeros_hospitales = set() # Conjunto para almacenar los números de hospitales generados
    for _ in range(num_datos):
        datos_hospital = {}
        numero_hospital = random.randint(1, 1000)
        # Verificar que el número de hospital no se repita
        while numero_hospital in numeros_hospitales:
            numero_hospital = random.randint(1, 1000)
        numeros_hospitales.add(numero_hospital)
        datos_hospital['name'] = f'hospital_{numero_hospital}'
        paciente_numero = random.randint(1, 100)
        paciente_key = 'Paciente_' + str(paciente_numero)
        datos_hospital[paciente_key] = {}
        datos_hospital[paciente_key]['families'] = {}
        datos_hospital[paciente_key]['families']['informacion_personal'] = {}
        datos_hospital[paciente_key]['families']['informacion_personal']['nombre'] = {}
        datos_hospital[paciente_key]['families']['informacion_personal']['nombre']['value'] = generar_nombre_aleatorio()
        datos_hospital[paciente_key]['families']['informacion_personal']['nombre']['timestamp'] = generar_timestamp()
        datos_hospital[paciente_key]['families']['antecedentes'] = {}
        datos_hospital[paciente_key]['families']['antecedentes']['registros'] = {}
        datos_hospital[paciente_key]['families']['antecedentes']['registros']['value'] = generar_registro_aleatorio()
        datos_hospital[paciente_key]['families']['antecedentes']['registros']['timestamp'] = generar_timestamp()
        datos_hospital[paciente_key]['families']['enfermedad'] = {}
        datos_hospital[paciente_key]['families']['enfermedad']['padece'] = {}
        datos_hospital[paciente_key]['families']['enfermedad']['padece']['value'] = generar_enfermedad_aleatoria()
        datos_hospital[paciente_key]['families']['enfermedad']['padece']['timestamp'] = generar_timestamp()
        datos.append(datos_hospital)

    return datos

def generar_nombre_aleatorio():
    nombres = ['Kevin Eagle', 'Erick Bar', 'Luisa Smith', 'María Rodríguez', 'Pedro Pérez', 'Ana Gómez']
    return random.choice(nombres)

def generar_registro_aleatorio():
    opciones = ['Si', 'No']
    return random.choice(opciones)

def generar_enfermedad_aleatoria():
    enfermedades = ['Infección del oído', 'Infección del estómago', 'Gripe', 'Asma', 'Diabetes']
    return random.choice(enfermedades)

def generar_timestamp():
    return random.randint(1000000000, 9999999999)

def generar():
    try:
        num_datos = int(entry_num_datos.get())
        nuevos_datos = generar_datos_aleatorios(num_datos)
        # Agregar los nuevos datos a la lista de datos habilitados
        tables_enabled.extend(nuevos_datos)
        messagebox.showinfo('Datos generados', f'Se generaron y se añadieron a la lista {num_datos} datos aleatorios.')
    except ValueError:
        messagebox.showerror('Error', 'Por favor ingrese un número válido para la cantidad de datos a generar.')

def mostrar():
    contenido = ''
    for dato in tables_enabled:
        contenido += str(dato) + '\n'
    messagebox.showinfo('Datos Habilitados', contenido)

# Crear ventana
ventana = tk.Tk()
ventana.title('Generador de Datos Aleatorios')

# Crear campo de entrada para el número de datos
label_num_datos = tk.Label(ventana, text='Número de Datos:')
label_num_datos.pack()
entry_num_datos = tk.Entry(ventana)
entry_num_datos.pack()

# Crear botón para generar datos
btn_generar = tk.Button(ventana, text='Generar', command=generar)
btn_generar.pack()

# Crear botón para mostrar datos
btn_mostrar = tk.Button(ventana, text='Mostrar', command=mostrar)
btn_mostrar.pack()

ventana.mainloop()