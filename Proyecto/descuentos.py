from tkinter import *

class DescuentosFormulario:
    def __init__(self, master):
        self.master = master
        master.title("Formulario de Descuentos")

        self.label_porcentaje_desc = Label(master, text="Porcentaje de Descuento:")
        self.entry_porcentaje_desc = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_descuento)

        self.label_porcentaje_desc.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.entry_porcentaje_desc.grid(row=0, column=1, padx=10, pady=10)

        self.boton_guardar.grid(row=1, column=0, columnspan=2, pady=10)

    def guardar_descuento(self):
        porcentaje_desc = self.entry_porcentaje_desc.get()

        # Aquí puedes agregar la lógica para guardar el descuento en tu aplicación
        print(f"Descuento guardado: Porcentaje - {porcentaje_desc}%")

if __name__ == "__main__":
    root = Tk()
    app = DescuentosFormulario(root)
    root.mainloop()
