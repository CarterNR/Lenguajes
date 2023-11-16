from tkinter import *

class ProductosFormulario:

    def __init__(self, master):
        self.master = master
        master.title("Formulario de Productos")

        self.label_descripcion = Label(master, text="Descripción del Producto:")
        self.entry_descripcion = Entry(master)

        self.label_precio = Label(master, text="Precio:")
        self.entry_precio = Entry(master)

        self.label_id_categoria = Label(master, text="ID Categoría:")
        self.entry_id_categoria = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_producto)

        self.label_descripcion.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.entry_descripcion.grid(row=0, column=1, padx=10, pady=10)

        self.label_precio.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_precio.grid(row=1, column=1, padx=10, pady=10)

        self.label_id_categoria.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.entry_id_categoria.grid(row=2, column=1, padx=10, pady=10)

        self.boton_guardar.grid(row=3, column=0, columnspan=2, pady=10)

    def guardar_producto(self):
        descripcion = self.entry_descripcion.get()
        precio = self.entry_precio.get()
        id_categoria = self.entry_id_categoria.get()

        # Aquí puedes agregar la lógica para guardar el producto en tu aplicación
        print(f"Producto guardado: Descripción - {descripcion}, Precio - {precio}, ID Categoría - {id_categoria}")

if __name__ == "__main__":
    root = Tk()
    app = ProductosFormulario(root)
    root.mainloop()


