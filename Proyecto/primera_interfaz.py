from tkinter import*

# Función que se ejecutará cuando se presiona el botón
def on_button_click():
    # Crear una nueva ventana (top-level window)
    nueva_ventana = Toplevel(raiz)
    nueva_ventana.title("Nueva Ventana")
    etiqueta = Label(nueva_ventana, text="¡Joel es un estupido!")
    etiqueta.pack(pady=20)  # Ajustar el espacio alrededor del texto


    # Puedes agregar widgets (botones, etiquetas, etc.) a la nueva ventana aquí

# Crear la ventana principal
raiz = Tk()
raiz.title("Prueba")
raiz.resizable(0, 0)

# Crear un botón y asociarlo con la función on_button_click
boton = Button(raiz, text="Presionar para abrir nueva ventana", command=on_button_click)
boton.pack(pady=20)  # Ajustar el espacio alrededor del botón

# Iniciar el bucle principal
raiz.mainloop()
