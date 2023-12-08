import tkinter as tk
import cx_Oracle
from tkinter import ttk, messagebox


class InventarioFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Usuario")

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
        etiquetas = ["Cantidad"]
        self.campos = {}
        for i, etiqueta in enumerate(etiquetas):
            tk.Label(root, text=etiqueta).grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            self.campos[etiqueta] = tk.Entry(root)
            self.campos[etiqueta].grid(row=i, column=1, padx=10, pady=5)

        # Etiqueta y combobox para el rol
        tk.Label(root, text="Descripcion").grid(row=len(etiquetas), column=0, sticky=tk.W, padx=10, pady=5)
        self.combo_descripcion = ttk.Combobox(root, state="readonly")
        self.combo_descripcion.grid(row=len(etiquetas), column=1, padx=10, pady=5)

        # Cargar roles automáticamente al iniciar
        self.cargar_descripcion()

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Enviar", command=self.enviar_formulario)
        btn_enviar.grid(row=len(etiquetas) + 1, column=0, columnspan=2, pady=10)

    def cargar_descripcion(self):
        # Limpiar valores del Combobox
        self.combo_descripcion.set("")

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_PRODCUTOS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Configurar valores del Combobox
            productos = [row[1] for row in result_set]
            self.combo_descripcion["values"] = productos

    def enviar_formulario(self):
        # Obtener los valores del formulario
        valores = [self.campos[etiqueta].get() for etiqueta in self.campos]
        rol_seleccionado = self.combo_descripcion.get()

        if not all(valores) or not rol_seleccionado:
            print("Por favor, complete todos los campos y seleccione un rol.")
            return

        # Ejecutar el procedimiento almacenado con los valores del formulario
        self.cursor.callproc('INSERTAR_INVENTARIO', valores + [rol_seleccionado])
        self.connection.commit()

        # Limpiar los campos del formulario
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        self.combo_descripcion.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioFormulario(root)
    root.mainloop()


#-VistaInventarios----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class VistaInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Inventarios")

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
        self.tree = ttk.Treeview(root, columns=('ID_INVENTARIO', 'CANTIDAD', 'PRODUCTO'), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar encabezados de columnas
        for col in ('ID_INVENTARIO', 'CANTIDAD', 'PRODUCTO'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Botón para cargar y mostrar inventarios
        btn_cargar = ttk.Button(root, text="Cargar Inventarios", command=self.cargar_inventarios)
        btn_cargar.pack(pady=10)

    def cargar_inventarios(self):
        # Limpiar árbol antes de cargar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_INVENTARIOS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Insertar filas en el Treeview
            for row in result_set:
                self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaInventario(root)
    root.mainloop()



#-EliminarInventarios-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EliminarInventarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario para Eliminar Inventario")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta y campo de entrada para el ID del inventario a eliminar
        tk.Label(root, text="ID del Inventario a Eliminar").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_id_inventario = tk.Entry(root)
        self.entry_id_inventario.grid(row=0, column=1, padx=10, pady=5)

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Eliminar Inventario", command=self.eliminar_inventario)
        btn_enviar.grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_inventario(self):
        # Obtener el ID del inventario a eliminar
        id_inventario = int(self.entry_id_inventario.get())

        # Ejecutar el procedimiento almacenado para eliminar el inventario
        self.cursor.callproc('ELIMINAR_INVENTARIO', (id_inventario,))
        self.connection.commit()

        # Limpiar el campo del formulario
        self.entry_id_inventario.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarInventarios(root)
    root.mainloop()


#-EditarInventarios-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EditarInventario:
    def __init__(self, master, user_info, connection, main_form):
        self.master = master
        self.master.title("Detalles del Inventario")

        # Referencia al formulario principal
        self.main_form = main_form

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Conexión a la base de datos
        self.connection = connection

        # Crear campos de texto para mostrar/permitir la edición de la información del inventario
        self.campos = {}
        labels = ["ID_INVENTARIO", "CANTIDAD", "PRODUCTO"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=f"{label}:").grid(row=i, column=0, pady=5)
            self.campos[label] = tk.Entry(self.frame)
            self.campos[label].insert(0, user_info[i])  # Insertar la información en el campo
            self.campos[label].grid(row=i, column=1, padx=10, pady=5)

        # Botón para actualizar los datos del inventario
        btn_actualizar = ttk.Button(self.frame, text="Actualizar Inventario", command=self.actualizar_inventario)
        btn_actualizar.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Configurar el evento de cierre del formulario
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_formularios)

    def cerrar_formularios(self):
        # Cerrar ambos formularios
        self.master.destroy()
        self.main_form.root.destroy()

    def actualizar_inventario(self):
        # Obtener los nuevos datos del inventario
        nuevos_datos = {}
        for label, entry in self.campos.items():
            nuevos_datos[label] = entry.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            cursor = self.connection.cursor()

            # Ejecutar el procedimiento almacenado ACTUALIZAR_INVENTARIO
            cursor.callproc(
                'ACTUALIZAR_INVENTARIO',
                (
                    nuevos_datos["ID_INVENTARIO"],
                    nuevos_datos["CANTIDAD"],
                    nuevos_datos["PRODUCTO"]
                )
            )

            # Confirmar los cambios en la base de datos
            self.connection.commit()

            # Cerrar el cursor
            cursor.close()

            # messagebox.showinfo("Inventario Actualizado", "Los datos del inventario han sido actualizados exitosamente.")
            self.cerrar_formularios()  # Cerrar ambos formularios
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar inventario: {str(e)}")

class LlamarInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Inventario por ID")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta e input para el ID del inventario
        lbl_id_inventario = ttk.Label(root, text="ID del Inventario:")
        lbl_id_inventario.pack(pady=5)
        self.entry_id_inventario = ttk.Entry(root)
        self.entry_id_inventario.pack(pady=5)

        # Botón para enviar el ID del inventario
        btn_enviar = ttk.Button(root, text="Consultar Inventario", command=self.consultar_inventario)
        btn_enviar.pack(pady=10)

    def consultar_inventario(self):
        # Obtener el ID del inventario desde el campo de entrada
        id_inventario = self.entry_id_inventario.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            v_cursor = self.cursor.var(cx_Oracle.CURSOR)

            # Ejecutar el procedimiento almacenado
            self.cursor.callproc('VER_INVENTARIOSAC', (v_cursor, id_inventario))

            # Obtener los resultados del cursor usando fetchall()
            result_set = v_cursor.getvalue().fetchall()

            if result_set:  # Asegurarse de que haya resultados
                # Mostrar los detalles en un nuevo formulario
                user_info = result_set[0]
                user_details_form = tk.Toplevel(self.root)
                EditarInventario(user_details_form, user_info, self.connection, self)
            else:
                messagebox.showinfo("Inventario no encontrado", "No se encontró ningún inventario con el ID especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Llamar(root)
    root.mainloop()
