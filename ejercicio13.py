# Ejercicio 13 y 14
import os
from tkinter import *
from PIL import ImageTk, Image

# Directorio que contiene las imágenes
rutaDirectorio = "./imagenes"
# Lista de nombres de archivos de imágenes en el directorio
listaImagenes = os.listdir(rutaDirectorio)

# Índice de la imagen actual
indiceActual = 0
# Lista para almacenar objetos PhotoImage de las imágenes
photoImages = []


# Función para mostrar la imagen actual
def mostrarImage():
    global indiceActual

    # Si ya hay una imagen mostrada, eliminarla
    if hasattr(mostrarImage, "imagenLabel"):
        mostrarImage.imagenLabel.grid_forget()

    # Ruta de la imagen actual
    imagenPath = os.path.join(rutaDirectorio, listaImagenes[indiceActual])
    print(imagenPath)

    # Abre la imagen con la biblioteca PIL (Pillow)
    imagen = Image.open(imagenPath)
    # Convierte la imagen a un objeto PhotoImage
    photo = ImageTk.PhotoImage(imagen)
    photoImages.append(photo)

    # Crea una etiqueta para mostrar la imagen en la ventana
    mostrarImage.imagenLabel = Label(root, image=photo)
    mostrarImage.imagenLabel.grid(row=0, column=0, padx=10, pady=10)

    # Configura el estado de los botones "Anterior" y "Siguiente" según la posición actual
    if indiceActual == 0:
        botonAnterior.config(state=DISABLED)
    else:
        botonAnterior.config(state=NORMAL)


    if indiceActual == len(listaImagenes) - 1:
        botonSiguiente.config(state=DISABLED)
    else:
        botonSiguiente.config(state=NORMAL)

    # Actualiza la etiqueta de información con el número de imagen actual
    infoEtiqueta.config(text=f"Imatge {indiceActual + 1} de {len(listaImagenes)}")


# Función para mostrar la siguiente imagen
def siguienteImagen():
    global indiceActual
    indiceActual += 1
    mostrarImage()


# Función para mostrar la imagen anterior
def imagenAnterior():
    global indiceActual
    indiceActual -= 1
    mostrarImage()


# Crear la ventana principal de la aplicación
root = Tk()
root.title("Visor de Imagenes")
root.geometry("800x800")

# Crear un marco para la imagen
imagenFrame = LabelFrame(root, text="Imagenes", padx=100, pady=100)
imagenFrame.grid(row=0, column=0, padx=100, pady=100)

# Crear botones para navegar entre las imágenes y salir
botonSiguiente = Button(root, text="Siguiente Fotografía", command=siguienteImagen)
botonAnterior = Button(root, text="Fotografía Anterior", command=imagenAnterior)
botonSalir = Button(root, text="Salir", command=root.quit)

botonSiguiente.grid(row=1, column=0, padx=10, pady=10)
botonAnterior.grid(row=1, column=1, padx=10, pady=10)
botonSalir.grid(row=1, column=2, padx=10, pady=10)

# Etiqueta para mostrar información sobre la imagen actual
infoEtiqueta = Label(root, text="", bd=2, relief=SUNKEN, anchor=E)
infoEtiqueta.grid(row=2, column=0, columnspan=3, sticky=W+E)
infoEtiqueta.config(text=f"Imatge {indiceActual + 1} de {len(listaImagenes)}", anchor=E)

# Llamar a la función para mostrar la imagen actual
mostrarImage()

# Iniciar la aplicación
root.mainloop()
