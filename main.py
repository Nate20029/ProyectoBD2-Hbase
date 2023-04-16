
import tkinter as tk

# Función para cerrar la ventana
def salir():
    ventana.destroy()

# Función para crear la nueva ventana
def ventana_put():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()

    ventana2.geometry("500x300")
    # Agregar un botón a la nueva ventana que cierre la ventana actual y muestre la ventana principal de nuevo
    boton_volver = tk.Button(ventana2, text="Volver a ventana principal", command=lambda:[ventana2.destroy(), ventana.deiconify()])
    boton_volver.pack()


# Función para crear la nueva ventana
def ventana_get():
    # Ocultar la ventana principal
    ventana.withdraw()

    # Crear una nueva ventana
    ventana2 = tk.Toplevel()

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
y = 50
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
boton = tk.Button(ventana, text="SCAN", command=ventana_get)
x = 10
y = 130
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="DELETE", command=ventana_get)
x = 10
y = 160
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="COUNT", command=ventana_get)
x = 10
y = 190
boton.place(x=x, y=y)

# Agregar un botón a la ventana principal que abra una nueva ventana al hacer clic
boton = tk.Button(ventana, text="TRUNCATE", command=ventana_get)
x = 10
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
