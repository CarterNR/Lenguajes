import tkinter as tk
import cx_Oracle
from tkinter import ttk, messagebox


class CategoriasFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Categorias")

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
        etiquetas = ["Categoria"]
        self.campos = {}
        for i, etiqueta in enumerate(etiquetas):
            tk.Label(root, text=etiqueta).grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            self.campos[etiqueta] = tk.Entry(root)
            self.campos[etiqueta].grid(row=i, column=1, padx=10, pady=5)

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Enviar", command=self.enviar_formulario)
        btn_enviar.grid(row=len(etiquetas) + 1, column=0, columnspan=2, pady=10)

    def enviar_formulario(self):
        # Obtener los valores del formulario
        valores = [self.campos[etiqueta].get() for etiqueta in self.campos]

        # Ejecutar el procedimiento almacenado con los valores del formulario
        self.cursor.callproc('INSERTAR_CATEGORIA', valores)
        self.connection.commit()

        # Limpiar los campos del formulario
        for campo in self.campos.values():
            campo.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CategoriasFormulario(root)
    root.mainloop()


#-VerCategorias-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class VistaCategoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Categorias")

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
        self.tree = ttk.Treeview(root, columns=('ID_CATEGORIA', 'CATEGORIA'), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar encabezados de columnas
        for col in ('ID_CATEGORIA', 'CATEGORIA'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Botón para cargar y mostrar usuarios
        btn_cargar = ttk.Button(root, text="Cargar Categorias", command=self.cargar_categorias)
        btn_cargar.pack(pady=10)

    def cargar_categorias(self):
        # Limpiar árbol antes de cargar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_CATEGORIAS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Insertar filas en el Treeview
            for row in result_set:
                self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaCategoria(root)
    root.mainloop()


#-EliminarCategorias-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EliminarCategorias:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario para Eliminar Categoria")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta y campo de entrada para el ID del usuario a eliminar
        tk.Label(root, text="ID del Categoria a Eliminar").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_id_categoria = tk.Entry(root)
        self.entry_id_categoria.grid(row=0, column=1, padx=10, pady=5)

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Eliminar Categoria", command=self.eliminar_categoria)
        btn_enviar.grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_categoria(self):
        # Obtener el ID del usuario a eliminar
        id_categoria = int(self.entry_id_categoria.get())

        # Ejecutar el procedimiento almacenado para eliminar el usuario
        self.cursor.callproc('ELIMINAR_CATEGORIA', (id_categoria,))
        self.connection.commit()

        # Limpiar el campo del formulario
        self.entry_id_categoria.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarCategorias(root)
    root.mainloop()


#-EditarUsuarios-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EditarCategoria:
    def __init__(self, master, categoria_info, connection, main_form):
        self.master = master
        self.master.title("Editar Categoria")

        # Referencia al formulario principal
        self.main_form = main_form

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Conexión a la base de datos
        self.connection = connection

        # Crear campos de texto para mostrar/permitir la edición de la información del usuario
        self.campos = {}
        labels = ["ID_CATEGORIA", "CATEGORIA"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=f"{label}:").grid(row=i, column=0, pady=5)
            self.campos[label] = tk.Entry(self.frame)
            self.campos[label].insert(0, categoria_info[i])  # Insertar la información en el campo
            self.campos[label].grid(row=i, column=1, padx=10, pady=5)

        # Botón para actualizar los datos del usuario
        btn_actualizar = ttk.Button(self.frame, text="Actualizar Categoria", command=self.actualizar_categoria)
        btn_actualizar.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Configurar el evento de cierre del formulario
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_formularios)

    def cerrar_formularios(self):
        # Cerrar ambos formularios
        self.master.destroy()
        self.main_form.root.destroy()

    def actualizar_categoria(self):
        # Obtener los nuevos datos del usuario
        nuevos_datos = {}
        for label, entry in self.campos.items():
            nuevos_datos[label] = entry.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            cursor = self.connection.cursor()

            # Ejecutar el procedimiento almacenado ACTUALIZAR_USUARIO
            cursor.callproc(
                'ACTUALIZAR_CATEGORIA',
                (
                    nuevos_datos["ID_CATEGORIA"],
                    nuevos_datos["CATEGORIA"]
                )
            )

            # Confirmar los cambios en la base de datos
            self.connection.commit()

            # Cerrar el cursor
            cursor.close()

            # messagebox.showinfo("Usuario Actualizado", "Los datos del usuario han sido actualizados exitosamente.")
            self.cerrar_formularios()  # Cerrar ambos formularios
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar categoria: {str(e)}")

class LlamarCategorias:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Categoria por ID")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta e input para el ID del usuario
        lbl_id_categoria = ttk.Label(root, text="ID del Categoria:")
        lbl_id_categoria.pack(pady=5)
        self.entry_id_categoria = ttk.Entry(root)
        self.entry_id_categoria.pack(pady=5)

        # Botón para enviar el ID del usuario
        btn_enviar = ttk.Button(root, text="Consultar Categoria", command=self.consultar_categoria)
        btn_enviar.pack(pady=10)

    def consultar_categoria(self):
        # Obtener el ID del usuario desde el campo de entrada
        id_categoria = self.entry_id_categoria.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            v_cursor = self.cursor.var(cx_Oracle.CURSOR)

            # Ejecutar el procedimiento almacenado
            self.cursor.callproc('VER_CATEGORIAAC', (v_cursor, id_categoria))

            # Obtener los resultados del cursor usando fetchall()
            result_set = v_cursor.getvalue().fetchall()

            if result_set:  # Asegurarse de que haya resultados
                # Mostrar los detalles en un nuevo formulario
                categoria_info = result_set[0]
                categoria_details_form = tk.Toplevel(self.root)
                EditarCategoria(categoria_details_form, categoria_info, self.connection, self)
            else:
                messagebox.showinfo("Categoria no encontrado", "No se encontró ningún categoria con el ID especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Llamar(root)
    root.mainloop()
