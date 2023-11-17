from tkinter import *

class VentasFormulario:

    def __init__(self, master):
        self.master = master
        master.title("Formulario de Ventas")

        
        self.label_emision = Label(master, text="Emision:")
        self.entry_emision = Entry(master)

        self.label_cantidad = Label(master, text="Cantidad:")
        self.entry_cantidad = Entry(master)

        self.label_id_orden = Label(master, text="ID Orden:")
        self.entry_id_orden = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_venta)

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

    def guardar_venta(self):
        emision = self.entry_emision.get()
        cantidad = self.entry_cantidad.get()
        id_orden = self.entry_id_orden.get()

        print(f"Emision: {emision}, Cantidad: {cantidad}, ID Orden - {id_orden}")

if __name__ == "__main__":
    root = Tk()
    app = VentasFormulario(root)
    root.mainloop()