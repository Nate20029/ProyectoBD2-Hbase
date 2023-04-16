import tkinter as tk
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
    boton_volver = tk.Button(ventana2, text="put", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()


# Función para crear la nueva ventana
def ventana_get():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Get")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Hola", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()

# Función para crear la nueva ventana
def ventana_scan():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Scan")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Hola", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()

# Función para crear la nueva ventana
def ventana_delete():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Delete")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Hola", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()

# Función para crear la nueva ventana
def ventana_count():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Count")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Hola", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()

# Función para crear la nueva ventana
def ventana_truncate():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Truncate")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Hola", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()                

# Creamos una lista vacía para almacenar las tablas creadas
tablas_creadas = []

# Función para crear la nueva ventana
def ventana_create():

        # Definimos una función para crear la tabla
    def create_table(table_name, column_families):
        table = {}
        table['name'] = table_name
        table['families'] = {}
        for family in column_families:
            table['families'][family] = {}
        return table

    # Definimos una función que se ejecutará cuando el usuario presione el botón "Crear"
    def create_table_button_click():
        table_name = table_name_entry.get()
        column_families = column_families_entry.get().split(',')
        mi_tabla = create_table(table_name, column_families)
        tablas_creadas.append(mi_tabla)

    # Definimos una función que se ejecutará cuando el usuario presione el botón "Mostrar tablas"
    def mostrar_tablas_button_click():
        for tabla in tablas_creadas:
            print(tabla)

   
    
    
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Create")
    """
     # Creamos un botón para mostrar todas las tablas creadas
    mostrar_tablas_button = tk.Button(ventana2, text="Mostrar tablas", command=mostrar_tablas_button_click)
    mostrar_tablas_button.pack()

    """
    
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
        for tabla in tablas_creadas:
            # Obtener el nombre de la tabla
            tabla_name = tabla['name']
            # Obtener la cantidad de familias de la tabla
            tabla_families = len(tabla['families'])
            # Agregar la fila a la salida
            texto_salida.insert(tk.END, f"{tabla_name}\t{tabla_families} rows(s)\n")
        
        # Agregar el total de filas al final de la salida
        if len(tablas_creadas) > 1:
            texto_salida.insert(tk.END, f"{len(tablas_creadas)} rows(s)\n")
        else:
            texto_salida.insert(tk.END, f"{len(tablas_creadas)} row(s)\n")
            
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



# Función para crear la nueva ventana
def ventana_disable_enable():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Disable/Enable")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Regresar a Menú", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    x = 460
    y = 265
    boton_volver.place(x=x, y=y)


# Función para crear la nueva ventana
def ventana_alter():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Alter")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Hola", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()

# Función para crear la nueva ventana
def ventana_drop():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion drop")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Hola", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()

# Función para crear la nueva ventana
def ventana_describe():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()
    ventana2.title("Funcion Describe")

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Hola", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()

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




