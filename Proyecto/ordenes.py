from tkinter import *

class OrdenesFormulario:
    def __init__(self, master):
        self.master = master
        master.title("Formulario de Órdenes")

        self.label_cantidad_personas = Label(master, text="Cantidad de Personas:")
        self.entry_cantidad_personas = Entry(master)

        self.label_id_producto = Label(master, text="ID Producto:")
        self.entry_id_producto = Entry(master)

        self.label_id_relleno = Label(master, text="ID Relleno:")
        self.entry_id_relleno = Entry(master)

        self.label_id_cubierta = Label(master, text="ID Cubierta:")
        self.entry_id_cubierta = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_orden)

        self.label_cantidad_personas.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.entry_cantidad_personas.grid(row=0, column=1, padx=10, pady=10)

        self.label_id_producto.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_id_producto.grid(row=1, column=1, padx=10, pady=10)

        self.label_id_relleno.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.entry_id_relleno.grid(row=2, column=1, padx=10, pady=10)

        self.label_id_cubierta.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.entry_id_cubierta.grid(row=3, column=1, padx=10, pady=10)

        self.boton_guardar.grid(row=4, column=0, columnspan=2, pady=10)

    def guardar_orden(self):
        cantidad_personas = self.entry_cantidad_personas.get()
        id_producto = self.entry_id_producto.get()
        id_relleno = self.entry_id_relleno.get()
        id_cubierta = self.entry_id_cubierta.get()

        # Aquí puedes agregar la lógica para guardar la orden en tu aplicación
        print(f"Orden guardada: Cantidad de Personas - {cantidad_personas}, "
              f"ID Producto - {id_producto}, ID Relleno - {id_relleno}, ID Cubierta - {id_cubierta}")

if __name__ == "__main__":
    root = Tk()
    app = OrdenesFormulario(root)
    root.mainloop()
