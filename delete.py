import tkinter as tk
from tkinter import messagebox

tables_enabled = [{'name': 'hospital_a', 'Paciente_2': {'families': {'informacion_personal': {'nombre': {'value': 'Erick Bar', 'timestamp': 6543646465}}, 'antecedentes': {'registros': {'value': 'Si', 'timestamp': 4329540583}}, 'enfermedad': {'padece': {'value': 'Infeccion del estomago', 'timestamp': 2432685891}}}}}]


def search_and_delete():
    table_name = table_name_entry.get()
    row_id = row_id_entry.get()
    column_family = column_family_entry.get()

    # Buscar la tabla
    for table in tables_enabled:
        if table['name'] == table_name:
            if row_id in table:
                if column_family in table[row_id]['families']:
                    # Eliminar el valor
                    del table[row_id]['families'][column_family]
                    messagebox.showinfo("Éxito", "Valor eliminado con éxito.")
                    print(tables_enabled)  # Imprimir tables_enabled en la consola
                    return
                else:
                    messagebox.showerror("Error", f"No se encontró la column_family '{column_family}' en la tabla '{table_name}'.")
                    return
            else:
                messagebox.showerror("Error", f"No se encontró el row_id '{row_id}' en la tabla '{table_name}'.")
                return
    messagebox.showerror("Error", f"No se encontró la tabla '{table_name}'.")


def print_tables_enabled():
    print(tables_enabled)


# Crear ventana
window = tk.Tk()
window.title("Eliminador de Valores en Tablas")
window.geometry("300x200")

# Crear etiquetas y campos de entrada
table_name_label = tk.Label(window, text="Nombre de la Tabla:")
table_name_label.pack()
table_name_entry = tk.Entry(window)
table_name_entry.pack()

row_id_label = tk.Label(window, text="Row ID:")
row_id_label.pack()
row_id_entry = tk.Entry(window)
row_id_entry.pack()

column_family_label = tk.Label(window, text="Column Family:")
column_family_label.pack()
column_family_entry = tk.Entry(window)
column_family_entry.pack()

# Crear botón eliminar valor
delete_button = tk.Button(window, text="Eliminar Valor", command=search_and_delete)
delete_button.pack()

# Crear botón imprimir tables_enabled
print_button = tk.Button(window, text="Imprimir", command=print_tables_enabled)
print_button.pack()

window.mainloop()