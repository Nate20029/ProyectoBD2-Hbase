import tkinter as tk
import random
from tkinter import messagebox
from tkinter import ttk
import datetime

# Función para cerrar la ventana
def salir():
    ventana.destroy()

# Función para crear la nueva ventana
def ventana_datos():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Scan")

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


    # Crear campo de entrada para el número de datos
    label_num_datos = tk.Label(ventana2, text='Número de Datos:')
    label_num_datos.pack()
    entry_num_datos = tk.Entry(ventana2)
    entry_num_datos.pack()

    # Crear botón para generar datos
    btn_generar = tk.Button(ventana2, text='Generar', command=generar)
    btn_generar.pack()

    # Crear botón para mostrar datos
    btn_mostrar = tk.Button(ventana2, text='Mostrar', command=mostrar)
    btn_mostrar.pack()

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)

def ventana_put():
    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Put")

    # Función para simular el comando PUT
    def put_record():
        # Obtener los datos de la interfaz gráfica
        table_name = entry_table.get()
        row_key = entry_row_key.get()
        family_name = entry_family.get()
        column = entry_column.get()
        value = entry_value.get()

        # Buscar la tabla en la lista de habilitadas
        table_found = False
        for table in tables_enabled:
            if table['name'] == table_name:
                table_found = True

                # Verificar si la fila especificada está presente en la tabla
                if row_key not in table:
                    table[row_key] = {'families': {}}

                # Verificar si la familia especificada está presente en la tabla
                if family_name not in table[row_key]['families']:
                    table[row_key]['families'][family_name] = {}

                # Verificar si la columna especificada está presente en la familia especificada
                if column not in table[row_key]['families'][family_name]:
                    table[row_key]['families'][family_name][column] = {}

                # Agregar el registro a la columna especificada
                table[row_key]['families'][family_name][column]['value'] = value
                timestamp = str(random.randint(1000000000, 9999999999))
                table[row_key]['families'][family_name][column]['timestamp'] = timestamp

                # Mostrar mensaje de éxito
                label_result.config(text="Registro agregado exitosamente.")
                break

        # Mostrar mensaje de error si la tabla no existe
        if not table_found:
            label_result.config(text="La tabla especificada no existe.")

    # Definir la función para actualizar un registro en una tabla
    def update_record():
        # Obtener los datos de la interfaz gráfica
        table_name1 = entry_table1.get()
        row_key2 = entry_row_key1.get()
        family_name1 = entry_family1.get()
        column_name1 = entry_column_name1.get()
        new_value1 = entry_new_value1.get()

        # Buscar la tabla en la lista de habilitadas
        table_found = False
        for table in tables_enabled:
            if table['name'] == table_name1:
                table_found = True
                # Buscar el registro en la tabla
                if row_key2 in table:
                    # Buscar la familia en la tabla
                    if family_name1 in table[row_key2]['families']:
                        # Buscar el registro en la familia
                        if column_name1 in table[row_key2]['families'][family_name1]:
                            # Actualizar el valor del registro
                            table[row_key2]['families'][family_name1][column_name1]['value'] = new_value1
                            # Mostrar mensaje de éxito
                            label_result.config(text="Registro actualizado exitosamente.")
                        else:
                            # Mostrar mensaje de error si la columna no existe en el registro
                            label_result.config(text="La columna especificada no existe en el registro.")
                    else:
                        # Mostrar mensaje de error si la familia no existe en la tabla
                        label_result.config(text="La familia especificada no existe en la tabla.")
                else:
                    # Mostrar mensaje de error si el registro no existe en la tabla
                    label_result.config(text="El registro especificado no existe en la tabla.")
                break

        # Mostrar mensaje de error si la tabla no existe
        if not table_found:
            label_result.config(text="La tabla especificada no existe.")


    # Crear los elementos de la interfaz gráfica
    label_table = tk.Label(ventana2, text="Tabla:")
    label_table.grid(row=0, column=0, padx=5, pady=5)
    entry_table = tk.Entry(ventana2)
    entry_table.grid(row=0, column=1, padx=5, pady=5)

    label_row_key = tk.Label(ventana2, text="Clave:")
    label_row_key.grid(row=1, column=0, padx=5, pady=5)
    entry_row_key = tk.Entry(ventana2)
    entry_row_key.grid(row=1, column=1, padx=5, pady=5)

    label_family = tk.Label(ventana2, text="Familia:")
    label_family.grid(row=2, column=0, padx=5, pady=5)
    entry_family = tk.Entry(ventana2)
    entry_family.grid(row=2, column=1, padx=5, pady=5)

    label_column = tk.Label(ventana2, text="Columna:")
    label_column.grid(row=3, column=0, padx=5, pady=5)
    entry_column = tk.Entry(ventana2)
    entry_column.grid(row=3, column=1, padx=5, pady=5)

    label_value = tk.Label(ventana2, text="Valor:")
    label_value.grid(row=4, column=0, padx=5, pady=5)
    entry_value = tk.Entry(ventana2)
    entry_value.grid(row=4, column=1, padx=5, pady=5)

    button_put = tk.Button(ventana2, text="Agregar registro", command=put_record)
    button_put.grid(row=5, column=0, padx=5, pady=5)

    label_table1 = tk.Label(ventana2, text="Tabla:")
    x = 330
    y = 10
    label_table1.place(x=x, y=y)
    entry_table1 = tk.Entry(ventana2)
    x = 380
    y = 10
    entry_table1.place(x=x, y=y)

    label_row_key1 = tk.Label(ventana2, text="Clave:")
    x = 330
    y = 35
    label_row_key1.place(x=x, y=y)
    entry_row_key1 = tk.Entry(ventana2)
    x = 380
    y = 35
    entry_row_key1.place(x=x, y=y)

    label_family1 = tk.Label(ventana2, text="Familia:")
    x = 330
    y = 60
    label_family1.place(x=x, y=y)
    entry_family1 = tk.Entry(ventana2)
    x = 380
    y = 60
    entry_family1.place(x=x, y=y)

    label_column_name1 = tk.Label(ventana2, text="Nombre de la columna:")
    x = 330
    y = 85
    label_column_name1.place(x=x, y=y)
    entry_column_name1 = tk.Entry(ventana2)
    x = 380
    y = 85
    entry_column_name1.place(x=x, y=y)

    label_new_value1 = tk.Label(ventana2, text="Nuevo valor:")
    x = 330
    y = 110
    label_new_value1.place(x=x, y=y)
    entry_new_value1 = tk.Entry(ventana2)
    x = 410
    y = 110
    entry_new_value1.place(x=x, y=y)

    button_update = tk.Button(ventana2, text="Actualizar registro", command=update_record)
    x = 330
    y = 140
    button_update.place(x=x, y=y)

    label_result = tk.Label(ventana2, text="")
    label_result.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)



