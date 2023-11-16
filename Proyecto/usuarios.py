from tkinter import *

class UsuariosFormulario:

    def __init__(self, master):
        self.master = master
        master.title("Formulario de Usuarios")

        self.label_nombre = Label(master, text="Nombre:")
        self.entry_nombre = Entry(master)

        self.label_apellido1 = Label(master, text="Apellido 1:")
        self.entry_apellido1 = Entry(master)

        self.label_apellido2 = Label(master, text="Apellido 2:")
        self.entry_apellido2 = Entry(master)

        self.label_telefono = Label(master, text="Teléfono:")
        self.entry_telefono = Entry(master)

        self.label_correo = Label(master, text="Correo:")
        self.entry_correo = Entry(master)

        self.label_clave = Label(master, text="Clave:")
        self.entry_clave = Entry(master, show="*")  # Para ocultar la contraseña

        self.label_id_domicilio = Label(master, text="ID Domicilio:")
        self.entry_id_domicilio = Entry(master)

        self.label_id_rol = Label(master, text="ID Rol:")
        self.entry_id_rol = Entry(master)

        self.boton_guardar = Button(master, text="Guardar", command=self.guardar_usuario)

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

    def guardar_usuario(self):
        nombre = self.entry_nombre.get()
        apellido1 = self.entry_apellido1.get()
        apellido2 = self.entry_apellido2.get()
        telefono = self.entry_telefono.get()
        correo = self.entry_correo.get()
        clave = self.entry_clave.get()
        id_domicilio = self.entry_id_domicilio.get()
        id_rol = self.entry_id_rol.get()

        # Aquí puedes agregar la lógica para guardar el usuario en tu aplicación
        print(f"Usuario guardado: Nombre - {nombre}, Apellido 1 - {apellido1}, Apellido 2 - {apellido2}, "
              f"Teléfono - {telefono}, Correo - {correo}, Clave - {clave}, "
              f"ID Domicilio - {id_domicilio}, ID Rol - {id_rol}")

if __name__ == "__main__":
    root = Tk()
    app = UsuariosFormulario(root)
    root.mainloop()
