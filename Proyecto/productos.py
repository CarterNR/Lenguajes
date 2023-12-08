import tkinter as tk
import cx_Oracle
from tkinter import ttk, messagebox


class ProductosFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Producto")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiquetas y campos de entrada
        etiquetas = ["Descripcion", "Precio"]
        self.campos = {}
        for i, etiqueta in enumerate(etiquetas):
            tk.Label(root, text=etiqueta).grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            self.campos[etiqueta] = tk.Entry(root)
            self.campos[etiqueta].grid(row=i, column=1, padx=10, pady=5)

        # Etiqueta y combobox para el categoria
        tk.Label(root, text="Categoria").grid(row=len(etiquetas), column=0, sticky=tk.W, padx=10, pady=5)
        self.combo_categoria = ttk.Combobox(root, state="readonly")
        self.combo_categoria.grid(row=len(etiquetas), column=1, padx=10, pady=5)

        # Cargar categorias automáticamente al iniciar
        self.cargar_categorias()

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Enviar", command=self.enviar_formulario)
        btn_enviar.grid(row=len(etiquetas) + 1, column=0, columnspan=2, pady=10)

    def cargar_categorias(self):
        # Limpiar valores del Combobox
        self.combo_categoria.set("")

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_CATEGORIAS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Configurar valores del Combobox
            categorias = [row[1] for row in result_set]
            self.combo_categoria["values"] = categorias

    def enviar_formulario(self):
        # Obtener los valores del formulario
        valores = [self.campos[etiqueta].get() for etiqueta in self.campos]
        categoria_seleccionado = self.combo_categoria.get()

        if not all(valores) or not categoria_seleccionado:
            print("Por favor, complete todos los campos y seleccione un categoria.")
            return

        # Ejecutar el procedimiento almacenado con los valores del formulario
        self.cursor.callproc('INSERTAR_PRODUCTO', valores + [categoria_seleccionado])
        self.connection.commit()

        # Limpiar los campos del formulario
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        self.combo_categoria.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductosFormulario(root)
    root.mainloop()



#-VistaProductos----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class VistaProducto:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Productos")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Crear un Treeview para mostrar los resultados
        self.tree = ttk.Treeview(root, columns=('ID_PRODUCTO', 'DESCRIPCION', 'PRECIO', 'CATEGORIA'), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar encabezados de columnas
        for col in ('ID_PRODUCTO', 'DESCRIPCION', 'PRECIO', 'CATEGORIA'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Botón para cargar y mostrar productos
        btn_cargar = ttk.Button(root, text="Cargar Productos", command=self.cargar_productos)
        btn_cargar.pack(pady=10)

    def cargar_productos(self):
        # Limpiar árbol antes de cargar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_PRODUCTOS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Insertar filas en el Treeview
            for row in result_set:
                self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaProducto(root)
    root.mainloop()



#-EliminarProductos-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EliminarProductos:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario para Eliminar Producto")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta y campo de entrada para el ID del producto a eliminar
        tk.Label(root, text="ID del Producto a Eliminar").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_id_producto = tk.Entry(root)
        self.entry_id_producto.grid(row=0, column=1, padx=10, pady=5)

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Eliminar Producto", command=self.eliminar_producto)
        btn_enviar.grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_producto(self):
        # Obtener el ID del producto a eliminar
        id_producto = int(self.entry_id_producto.get())

        # Ejecutar el procedimiento almacenado para eliminar el producto
        self.cursor.callproc('ELIMINAR_PRODUCTO', (id_producto,))
        self.connection.commit()

        # Limpiar el campo del formulario
        self.entry_id_producto.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarProductos(root)
    root.mainloop()


#-EditarProductos-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EditarProducto:
    def __init__(self, master, user_info, connection, main_form):
        self.master = master
        self.master.title("Detalles del Producto")

        # Referencia al formulario principal
        self.main_form = main_form

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Conexión a la base de datos
        self.connection = connection

        # Crear campos de texto para mostrar/permitir la edición de la información del producto
        self.campos = {}
        labels = ["ID_PRODUCTO", "DESCRIPCION", "PRECIO", "CATEGORIA"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=f"{label}:").grid(row=i, column=0, pady=5)
            self.campos[label] = tk.Entry(self.frame)
            self.campos[label].insert(0, user_info[i])  # Insertar la información en el campo
            self.campos[label].grid(row=i, column=1, padx=10, pady=5)

        # Botón para actualizar los datos del producto
        btn_actualizar = ttk.Button(self.frame, text="Actualizar Producto", command=self.actualizar_producto)
        btn_actualizar.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Configurar el evento de cierre del formulario
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_formularios)

    def cerrar_formularios(self):
        # Cerrar ambos formularios
        self.master.destroy()
        self.main_form.root.destroy()

    def actualizar_producto(self):
        # Obtener los nuevos datos del producto
        nuevos_datos = {}
        for label, entry in self.campos.items():
            nuevos_datos[label] = entry.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            cursor = self.connection.cursor()

            # Ejecutar el procedimiento almacenado ACTUALIZAR_PRODUCTO
            cursor.callproc(
                'ACTUALIZAR_PRODUCTO',
                (
                    nuevos_datos["ID_PRODUCTO"],
                    nuevos_datos["DESCRIPCION"],
                    nuevos_datos["PRECIO"],
                    nuevos_datos["CATEGORIA"]
                )
            )

            # Confirmar los cambios en la base de datos
            self.connection.commit()

            # Cerrar el cursor
            cursor.close()

            # messagebox.showinfo("Producto Actualizado", "Los datos del producto han sido actualizados exitosamente.")
            self.cerrar_formularios()  # Cerrar ambos formularios
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar producto: {str(e)}")

class LlamarProductos:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Producto por ID")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta e input para el ID del producto
        lbl_id_producto = ttk.Label(root, text="ID del Producto:")
        lbl_id_producto.pack(pady=5)
        self.entry_id_producto = ttk.Entry(root)
        self.entry_id_producto.pack(pady=5)

        # Botón para enviar el ID del producto
        btn_enviar = ttk.Button(root, text="Consultar Producto", command=self.consultar_producto)
        btn_enviar.pack(pady=10)

    def consultar_producto(self):
        # Obtener el ID del producto desde el campo de entrada
        id_producto = self.entry_id_producto.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            v_cursor = self.cursor.var(cx_Oracle.CURSOR)

            # Ejecutar el procedimiento almacenado
            self.cursor.callproc('VER_PRODUCTOSAC', (v_cursor, id_producto))

            # Obtener los resultados del cursor usando fetchall()
            result_set = v_cursor.getvalue().fetchall()

            if result_set:  # Asegurarse de que haya resultados
                # Mostrar los detalles en un nuevo formulario
                user_info = result_set[0]
                user_details_form = tk.Toplevel(self.root)
                EditarProducto(user_details_form, user_info, self.connection, self)
            else:
                messagebox.showinfo("Producto no encontrado", "No se encontró ningún producto con el ID especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Llamar(root)
    root.mainloop()