def ventana_get():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Get")

    # Crear un marco para los resultados
    result_frame = tk.Frame(ventana2)
    result_frame.pack(padx=10, pady=10)

    def get_data():
        # Limpiar el marco de resultados antes de agregar nuevos widgets
        for widget in result_frame.winfo_children():
            widget.destroy()

        table_name = table_name_entry.get()
        key = key_entry.get()

        data = next((item for item in tables_enabled if item.get("name") == table_name), None)
        if data:
            patient_data = data.get(key, None)
            if patient_data:
                families = patient_data.get("families", {})
                for family, family_data in families.items():
                    family_label = tk.Label(result_frame, text=f"{family}:")
                    family_label.pack(anchor="w")

                    for subkey, subdata in family_data.items():
                        timestamp = subdata.get("timestamp", "")
                        value = subdata.get("value", "")
                        sublabel_text = f"\t{subkey}\ttimestamp={timestamp}, value={value}"
                        sublabel = tk.Label(result_frame, text=sublabel_text)
                        sublabel.pack(anchor="w")
            else:
                messagebox.showerror("Error", "La llave no existe en la tabla.")
        else:
            messagebox.showerror("Error", "La tabla no existe o no está habilitada.")

        # Actualizar la ventana para mostrar los resultados
        ventana2.update()

    # Crear marco para los campos de entrada
    input_frame = tk.Frame(ventana2, padx=10, pady=10)
    input_frame.pack()

    # Campo de entrada para el nombre de la tabla
    table_name_label = tk.Label(input_frame, text="Nombre de la tabla:")
    table_name_label.grid(row=0, column=0)
    table_name_entry = tk.Entry(input_frame)
    table_name_entry.grid(row=0, column=1)

    # Campo de entrada para la llave
    key_label = tk.Label(input_frame, text="Llave:")
    key_label.grid(row=1, column=0)
    key_entry = tk.Entry(input_frame)
    key_entry.grid(row=1, column=1)

    # Botón para enviar los datos
    submit_button = tk.Button(ventana2, text="Consultar", command=get_data)
    submit_button.pack()

    ventana2.geometry("500x300")

    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)


