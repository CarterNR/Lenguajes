from tkinter import *

class CostosFormulario:
    def __init__(self, master):
        self.master = master
        master.title("Formulario de Costos")

        self.label_costo = Label(master, text="Costo:")
        self.entry_costo = Entry(master)

        self.label_id_provincia = Label(master, text="ID Provincia:")
        self.entry_id_provincia = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_costo)

        self.label_costo.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.entry_costo.grid(row=0, column=1, padx=10, pady=10)

        self.label_id_provincia.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_id_provincia.grid(row=1, column=1, padx=10, pady=10)

        self.boton_guardar.grid(row=2, column=0, columnspan=2, pady=10)

    def guardar_costo(self):
        costo = self.entry_costo.get()
        id_provincia = self.entry_id_provincia.get()

        # Aquí puedes agregar la lógica para guardar el costo en tu aplicación
        print(f"Costo guardado: Costo - {costo}, ID Provincia - {id_provincia}")

if __name__ == "__main__":
    root = Tk()
    app = CostosFormulario(root)
    root.mainloop()
