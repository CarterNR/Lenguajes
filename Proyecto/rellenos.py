import tkinter as tk
import cx_Oracle
from tkinter import ttk, messagebox


class RellenosFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Rellenos")

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
        etiquetas = ["Relleno"]
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
        self.cursor.callproc('INSERTAR_RELLENO', valores)
        self.connection.commit()

        # Limpiar los campos del formulario
        for campo in self.campos.values():
            campo.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RellenosFormulario(root)
    root.mainloop()


#-VerRellenos-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class VistaRelleno:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Rellenos")

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
        self.tree = ttk.Treeview(root, columns=('ID_RELLENO', 'RELLENO'), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar encabezados de columnas
        for col in ('ID_RELLENO', 'RELLENO'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Botón para cargar y mostrar usuarios
        btn_cargar = ttk.Button(root, text="Cargar Rellenos", command=self.cargar_rellenos)
        btn_cargar.pack(pady=10)

    def cargar_rellenos(self):
        # Limpiar árbol antes de cargar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_RELLENOS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Insertar filas en el Treeview
            for row in result_set:
                self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaRelleno(root)
    root.mainloop()


#-EliminarRellenos-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EliminarRellenos:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario para Eliminar Relleno")

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
        tk.Label(root, text="ID del Relleno a Eliminar").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_id_relleno = tk.Entry(root)
        self.entry_id_relleno.grid(row=0, column=1, padx=10, pady=5)

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Eliminar Relleno", command=self.eliminar_relleno)
        btn_enviar.grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_relleno(self):
        # Obtener el ID del usuario a eliminar
        id_relleno = int(self.entry_id_relleno.get())

        # Ejecutar el procedimiento almacenado para eliminar el usuario
        self.cursor.callproc('ELIMINAR_RELLENO', (id_relleno,))
        self.connection.commit()

        # Limpiar el campo del formulario
        self.entry_id_relleno.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarRellenos(root)
    root.mainloop()


#-EditarUsuarios-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EditarRelleno:
    def __init__(self, master, relleno_info, connection, main_form):
        self.master = master
        self.master.title("Editar Relleno")

        # Referencia al formulario principal
        self.main_form = main_form

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Conexión a la base de datos
        self.connection = connection

        # Crear campos de texto para mostrar/permitir la edición de la información del usuario
        self.campos = {}
        labels = ["ID_RELLENO", "RELLENO"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=f"{label}:").grid(row=i, column=0, pady=5)
            self.campos[label] = tk.Entry(self.frame)
            self.campos[label].insert(0, relleno_info[i])  # Insertar la información en el campo
            self.campos[label].grid(row=i, column=1, padx=10, pady=5)

        # Botón para actualizar los datos del usuario
        btn_actualizar = ttk.Button(self.frame, text="Actualizar Relleno", command=self.actualizar_relleno)
        btn_actualizar.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Configurar el evento de cierre del formulario
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_formularios)

    def cerrar_formularios(self):
        # Cerrar ambos formularios
        self.master.destroy()
        self.main_form.root.destroy()

    def actualizar_relleno(self):
        # Obtener los nuevos datos del usuario
        nuevos_datos = {}
        for label, entry in self.campos.items():
            nuevos_datos[label] = entry.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            cursor = self.connection.cursor()

            # Ejecutar el procedimiento almacenado ACTUALIZAR_USUARIO
            cursor.callproc(
                'ACTUALIZAR_RELLENO',
                (
                    nuevos_datos["ID_RELLENO"],
                    nuevos_datos["RELLENO"]
                )
            )

            # Confirmar los cambios en la base de datos
            self.connection.commit()

            # Cerrar el cursor
            cursor.close()

            # messagebox.showinfo("Usuario Actualizado", "Los datos del usuario han sido actualizados exitosamente.")
            self.cerrar_formularios()  # Cerrar ambos formularios
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar relleno: {str(e)}")

class LlamarRellenos:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Relleno por ID")

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
        lbl_id_relleno = ttk.Label(root, text="ID del Relleno:")
        lbl_id_relleno.pack(pady=5)
        self.entry_id_relleno = ttk.Entry(root)
        self.entry_id_relleno.pack(pady=5)

        # Botón para enviar el ID del usuario
        btn_enviar = ttk.Button(root, text="Consultar Relleno", command=self.consultar_relleno)
        btn_enviar.pack(pady=10)

    def consultar_relleno(self):
        # Obtener el ID del usuario desde el campo de entrada
        id_relleno = self.entry_id_relleno.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            v_cursor = self.cursor.var(cx_Oracle.CURSOR)

            # Ejecutar el procedimiento almacenado
            self.cursor.callproc('VER_RELLENOSAC', (v_cursor, id_relleno))

            # Obtener los resultados del cursor usando fetchall()
            result_set = v_cursor.getvalue().fetchall()

            if result_set:  # Asegurarse de que haya resultados
                # Mostrar los detalles en un nuevo formulario
                relleno_info = result_set[0]
                relleno_details_form = tk.Toplevel(self.root)
                EditarRelleno(relleno_details_form, relleno_info, self.connection, self)
            else:
                messagebox.showinfo("Relleno no encontrado", "No se encontró ningún relleno con el ID especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Llamar(root)
    root.mainloop()