# Función para crear la nueva ventana
def ventana_scan():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Scan")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)

# Función para crear la nueva ventana
def ventana_delete():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Delete")

   
    # Función para buscar un valor en la tabla
    def buscar_valor():
        # Obtiene el valor de búsqueda ingresado por el usuario
        valor = valor_entry.get()
        
        # Busca el valor en todas las filas y columnas de la tabla
        for fila, columnas in tables_enabled['name'].items():
            for familia, datos in columnas['families'].items():
                for columna, valores in datos.items():
                    if valor in valores.values():
                        # Imprime un mensaje que indica dónde se encontró el valor
                        print(f'Valor "{valor}" encontrado en la fila "{fila}", familia "{familia}", columna "{columna}"')
        
        # Si el valor no se encontró en la tabla, muestra un mensaje en la consola
        if valor not in str(tables_enabled):
            print(f'Valor "{valor}" no encontrado en la tabla')


    # Crea la etiqueta y la entrada para el valor de búsqueda
    valor_label = tk.Label(ventana2, text='Valor:')
    valor_entry = tk.Entry(ventana2)

    # Agrega los elementos a la ventana
    valor_label.pack(pady=5)
    valor_entry.pack()
    buscar_valor_btn = tk.Button(ventana2, text='Buscar valor', command=buscar_valor)
    buscar_valor_btn.pack(pady=10)



    ventana2.geometry("500x300")
   # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)

# Función para crear la nueva ventana
def ventana_count():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Count")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)

# Función para crear la nueva ventana
def ventana_truncate():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Truncate")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)                


# Función para crear la nueva ventana
def ventana_create():
    last_row_key = 1

        # Definimos una función para crear la tabla
    def create_table(table_name, column_families):
        table = {}
        last_row_key = 0
        table['name'] = table_name
        table['default'] = {'families': {}}
        for family_name in column_families:
            family = {}
            table['default']['families'][family_name] = family
        return table

    # Definimos una función que se ejecutará cuando el usuario presione el botón "Crear"
    def create_table_button_click():
        table_name = table_name_entry.get()
        column_families = column_families_entry.get().split(',')
        mi_tabla = create_table(table_name, column_families)
        tables_enabled.append(mi_tabla)

    # Definimos una función que se ejecutará cuando el usuario presione el botón "Mostrar tablas"
    def mostrar_tablas_button_click():
        for tabla in tables_enabled:
            print(tabla)

   
    
    
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Create")
    
     # Creamos un botón para mostrar todas las tablas creadas
    mostrar_tablas_button = tk.Button(ventana2, text="Mostrar tablas", command=mostrar_tablas_button_click)
    mostrar_tablas_button.pack()

    
    
    # Agregamos un label y un entry para el nombre de la tabla
    table_name_label = tk.Label(ventana2, text="Nombre de la tabla:")
    table_name_label.pack()
    table_name_entry = tk.Entry(ventana2)
    table_name_entry.pack()

    # Agregamos un label y un entry para las column families
    column_families_label = tk.Label(ventana2, text="Column Families (separadas por coma):")
    column_families_label.pack()
    column_families_entry = tk.Entry(ventana2)
    column_families_entry.pack()

    # Agregamos un botón para crear la tabla
    create_table_button = tk.Button(ventana2, text="Crear tabla", command=create_table_button_click)
    create_table_button.pack()

    # Agregamos un label para mostrar los resultados
    result_label = tk.Label(ventana2, text="")
    result_label.pack()



    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)


# Función para crear la nueva ventana
def ventana_list():

    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion List")

    def mostrar_tablas():
        # Limpiar cualquier texto existente en el widget Text
        texto_salida.delete('1.0', tk.END)

        # Agregar encabezado a la salida
        texto_salida.insert(tk.END, "Table\tFamilies\n")

        # Iterar sobre la lista de tablas y construir la salida
        for tabla in tables_enabled:
            # Obtener el nombre de la tabla y la cantidad de families
            tabla_name = tabla['name']
            tabla_families = len(list(tabla.values())[1]['families'])
            # Agregar la fila a la salida
            texto_salida.insert(tk.END, f"{tabla_name}\t{tabla_families}\n")

        # Agregar un separador de línea
        texto_salida.insert(tk.END, '-'*20)        

    # Agregar un widget Text para mostrar la salida
    texto_salida = tk.Text(ventana2, height=10, width=40)
    texto_salida.pack()

    # Agregar un botón para mostrar la lista de tablas
    boton_mostrar = tk.Button(ventana2, text="Mostrar tablas", command=mostrar_tablas)
    boton_mostrar.pack()

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)


