from tkinter import *

class DomiciliosFormulario:
    def __init__(self, master):
        self.master = master
        master.title("Formulario de Domicilios")

        self.label_direccion = Label(master, text="Dirección:")
        self.entry_direccion = Entry(master)

        self.label_id_provincia = Label(master, text="ID Provincia:")
        self.entry_id_provincia = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_domicilio)

        self.label_direccion.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.entry_direccion.grid(row=0, column=1, padx=10, pady=10)

        self.label_id_provincia.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_id_provincia.grid(row=1, column=1, padx=10, pady=10)

        self.boton_guardar.grid(row=2, column=0, columnspan=2, pady=10)

    def guardar_domicilio(self):
        direccion = self.entry_direccion.get()
        id_provincia = self.entry_id_provincia.get()

        # Aquí puedes agregar la lógica para guardar el domicilio en tu aplicación
        print(f"Domicilio guardado: Dirección - {direccion}, ID Provincia - {id_provincia}")

if __name__ == "__main__":
    root = Tk()
    app = DomiciliosFormulario(root)
    root.mainloop()
