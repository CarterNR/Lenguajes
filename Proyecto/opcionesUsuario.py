import tkinter as tk
from tkinter import *
from tkinter import messagebox
from usuarios import *
from roles import *
from categorias import *
from productos import *
from inventario import *
from rellenos import *
from cubiertas import *
from ordenes import *
from facturas import *


class App:
    def __init__(self, master):
        self.master = master
        master.title("Menú de Opciones")

        # Barra de menú
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Menú Archivo
        self.menu_archivo = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_archivo.add_command(label="Abrir", command=self.abrir_pagina)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=master.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.menu_archivo)

        # Menú Ver
        self.menu_ver = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_ver.add_command(label="Agregar Usuario", command=self.agregar_usuario)
        self.menu_ver.add_command(label="Ver Usuarios", command=self.ver_usuarios)
        self.menu_ver.add_command(label="Eliminar Usuario", command=self.eliminar_usuario)
        self.menu_ver.add_command(label="Editar Usuario", command=self.editar_usuario)
        self.menu_bar.add_cascade(label="Usuarios", menu=self.menu_ver)

        #Roles
        self.menu_ver = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_ver.add_command(label="Agregar Rol", command=self.agregar_rol)
        self.menu_ver.add_command(label="Ver Roles", command=self.ver_roles)
        self.menu_ver.add_command(label="Eliminar Rol", command=self.eliminar_rol)
        self.menu_ver.add_command(label="Editar Rol", command=self.editar_rol)
        self.menu_bar.add_cascade(label="Roles", menu=self.menu_ver)

        #Categorias
        self.menu_ver = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_ver.add_command(label="Agregar Categoría", command=self.agregar_categoria)
        self.menu_ver.add_command(label="Ver Categorías", command=self.ver_categorias)
        self.menu_ver.add_command(label="Eliminar Categoría", command=self.eliminar_categoria)
        self.menu_ver.add_command(label="Editar Categoría", command=self.editar_categoria)
        self.menu_bar.add_cascade(label="Categorías", menu=self.menu_ver)

        #Producto
        self.menu_productos = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_productos.add_command(label="Agregar Producto", command=self.agregar_producto)
        self.menu_productos.add_command(label="Ver Productos", command=self.ver_productos)
        self.menu_productos.add_command(label="Eliminar Producto", command=self.eliminar_producto)
        self.menu_productos.add_command(label="Editar Producto", command=self.editar_producto)
        self.menu_bar.add_cascade(label="Productos", menu=self.menu_productos)


        # Inventarios
        self.menu_inventarios = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_inventarios.add_command(label="Agregar Inventario", command=self.agregar_inventario)
        self.menu_inventarios.add_command(label="Ver Inventarios", command=self.ver_inventarios)
        self.menu_inventarios.add_command(label="Eliminar Inventario", command=self.eliminar_inventario)
        self.menu_inventarios.add_command(label="Editar Inventario", command=self.editar_inventario)
        self.menu_bar.add_cascade(label="Inventario", menu=self.menu_inventarios)


        # Rellenos
        self.menu_rellenos = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_rellenos.add_command(label="Agregar Relleno", command=self.agregar_relleno)
        self.menu_rellenos.add_command(label="Ver Rellenos", command=self.ver_rellenos)
        self.menu_rellenos.add_command(label="Eliminar Relleno", command=self.eliminar_relleno)
        self.menu_rellenos.add_command(label="Editar Relleno", command=self.editar_relleno)
        self.menu_bar.add_cascade(label="Rellenos", menu=self.menu_rellenos)


        # Cubiertas
        self.menu_cubiertas = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_cubiertas.add_command(label="Agregar Cubierta", command=self.agregar_cubierta)
        self.menu_cubiertas.add_command(label="Ver Cubiertas", command=self.ver_cubiertas)
        self.menu_cubiertas.add_command(label="Eliminar Cubierta", command=self.eliminar_cubierta)
        self.menu_cubiertas.add_command(label="Editar Cubierta", command=self.editar_cubierta)
        self.menu_bar.add_cascade(label="Cubiertas", menu=self.menu_cubiertas)


        # Ordenes
        self.menu_ordenes = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_ordenes.add_command(label="Agregar Orden", command=self.agregar_orden)
        self.menu_ordenes.add_command(label="Ver Ordenes", command=self.ver_ordenes)
        self.menu_ordenes.add_command(label="Eliminar Orden", command=self.eliminar_orden)
        self.menu_ordenes.add_command(label="Editar Orden", command=self.editar_orden)
        self.menu_bar.add_cascade(label="Ordenes", menu=self.menu_ordenes)


        # Facturas
        self.menu_facturas = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_facturas.add_command(label="Agregar Factura", command=self.agregar_factura)
        self.menu_facturas.add_command(label="Ver Facturas", command=self.ver_facturas)
        self.menu_facturas.add_command(label="Eliminar Factura", command=self.eliminar_factura)
        self.menu_facturas.add_command(label="Editar Factura", command=self.editar_factura)
        self.menu_bar.add_cascade(label="Facturas", menu=self.menu_facturas)








    def agregar_usuario(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        UsuariosFormulario(ventana_usuarios)

    def ver_usuarios(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        VistaUsuario(ventana_usuarios)

    def eliminar_usuario(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        EliminarUsuarios(ventana_usuarios)
    
    def editar_usuario(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        LlamarUsuarios(ventana_usuarios)

    
    #Roles
    def agregar_rol(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        RolesFormulario(ventana_usuarios)

    def ver_roles(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        VistaRol(ventana_usuarios)

    def eliminar_rol(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        EliminarRoles(ventana_usuarios)
    
    def editar_rol(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        LlamarRoles(ventana_usuarios)

    
    #Categorias
    def agregar_categoria(self):
        ventana_categorias = Toplevel(self.master)
        ventana_categorias.geometry("500x300")
        CategoriasFormulario(ventana_categorias)

    def ver_categorias(self):
        ventana_categorias = Toplevel(self.master)
        ventana_categorias.geometry("500x300")
        VistaCategoria(ventana_categorias)

    def eliminar_categoria(self):
        ventana_categorias = Toplevel(self.master)
        ventana_categorias.geometry("500x300")
        EliminarCategorias(ventana_categorias)

    def editar_categoria(self):
        ventana_categorias = Toplevel(self.master)
        ventana_categorias.geometry("500x300")
        LlamarCategorias(ventana_categorias)


    #Productos
    def agregar_producto(self):
        ventana_productos = Toplevel(self.master)
        ventana_productos.geometry("500x300")
        ProductosFormulario(ventana_productos)

    def ver_productos(self):
        ventana_productos = Toplevel(self.master)
        ventana_productos.geometry("500x300")
        VistaProducto(ventana_productos)

    def eliminar_producto(self):
        ventana_productos = Toplevel(self.master)
        ventana_productos.geometry("500x300")
        EliminarProductos(ventana_productos)

    def editar_producto(self):
        ventana_productos = Toplevel(self.master)
        ventana_productos.geometry("500x300")
        LlamarProductos(ventana_productos)


    # Inventarios
    def agregar_inventario(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        InventarioFormulario(ventana_usuarios)

    def ver_inventarios(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        VistaInventario(ventana_usuarios)

    def eliminar_inventario(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        EliminarInventarios(ventana_usuarios)

    def editar_inventario(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        LlamarInventario(ventana_usuarios)


    # Rellenos
    def agregar_relleno(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        RellenosFormulario(ventana_usuarios)

    def ver_rellenos(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        VistaRelleno(ventana_usuarios)

    def eliminar_relleno(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        EliminarRellenos(ventana_usuarios)

    def editar_relleno(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        LlamarRellenos(ventana_usuarios)


    # Cubiertas
    def agregar_cubierta(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        CubiertasFormulario(ventana_usuarios)

    def ver_cubiertas(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        VistaCubierta(ventana_usuarios)

    def eliminar_cubierta(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        EliminarCubiertas(ventana_usuarios)

    def editar_cubierta(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        LlamarCubiertas(ventana_usuarios)

    
    # Ordenes
    def agregar_orden(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        OrdenesFormulario(ventana_usuarios)

    def ver_ordenes(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        VistaOrden(ventana_usuarios)

    def eliminar_orden(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        EliminarOrdenes(ventana_usuarios)

    def editar_orden(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        LlamarOrdenes(ventana_usuarios)


    # Facturas
    def agregar_factura(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        FacturasFormulario(ventana_usuarios)

    def ver_facturas(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        VistaFactura(ventana_usuarios)

    def eliminar_factura(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        EliminarFacturas(ventana_usuarios)

    def editar_factura(self):
        ventana_usuarios = Toplevel(self.master)
        ventana_usuarios.geometry("500x300")
        LlamarFacturas(ventana_usuarios)




    def abrir_pagina(self):
        messagebox.showinfo("Abrir", "Abrir página aún no implementado")

if __name__ == "__main__":

    root = tk.Tk()
    app = App(root)
    root.mainloop()
