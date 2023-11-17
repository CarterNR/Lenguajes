from tkinter import *

class FacturasFormulario:

    def __init__(self, master):
        self.master = master
        master.title("Formulario de Facturas")

        
        self.label_emision = Label(master, text="Emision:")
        self.entry_emision = Entry(master)

        self.label_subtotal = Label(master, text="Subtotal:")
        self.entry_subtotal = Entry(master)

        self.label_impuestos = Label(master, text="Impuestos:")
        self.entry_impuestos = Entry(master)

        self.label_total = Label(master, text="Total:")
        self.entry_total = Entry(master)

        self.label_id_venta = Label(master, text="ID Venta:")
        self.entry_id_venta = Entry(master)

        self.label_id_descuento = Label(master, text="ID Descuento:")
        self.entry_id_descuento = Entry(master)

        self.label_id_usuario_emisor = Label(master, text="ID Usuario Emisor:")
        self.entry_id_usuario_emisor = Entry(master)

        self.label_id_usuario_receptor = Label(master, text="ID Usuario Receptor:")
        self.entry_id_usuario_receptor = Entry(master)

        self.label_id_envio = Label(master, text="ID Envio:")
        self.entry_id_envio = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_factura)

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

    def guardar_factura(self):
        emision = self.entry_emision.get()
        subtotal = self.entry_subtotal.get()
        impuestos = self.entry_impuestos.get()
        total = self.entry_total.get()
        id_venta = self.entry_id_venta.get()
        id_descuento = self.entry_id_descuento.get()
        id_usuario_emisor = self.entry_id_usuario_emisor.get()
        id_usuario_receptor = self.entry_id_usuario_receptor.get()
        id_envio = self.entry_id_envio.get()

        print(f"Emision: {emision}, Subtotal= - {subtotal}, Impuestos= - {impuestos}, "
              f"Total= - {total}, ID venta: - {id_venta}, ID descuento: - {id_descuento}, "
              f"ID Usuario Emisor: - {id_usuario_emisor}, ID Usuario Receptor: - {id_usuario_receptor}, "
              f"ID Envio: - {id_envio},")

if __name__ == "__main__":
    root = Tk()
    app = FacturasFormulario(root)
    root.mainloop()