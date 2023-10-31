# Ejercicio 23
import os
from tkinter import filedialog as quelcom
import tkinter as tk
from PIL import Image, ImageTk

# Variables globales para almacenar la imagen seleccionada y su representación en ImageTk
imagenSeleccionada = None
imagenTk = None


# Función para abrir una imagen desde una carpeta
def abrirImagen():
    global imagenSeleccionada, imagenTk

    # Solicita al usuario que seleccione una carpeta de imágenes
    carpetaOrigen = quelcom.askdirectory(initialdir=os.getcwd(), title='Seleccionar una carpeta de imágenes')

    if carpetaOrigen:
        # Listar archivos en la carpeta y filtrar los que son imágenes .jpg
        archivos = os.listdir(carpetaOrigen)
        archivosImagen = [archivo for archivo in archivos if archivo.endswith('.jpg')]
        if not archivosImagen:
            etiquetaResultado.config(text='No se encontraron imágenes en la carpeta.')
            return

        # Seleccionar la primera imagen encontrada
        imagenSeleccionada = os.path.join(carpetaOrigen, archivosImagen[0])
        # Crea una ventana secundara para mostrar la imagen y su ruta
        ventanaSecundaria = tk.Toplevel()
        ventanaSecundaria.title('Imagen y ruta')

        # Crea una etiqueta con la ruta de la imagen
        etiquetaRuta = tk.Label(ventanaSecundaria, text=f'Ruta de la imagen:\n{imagenSeleccionada}')
        etiquetaRuta.pack()

        # Abre la imagen seleccionada y la muestra en una etiqueta
        imagen = Image.open(imagenSeleccionada)
        imagenTk = ImageTk.PhotoImage(imagen)
        etiquetaImagen = tk.Label(ventanaSecundaria, image=imagenTk)
        etiquetaImagen.image = imagenTk
        etiquetaImagen.pack()

        # Botón para guardar la imagen
        botonGuardar = tk.Button(ventanaSecundaria, text='Guardar', command=guardarImagen)
        botonGuardar.pack()


# Función para guardar la imagen
def guardarImagen():
    if imagenSeleccionada:
        # Solicitar al usuario una ubicación para guardar la imagem
        archivoGuardado = quelcom.asksaveasfile(defaultextension='.jpg', filetypes=[('Archivos de imagen', 'jpg')])
        if archivoGuardado:
            # Abrir la imagen original y guardarla en la ubicación seleccionada
            imagenOriginal = Image.open(imagenSeleccionada)
            imagenOriginal.save(archivoGuardado.name)
            archivoGuardado.close()
            etiquetaResultado.config(text='Imagen guardado correctamente.')


# Crea la ventana principal de la aplicación
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title('Abrir Imagen')

# Crear un botón para abrir una imagen
botonAbrir = tk.Button(ventanaPrincipal, text='Abrir Imagen', command=abrirImagen)
botonAbrir.pack()

# Etiqueta para mostrar el resultado o mensaje
etiquetaResultado = tk.Label(ventanaPrincipal, text='')
etiquetaResultado.pack()

# Inici la aplicación
ventanaPrincipal.mainloop()
