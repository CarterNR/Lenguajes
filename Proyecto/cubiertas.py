from tkinter import *

class CubiertasFormulario:
    def __init__(self, master):
        self.master = master
        master.title("Formulario de Cubiertas")

        self.label_cubierta = Label(master, text="Tipo de Cubierta:")
        self.entry_cubierta = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_cubierta)

        self.label_cubierta.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.entry_cubierta.grid(row=0, column=1, padx=10, pady=10)

        self.boton_guardar.grid(row=1, column=0, columnspan=2, pady=10)

    def guardar_cubierta(self):
        cubierta = self.entry_cubierta.get()

        # Aquí puedes agregar la lógica para guardar la cubierta en tu aplicación
        print(f"Cubierta guardada: Tipo - {cubierta}")

if __name__ == "__main__":
    root = Tk()
    app = CubiertasFormulario(root)
    root.mainloop()
