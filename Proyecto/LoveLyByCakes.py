from tkinter import *
from usuarios import UsuariosFormulario
from productos import ProductosFormulario

class LoveLyByCakes:

    def __init__(self, master):
        self.master = master
        master.title("Love-ly By Cakes")

        self.boton_usuarios = Button(master, text="Formulario Usuarios", command=self.abrir_usuarios)
        self.boton_productos = Button(master, text="Formulario Productos", command=self.abrir_productos)

        self.boton_usuarios.pack(pady=20)
        self.boton_productos.pack(pady=20)

    def abrir_usuarios(self):
        ventana_usuarios = Toplevel(self.master)
        # Establecer el tamaño inicial de la ventana de usuarios
        ventana_usuarios.geometry("500x300")
        UsuariosFormulario(ventana_usuarios)

    def abrir_productos(self):
        ventana_productos = Toplevel(self.master)
        ventana_productos.geometry("500x300")
        ProductosFormulario(ventana_productos)

if __name__ == "__main__":
    root = Tk()
    app = LoveLyByCakes(root)
    root.mainloop()

