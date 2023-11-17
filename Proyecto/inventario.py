from tkinter import *

class InventarioFormulario:

    def __init__(self, master):
        self.master = master
        master.title("Formulario de Inventario")

        
        self.label_cantidad = Label(master, text="Cantidad:")
        self.entry_cantidad = Entry(master)

        self.label_id_producto = Label(master, text="ID Producto:")
        self.entry_id_producto = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_inventario)

        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_apellido1.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_apellido1.grid(row=1, column=1, padx=10, pady=10)

        self.label_apellido2.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.entry_apellido2.grid(row=2, column=1, padx=10, pady=10)

        self.label_telefono.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=10)

        self.label_correo.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        self.entry_correo.grid(row=4, column=1, padx=10, pady=10)

        self.label_clave.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        self.entry_clave.grid(row=5, column=1, padx=10, pady=10)

        self.label_id_domicilio.grid(row=6, column=0, padx=10, pady=10, sticky=W)
        self.entry_id_domicilio.grid(row=6, column=1, padx=10, pady=10)

        self.label_id_rol.grid(row=7, column=0, padx=10, pady=10, sticky=W)
        self.entry_id_rol.grid(row=7, column=1, padx=10, pady=10)

        self.boton_guardar.grid(row=8, column=0, columnspan=2, pady=10)

    def guardar_inventario(self):
        cantidad = self.entry_cantidad.get()
        id_producto = self.entry_id_producto.get()

        print(f"Cantidad en inventario: {cantidad}, ID Producto - {id_producto}")

if __name__ == "__main__":
    root = Tk()
    app = InventarioFormulario(root)
    root.mainloop()