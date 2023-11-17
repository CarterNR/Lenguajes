from tkinter import *

class CategoriasFormulario:
    def __init__(self, master):
        self.master = master
        master.title("Formulario de Categorías")

        self.label_categoria = Label(master, text="Categoría:")
        self.entry_categoria = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_categoria)

        self.label_categoria.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.entry_categoria.grid(row=0, column=1, padx=10, pady=10)

        self.boton_guardar.grid(row=1, column=0, columnspan=2, pady=10)

    def guardar_categoria(self):
        categoria = self.entry_categoria.get()

        # Aquí puedes agregar la lógica para guardar la categoría en tu aplicación
        print(f"Categoría guardada: Categoría - {categoria}")

if __name__ == "__main__":
    root = Tk()
    app = CategoriasFormulario(root)
    root.mainloop()