tables_enabled = []
tables_disabled = []

# Función para crear la nueva ventana
def ventana_disable_enable():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Disable/Enable")

        # Crear una etiqueta y un campo de entrada para el nombre de la tabla
    label_table1 = tk.Label(ventana2, text="Nombre de la tabla:")
    x = 200
    y = 75
    label_table1.place(x=x, y=y)
    entry_table1 = tk.Entry(ventana2)
    x = 200
    y = 95
    entry_table1.place(x=x, y=y)

    def enable_table():
        table_name = entry_table1.get()
        table_found = False
        for table in tables_disabled:
            if table['name'] == table_name:
                # Mover la tabla de la lista de tablas deshabilitadas a la lista de tablas habilitadas
                tables_disabled.remove(table)
                tables_enabled.append(table)
                message = f"La tabla '{table_name}' ha sido habilitada."
                label_message.config(text=message)
                table_found = True
                break
        if not table_found:
            message = f"La tabla '{table_name}' no se encontró o ya está habilitada."
            label_message.config(text=message)


    def disable_table():
        table_name = entry_table.get()
        table_found = False
        for table in tables_enabled:
            if table['name'] == table_name:
                # Mover la tabla de la lista de tablas habilitadas a la lista de tablas deshabilitadas
                tables_enabled.remove(table)
                tables_disabled.append(table)
                message = f"La tabla '{table_name}' ha sido deshabilitada."
                label_message.config(text=message)
                table_found = True
                break
        if not table_found:
            message = f"La tabla '{table_name}' no se encontró o ya está deshabilitada."
            label_message.config(text=message)

        # Crear una etiqueta y un campo de entrada para el nombre de la tabla
    label_table = tk.Label(ventana2, text="Nombre de la tabla:")
    x = 10
    y = 75
    label_table.place(x=x, y=y)
    entry_table = tk.Entry(ventana2)
    x = 10
    y = 100
    entry_table.place(x=x, y=y)

    # Crear un botón para deshabilitar la tabla
    button_disable = tk.Button(ventana2, text="Deshabilitar tabla", command=disable_table)
    x = 10
    y = 130
    button_disable.place(x=x, y=y)


    # Crear un botón para habilitar la tabla
    button_enable1 = tk.Button(ventana2, text="Habilitar tabla", command=enable_table)
    x = 200
    y = 130
    button_enable1.place(x=x, y=y)


    # Crear un Label para mostrar el mensaje
    label_message = tk.Label(ventana2, text="")
    label_message.pack()


    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)


