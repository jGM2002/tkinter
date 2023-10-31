# Calculadora
import tkinter as tk
import math

# Inicializamos variables globales para el primer número y la operación
primerNombre = ""
operacion = ""


# Función que me limpiara el cuadro de texto.
def clear():
    global primerNombre, operacion
    quatreText.delete(0, tk.END)
    primerNombre = ""
    operacion = ""


# Función que calculara cualquier tipo de operación permitida
def igual():
    global primerNombre, operacion
    segonNombre = quatreText.get()
    if primerNombre and segonNombre and operacion:
        try:
            if operacion == "+":
                resultat = str(float(primerNombre) + float(segonNombre))
            elif operacion == "-":
                resultat = str(float(primerNombre) - float(segonNombre))
            elif operacion == "*":
                resultat = str(float(primerNombre) * float(segonNombre))
            elif operacion == "/":
                if float(segonNombre) != 0:
                    resultat = str(float(primerNombre) / float(segonNombre))
                else:
                    resultat = "ERROR"
            quatreText.delete(0, tk.END)
            quatreText.insert(0, resultat)
        except ValueError:
            quatreText.delete(0, tk.END)
            quatreText.insert(0, "ERROR")


# Función para manejar el clic en un número
def click_boto(number):
    entrada_actual = quatreText.get()
    quatreText.delete(0, tk.END)
    quatreText.insert(0, entrada_actual + str(number))


# Función para establecer la operación
def set_operacion(op):
    global operacion, primerNombre
    if primerNombre:
        igual()
    primerNombre = quatreText.get()
    operacion = op
    quatreText.delete(0, tk.END)


# Creamos la ventana de la calculadora
finestra = tk.Tk()
finestra.title("Calculadora")

# Creamos un cuadro de texto para mostrar los números y resultados
quatreText = tk.Entry(finestra, font=("Courier", 10), width=30, borderwidth=2)
quatreText.grid(row=10, column=0, columnspan=4)

# Creamos botones para los números del 0 al 9
for i in range(10):
    boto = tk.Button(finestra, text=str(i), font=("Arial", 12), width=5, height=2, command=lambda i=i: click_boto(i))
    fila = (i - 1) // 3 + 1
    columna = (i - 1) % 3
    boto.grid(row=fila, column=columna)

# Botón "Clear" para borrar el contenido del cuadro de texto
botoClear = tk.Button(finestra, text="Clear", font=("Arial", 12), width=5, height=2, command=clear)
botoClear.grid(row=4, column=0)

# Botones para las operaciones de suma. resta, multiplicación y división
botoSuma = tk.Button(finestra, text="+", font=("Arial", 12), width=5, height=2, command=lambda: set_operacion("+"))
botoSuma.grid(row=4, column=1)

botoResta = tk.Button(finestra, text="-", font=("Arial", 12), width=5, height=2, command=lambda: set_operacion("-"))
botoResta.grid(row=4, column=2)

botoMultiplicacio = tk.Button(finestra, text="*", font=("Arial", 12), width=5, height=2, command=lambda: set_operacion("*"))
botoMultiplicacio.grid(row=5, column=1)

botoDivision = tk.Button(finestra, text="/", font=("Arial", 12), width=5, height=2, command=lambda: set_operacion("/"))
botoDivision.grid(row=5, column=2)

botoIgual = tk.Button(finestra, text="=", font=("Arial", 12), width=5, height=2, command=igual)
botoIgual.grid(row=5, column=0)

# Iniciamos la ventana de la calculadora
finestra.mainloop()
