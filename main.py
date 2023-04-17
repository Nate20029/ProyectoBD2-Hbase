import tkinter as tk
import random

# Función para cerrar la ventana
def salir():
    ventana.destroy()


def ventana_put():

    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Create")


    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 390
    y = 265
    boton_volver.place(x=x, y=y)


# Función para crear la nueva ventana
def ventana_get():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Get")

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
        table['families'] = {}
        for family_name in column_families:
            family = {}
            family['row_key'] = last_row_key + 1
            family['Timestamp'] = random.randint(10**9, 10**10-1)
            family['value'] = f'val_{last_row_key+1}'
            last_row_key += 1
            table['families'][family_name] = family
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
        texto_salida.insert(tk.END, "Table\n")
        
            # Iterar sobre la lista de tablas y construir la salida
        for tabla in tables_enabled:
            # Obtener el nombre de la tabla
            tabla_name = tabla['name']
            # Obtener la cantidad de familias de la tabla
            tabla_families = len(tabla['families'])
            # Agregar la fila a la salida
            texto_salida.insert(tk.END, f"{tabla_name}\t{tabla_families} rows(s)\n")
        
        # Agregar el total de filas al final de la salida
        if len(tables_enabled) > 1:
            texto_salida.insert(tk.END, f"{len(tables_enabled)} rows(s)\n")
        else:
            texto_salida.insert(tk.END, f"{len(tables_enabled)} row(s)\n")
            
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



        # Define una función para modificar la definición de la tabla
    def alter_table_colum():
        # Obtener los valores actuales de los atributos que se van a modificar
        table_name = name_entry.get()
        old_family_name = old_family_entry.get()
        new_family_name = new_family_entry.get()

        # Buscar la tabla en la lista de tablas habilitadas
        table_found = False
        table_found = False
        for table in tables_enabled:
            if table['name'] == table_name:
                table_found = True
                # Modificar la definición de la tabla
                if old_family_name in table['families']:
                    new_families = {}
                    for key in table['families']:
                        if key == old_family_name:
                            new_families[new_family_name] = table['families'][old_family_name]
                        else:
                            new_families[key] = table['families'][key]
                    table['families'] = new_families
                    break

        if table_found:
            # Actualizar la etiqueta de estado
            status_label.config(text='La tabla ha sido modificada')
        else:
            # Actualizar la etiqueta de estado
            status_label.config(text='La tabla no ha sido encontrada')


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
    def describe_table(table_name):
        table_data = None
        table_type = None

        # buscar la tabla en la lista de habilitadas
        for table in tables_enabled:
            if table['name'] == table_name:
                table_data = table
                table_type = "ENABLE"
                break

        # buscar la tabla en la lista de deshabilitadas
        if not table_data:
            for table in tables_disabled:
                if table['name'] == table_name:
                    table_data = table
                    table_type = "DISABLE"
                    break

        # si la tabla no se encuentra en ninguna lista
        if not table_data:
            return f"Table {table_name} not found\n"

        # generar la salida para la tabla encontrada
        table_text = f"Table  {table_name} is {table_type}\n"
        table_text += f"{table_name}\n"
        for family_name, family_options in table_data['families'].items():
            table_text += f"\nNAME => {family_name}, "
            for option_name, option_value in family_options.items():
                table_text += f"{option_name} => {option_value}, "
        return table_text

    def show_table_info():
        table_name = table_name_entry.get()
        table_info = describe_table(table_name)
        result_label.config(text=table_info)


    # agregar un campo de texto para ingresar el nombre de la tabla
    table_name_label = tk.Label(ventana2, text="Table Name")
    table_name_label.pack()
    table_name_entry = tk.Entry(ventana2)
    table_name_entry.pack()

    # agregar un botón para simular el comando describe
    describe_button = tk.Button(ventana2, text="Describe", command=show_table_info)
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