# Función para crear la nueva ventana
def ventana_alter():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Alter")

    """
    # Define una función para modificar la definición de la tabla
    def alter_table_name():
        # Obtener los valores actuales de los atributos que se van a modificar
        table_name = name_entry1.get()

        # Buscar la tabla en la lista de tablas habilitadas
        table_found = False
        for table in tables_enabled:
            if table['name'] == table_name:
                table_found = True
                # Modificar la definición de la tabla
                table['name'] = new_name_entry1.get()

        if table_found:
            # Actualizar la etiqueta de estado
            status_label.config(text='La tabla ha sido modificada')
        else:
            # Actualizar la etiqueta de estado
            status_label.config(text='La tabla no ha sido encontrada')


    # Crear las entradas de texto para los atributos
    name_label1 = tk.Label(ventana2, text='Nombre de la tabla')
    name_entry1 = tk.Entry(ventana2)
    new_name_label1 = tk.Label(ventana2, text='Nuevo nombre de la tabla')
    new_name_entry1 = tk.Entry(ventana2)

    # Crear el botón para modificar la tabla
    alter_button = tk.Button(ventana2, text='Modificar tabla', command=alter_table_name)

    # Crear la etiqueta de estado
    status_label = tk.Label(ventana2, text='')

    # Mostrar los elementos en la ventana
    x = 300
    y = 35
    name_label1.place(x=x, y=y)
    x = 300
    y = 55
    name_entry1.place(x=x, y=y)
    x = 300
    y = 75
    new_name_label1.place(x=x, y=y)
    x = 300
    y = 95
    new_name_entry1.place(x=x, y=y)
    x = 300
    y = 115
    alter_button.place(x=x, y=y)
    x = 300
    y = 125
    status_label.place(x=x, y=y)
    """


        # Define una función para modificar la definición de la tabla
    def alter_table_colum():
        # Obtener los nombres de la tabla y las familias a modificar desde las entradas de la GUI
        table_name = name_entry.get()
        old_family_name = old_family_entry.get()
        new_family_name = new_family_entry.get()

        # Buscar la tabla en la lista de tablas habilitadas
        table_found = False
        for table in tables_enabled:
            if table['name'] == table_name:
                table_found = True

                # Buscar la familia en el diccionario de familias del paciente
                patient_data = table.get(list(table.keys())[1])
                families_data = patient_data.get('families', {})
                if old_family_name in families_data:
                    family_data = families_data.pop(old_family_name)
                    families_data[new_family_name] = family_data
                    break

        # Mostrar mensaje de éxito o error
        if table_found:
            messagebox.showinfo('Éxito', f'Se ha modificado la familia de columnas "{old_family_name}" a "{new_family_name}" en la tabla "{table_name}"')
        else:
            messagebox.showerror('Error', f'La tabla "{table_name}" no se encuentra habilitada')

    # Crear las entradas de texto para los atributos
    name_label = tk.Label(ventana2, text='Nombre de la tabla')
    name_entry = tk.Entry(ventana2)
    old_family_label = tk.Label(ventana2, text='Nombre de la familia de columnas a modificar')
    old_family_entry = tk.Entry(ventana2)
    new_family_label = tk.Label(ventana2, text='Nuevo nombre de la familia de columnas')
    new_family_entry = tk.Entry(ventana2)

    # Crear el botón para modificar la tabla
    alter_button = tk.Button(ventana2, text='Modificar tabla', command=alter_table_colum)

    # Crear la etiqueta de estado
    status_label = tk.Label(ventana2, text='')

    # Mostrar los elementos en la ventana
    x = 10
    y = 35
    name_label.place(x=x, y=y)
    x = 10
    y = 55
    name_entry.place(x=x, y=y)
    x = 10
    y = 75
    old_family_label.place(x=x, y=y)
    x = 10
    y = 95
    old_family_entry.place(x=x, y=y)
    x = 10
    y = 125
    new_family_label.place(x=x, y=y)
    x = 10
    y = 145
    new_family_entry.place(x=x, y=y)
    x = 10
    y = 165
    alter_button.place(x=x, y=y)


    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)

# Función para crear la nueva ventana
def ventana_drop():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion drop")

    def drop_table(table_name):
        for i, table in enumerate(tables_enabled):
            if table['name'] == table_name:
                del tables_enabled[i]
                print(f"La tabla {table_name} ha sido eliminada con éxito.")
                return True
        print(f"No se encontró la tabla {table_name}.")
        return False
    
    def drop_all_tables():
        tables_enabled.clear()
        print("Todas las tablas han sido eliminadas con éxito.")
    
    # Crear los widgets
    table_name_label = tk.Label(ventana2, text="Nombre de la tabla:")
    table_name_entry = tk.Entry(ventana2)
    drop_table_button = tk.Button(ventana2, text="Eliminar tabla", command=lambda: drop_table(table_name_entry.get()))
    message_label = tk.Label(ventana2, text="")
    drop_alltable_button = tk.Button(ventana2, text="Eliminar todas las tablas", command=drop_all_tables)
    message_alllabel = tk.Label(ventana2, text="")
    
    # Posicionar los widgets en la ventana
    table_name_label.pack()
    table_name_entry.pack()
    drop_table_button.pack()
    message_label.pack()
    drop_alltable_button.pack()
    message_alllabel.pack()

    ventana2.geometry("500x300")
    
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)

