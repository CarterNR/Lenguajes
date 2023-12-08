from tkinter import *
from productos import ProductosFormulario
from categorias import CategoriasFormulario
from costos import CostosFormulario
from cubiertas import CubiertasFormulario
from descuentos import DescuentosFormulario
from domicilios import DomiciliosFormulario
from entregas import EntregasFormulario
from facturas import FacturasFormulario
from inventario import InventarioFormulario
from ordenes import OrdenesFormulario
from rellenos import RellenosFormulario
from roles import RolesFormulario
from ventas import VentasFormulario
from usuarios import EliminarUsuarios
from usuarios import EliminarUsuarios
from editarUsuario import UsuarioDetailsForm

class LoveLyByCakes:

    def __init__(self, master):
        self.master = master
        master.title("Love-ly By Cakes")

        self.boton_usuarios = Button(master, text="Opciones Usuario", command=self.abrir_ventana_usuarios)
        self.boton_productos = Button(master, text="Formulario Productos", command=self.abrir_productos)
        self.boton_categorias = Button(master, text="Formulario Categorías", command=self.abrir_categorias)
        self.boton_costos = Button(master, text="Formulario Costos", command=self.abrir_costos)
        self.boton_cubiertas = Button(master, text="Formulario Cubiertas", command=self.abrir_cubiertas)
        self.boton_descuentos = Button(master, text="Formulario Descuentos", command=self.abrir_descuentos)
        self.boton_domicilios = Button(master, text="Formulario Domicilios", command=self.abrir_domicilios)
        self.boton_entregas = Button(master, text="Formulario Entregas", command=self.abrir_entregas)
        self.boton_facturas = Button(master, text="Formulario Facturas", command=self.abrir_facturas)
        self.boton_inventario = Button(master, text="Formulario Inventario", command=self.abrir_inventario)
        self.boton_ordenes = Button(master, text="Formulario Ordenes", command=self.abrir_ordenes)
        self.boton_rellenos = Button(master, text="Formulario Rellenos", command=self.abrir_rellenos)
        self.boton_roles = Button(master, text="Formulario Roles", command=self.abrir_roles)
        self.boton_ventas = Button(master, text="Formulario Ventas", command=self.abrir_ventas)

        self.boton_usuarios.pack(pady=20)
        self.boton_productos.pack(pady=20)
        self.boton_categorias.pack(pady=20)
        self.boton_costos.pack(pady=20)
        self.boton_cubiertas.pack(pady=20)
        self.boton_descuentos.pack(pady=20)
        self.boton_domicilios.pack(pady=20)
        self.boton_entregas.pack(pady=20)
        self.boton_facturas.pack(pady=20)
        self.boton_inventario.pack(pady=20)
        self.boton_ordenes.pack(pady=20)
        self.boton_rellenos.pack(pady=20)
        self.boton_roles.pack(pady=20)
        self.boton_ventas.pack(pady=20)

    def abrir_ventana_usuarios(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        EliminarUsuarios(ventana_usuarios)

    def abrir_productos(self):
        ventana_productos = Toplevel(self.master)
        ventana_productos.geometry("500x300")
        EliminarUsuarios(ventana_productos)

    def abrir_categorias(self):
        ventana_categorias = Toplevel(self.master)
        ventana_categorias.geometry("500x300")
        UsuarioDetailsForm(ventana_categorias)

    def abrir_costos(self):
        ventana_costos = Toplevel(self.master)
        ventana_costos.geometry("500x300")
        CostosFormulario(ventana_costos)

    def abrir_cubiertas(self):
        ventana_cubiertas = Toplevel(self.master)
        ventana_cubiertas.geometry("500x300")
        CubiertasFormulario(ventana_cubiertas)

    def abrir_descuentos(self):
        ventana_descuentos = Toplevel(self.master)
        ventana_descuentos.geometry("500x300")
        DescuentosFormulario(ventana_descuentos)

    def abrir_domicilios(self):
        ventana_domicilios = Toplevel(self.master)
        ventana_domicilios.geometry("500x300")
        DomiciliosFormulario(ventana_domicilios)

    def abrir_entregas(self):
        ventana_entregas = Toplevel(self.master)
        ventana_entregas.geometry("500x300")
        EntregasFormulario(ventana_entregas)

    def abrir_facturas(self):
        ventana_facturas = Toplevel(self.master)
        ventana_facturas.geometry("500x300")
        FacturasFormulario(ventana_facturas)

    def abrir_inventario(self):
        ventana_inventario = Toplevel(self.master)
        ventana_inventario.geometry("500x300")
        InventarioFormulario(ventana_inventario)

    def abrir_ordenes(self):
        ventana_ordenes = Toplevel(self.master)
        ventana_ordenes.geometry("500x300")
        OrdenesFormulario(ventana_ordenes)

    def abrir_rellenos(self):
        ventana_rellenos = Toplevel(self.master)
        ventana_rellenos.geometry("500x300")
        RellenosFormulario(ventana_rellenos)

    def abrir_roles(self):
        ventana_roles = Toplevel(self.master)
        ventana_roles.geometry("500x300")
        RolesFormulario(ventana_roles)

    def abrir_ventas(self):
        ventana_ventas = Toplevel(self.master)
        ventana_ventas.geometry("500x300")
        VentasFormulario(ventana_ventas)

if __name__ == "__main__":
    root = Tk()
    app = LoveLyByCakes(root)
    root.mainloop()
