# Ejercicio 32
# Este programa te creara la base de datos con su tabla si esta no existe.
# Ademas de que te podra mostrar los datos de esta misma.
import sqlite3
import tkinter as tk
from tkinter import messagebox
import os

directorioBD = 'data'
nombreBD = 'basquet.db'
rutaBD = os.path.join(directorioBD, nombreBD)
# Si la carpeta data no existe, la creara
if not os.path.exists(directorioBD):
    os.makedirs(directorioBD)
# Intentara conectarse a mi base datos y creara la tabla jugadores si no existe
try:
    conexionBD = sqlite3.connect(rutaBD)
    cursorBD = conexionBD.cursor()

    cursorBD.execute("""
        CREATE TABLE IF NOT EXISTS jugadores (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            apellido TEXT,
            altura REAL,
            edad INTEGER
        )
    """)

    conexionBD.commit()
    print('Base de datos creada exitosamente.')
except sqlite3.Error as error:
    print('Error al crear la base de datos:', error)
finally:
    if conexionBD:
        conexionBD.close()


# Función que ingresara datos a mi base de datos
def insertarDatos():
    conexionBD = sqlite3.connect('data/basquet.db')
    cursorDN = conexionBD.cursor()

    nombre = entryNombre.get()
    apellido = entryApellido.get()
    altura = entryAltura.get()
    edad = entryEdad.get()

    cursorDN.execute('INSERT INTO jugadores (nombre, apellido, altura, edad) VALUES (?, ?, ?, ?)',
                     (nombre, apellido, altura, edad))

    conexionBD.commit()
    conexionBD.close()

    entryNombre.delete(0, tk.END)
    entryApellido.delete(0, tk.END)
    entryAltura.delete(0, tk.END)
    entryEdad.delete(0, tk.END)

    messagebox.showinfo('Éxito', 'Los datos se han insertado correctamente.')


ventana = tk.Tk()
ventana.title('Inserción de Datos')

labelNombre = tk.Label(ventana, text='Nombre:')
entryNombre = tk.Entry(ventana)

labelApellido = tk.Label(ventana, text='Apellido:')
entryApellido = tk.Entry(ventana)

labelAltura = tk.Label(ventana, text='Altura:')
entryAltura = tk.Entry(ventana)

labelEdad = tk.Label(ventana, text='Edad:')
entryEdad = tk.Entry(ventana)

botonInsertar = tk.Button(ventana, text='Insertar Datos', command=insertarDatos)

labelNombre.grid(row=0, column=0)
entryNombre.grid(row=0, column=1)

labelApellido.grid(row=1, column=0)
entryApellido.grid(row=1, column=1)

labelAltura.grid(row=2, column=0)
entryAltura.grid(row=2, column=1)

labelEdad.grid(row=3, column=0)
entryEdad.grid(row=3, column=1)

botonInsertar.grid(row=4, column=0, columnspan=2)

ventana.mainloop()


# Función que me mostrara el contenido de mi base de datos
def mostrarContenidoBD():
    try:
        conexionBD = sqlite3.connect('data/basquet.db')
        cursorBD = conexionBD.cursor()

        cursorBD.execute('SELECT * FROM jugadores')

        filas = cursorBD.fetchall()

        for fila in filas:
            print(fila)
    except sqlite3.Error as error:
        print('Error al conectar a la base de datos:', error)
    finally:
        if conexionBD:
            conexionBD.close()


input('Presionar Enter para mostrar el contenido de la base de datos...')
mostrarContenidoBD()