# Función para crear la nueva ventana
def ventana_describe():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Describe")

    # función para simular el comando describe
    def describe_table(table_name_entry):
        table_data = None
        table_type = None

        # buscar la tabla en la lista de habilitadas
        for table in tables_enabled:
            if table['name'] == table_name_entry:
                table_data = table
                table_type = "ENABLE"
                break

        # buscar la tabla en la lista de deshabilitadas
        if not table_data:
            for table in tables_disabled:
                if table['name'] == table_name_entry:
                    table_data = table
                    table_type = "DISABLE"
                    break

        # si la tabla no se encuentra en ninguna lista
        if not table_data:
            return f"Table {table_name_entry} not found\n"

        # generar la salida para la tabla encontrada
        table_text = f"Table  {table_name_entry} is {table_type}\n"
        table_text += f"{table_name_entry}\n"

        # buscar el valor que contiene la clave 'families' en el diccionario
        for value in table_data.values():
            if isinstance(value, dict) and 'families' in value:
                families = value['families']
                break

        # agregar los datos de cada familia al texto de salida
        for family_name, family_data in families.items():
            table_text += f"\nNAME => {family_name}\n"
            for attribute_name, attribute_data in family_data.items():
                value = attribute_data.get('value', '')
                timestamp = attribute_data.get('timestamp', '')
                table_text += f"{attribute_name}: {value} (timestamp: {timestamp})\n"

        return table_text

    

    # agregar un campo de texto para ingresar el nombre de la tabla
    table_name_label = tk.Label(ventana2, text="Table Name")
    table_name_label.pack()
    table_name_entry = tk.Entry(ventana2)
    table_name_entry.pack()

    # agregar un botón para simular el comando describe
    describe_button = tk.Button(ventana2, text="Describe", command=lambda: result_label.config(text=describe_table(table_name_entry.get())))
    describe_button.pack()

    # agregar una etiqueta para mostrar el resultado de describe
    result_label = tk.Label(ventana2, text="")
    result_label.pack()

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulación de Hbase")




# Etiqueta de bienvenida
etiqueta_bienvenida = tk.Label(ventana, text="Bienvenido a la simulación de Hbase")
etiqueta_bienvenida.pack()

# Etiqueta de Funciones
etiqueta_funciones = tk.Label(ventana, text="Listado de Funciones disponibles: ")
etiqueta_funciones.pack()
x = 10
y = 30
etiqueta_funciones.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="DATOS", command=ventana_datos)
x = 150
y = 70
boton.place(x=x, y=y)


# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="PUT", command=ventana_put)
x = 10
y = 70
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="GET", command=ventana_get)
x = 10
y = 100
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="SCAN", command=ventana_scan)
x = 10
y = 130
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="DELETE", command=ventana_delete)
x = 10
y = 160
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="COUNT", command=ventana_count)
x = 10
y = 190
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="TRUNCATE", command=ventana_truncate)
x = 10
y = 220
boton.place(x=x, y=y)



# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="CREATE", command=ventana_create)
x = 300
y = 70
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="LIST", command=ventana_list)
x = 300
y = 100
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="DISABLE/ENABLE", command=ventana_disable_enable)
x = 300
y = 130
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="ALTER", command=ventana_alter)
x = 300
y = 160
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="DROP", command=ventana_drop)
x = 300
y = 190
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="DESCRIBE", command=ventana_describe)
x = 300
y = 220
boton.place(x=x, y=y)

"""
# Crear una etiqueta para mostrar los datos ingresados
etiqueta_datos = tk.Label(ventana, text="")
etiqueta_datos.pack()

# Área de ingreso de datos
area_ingreso = tk.Entry(ventana)
x = 10
y = 100
area_ingreso.place(x=x, y=y)

# Función para actualizar la etiqueta de datos
def actualizar_datos():
    datos_ingresados = area_ingreso.get()
    etiqueta_datos.config(text="Datos ingresados: " + datos_ingresados)

# Asociar la función actualizar_datos con el evento KeyRelease del widget area_ingreso
area_ingreso.bind("<KeyRelease>", lambda event: actualizar_datos())

# Función para manejar el evento Enter en el área de ingreso de datos
def ingresar_datos(event):
    global datos
    datos = area_ingreso.get()
    etiqueta_datos.config(text="Datos ingresados: " + datos)
    area_ingreso.delete(0, tk.END)
    area_ingreso.focus_set()

# Asociar la función ingresar_datos con el evento <Return> del widget area_ingreso
area_ingreso.bind("<Return>", ingresar_datos)
"""


# Botón de salida
boton_salir = tk.Button(ventana, text="Salir", command=salir)
x = 460
y = 265
boton_salir.place(x=x, y=y)




# Mostrar la ventana
ventana.geometry("500x300")
ventana.mainloop()




