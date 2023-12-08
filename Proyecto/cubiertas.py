import tkinter as tk
import cx_Oracle
from tkinter import ttk, messagebox


class CubiertasFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Cubiertas")

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
        etiquetas = ["Cubierta"]
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
        self.cursor.callproc('INSERTAR_CUBIERTA', valores)
        self.connection.commit()

        # Limpiar los campos del formulario
        for campo in self.campos.values():
            campo.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CubiertasFormulario(root)
    root.mainloop()


#-VerCubiertas-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class VistaCubierta:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Cubiertas")

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
        self.tree = ttk.Treeview(root, columns=('ID_CUBIERTA', 'CUBIERTA'), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar encabezados de columnas
        for col in ('ID_CUBIERTA', 'CUBIERTA'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Botón para cargar y mostrar usuarios
        btn_cargar = ttk.Button(root, text="Cargar Cubiertas", command=self.cargar_cubiertas)
        btn_cargar.pack(pady=10)

    def cargar_cubiertas(self):
        # Limpiar árbol antes de cargar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_CUBIERTAS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Insertar filas en el Treeview
            for row in result_set:
                self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaCubierta(root)
    root.mainloop()


#-EliminarCubiertas-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EliminarCubiertas:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario para Eliminar Cubierta")

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
        tk.Label(root, text="ID del Cubierta a Eliminar").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_id_cubierta = tk.Entry(root)
        self.entry_id_cubierta.grid(row=0, column=1, padx=10, pady=5)

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Eliminar Cubierta", command=self.eliminar_cubierta)
        btn_enviar.grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_cubierta(self):
        # Obtener el ID del usuario a eliminar
        id_cubierta = int(self.entry_id_cubierta.get())

        # Ejecutar el procedimiento almacenado para eliminar el usuario
        self.cursor.callproc('ELIMINAR_CUBIERTA', (id_cubierta,))
        self.connection.commit()

        # Limpiar el campo del formulario
        self.entry_id_cubierta.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarCubiertas(root)
    root.mainloop()


#-EditarUsuarios-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EditarCubierta:
    def __init__(self, master, cubierta_info, connection, main_form):
        self.master = master
        self.master.title("Editar Cubierta")

        # Referencia al formulario principal
        self.main_form = main_form

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Conexión a la base de datos
        self.connection = connection

        # Crear campos de texto para mostrar/permitir la edición de la información del usuario
        self.campos = {}
        labels = ["ID_CUBIERTA", "CUBIERTA"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=f"{label}:").grid(row=i, column=0, pady=5)
            self.campos[label] = tk.Entry(self.frame)
            self.campos[label].insert(0, cubierta_info[i])  # Insertar la información en el campo
            self.campos[label].grid(row=i, column=1, padx=10, pady=5)

        # Botón para actualizar los datos del usuario
        btn_actualizar = ttk.Button(self.frame, text="Actualizar Cubierta", command=self.actualizar_cubierta)
        btn_actualizar.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Configurar el evento de cierre del formulario
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_formularios)

    def cerrar_formularios(self):
        # Cerrar ambos formularios
        self.master.destroy()
        self.main_form.root.destroy()

    def actualizar_cubierta(self):
        # Obtener los nuevos datos del usuario
        nuevos_datos = {}
        for label, entry in self.campos.items():
            nuevos_datos[label] = entry.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            cursor = self.connection.cursor()

            # Ejecutar el procedimiento almacenado ACTUALIZAR_USUARIO
            cursor.callproc(
                'ACTUALIZAR_CUBIERTA',
                (
                    nuevos_datos["ID_CUBIERTA"],
                    nuevos_datos["CUBIERTA"]
                )
            )

            # Confirmar los cambios en la base de datos
            self.connection.commit()

            # Cerrar el cursor
            cursor.close()

            # messagebox.showinfo("Usuario Actualizado", "Los datos del usuario han sido actualizados exitosamente.")
            self.cerrar_formularios()  # Cerrar ambos formularios
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar cubierta: {str(e)}")

class LlamarCubiertas:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Cubierta por ID")

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
        lbl_id_cubierta = ttk.Label(root, text="ID del Cubierta:")
        lbl_id_cubierta.pack(pady=5)
        self.entry_id_cubierta = ttk.Entry(root)
        self.entry_id_cubierta.pack(pady=5)

        # Botón para enviar el ID del usuario
        btn_enviar = ttk.Button(root, text="Consultar Cubierta", command=self.consultar_cubierta)
        btn_enviar.pack(pady=10)

    def consultar_cubierta(self):
        # Obtener el ID del usuario desde el campo de entrada
        id_cubierta = self.entry_id_cubierta.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            v_cursor = self.cursor.var(cx_Oracle.CURSOR)

            # Ejecutar el procedimiento almacenado
            self.cursor.callproc('VER_CUBIERTASAC', (v_cursor, id_cubierta))

            # Obtener los resultados del cursor usando fetchall()
            result_set = v_cursor.getvalue().fetchall()

            if result_set:  # Asegurarse de que haya resultados
                # Mostrar los detalles en un nuevo formulario
                cubierta_info = result_set[0]
                cubierta_details_form = tk.Toplevel(self.root)
                EditarCubierta(cubierta_details_form, cubierta_info, self.connection, self)
            else:
                messagebox.showinfo("Cubierta no encontrado", "No se encontró ningún cubierta con el ID especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Llamar(root)
    root.mainloop()
