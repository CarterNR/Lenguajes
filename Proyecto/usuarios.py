import tkinter as tk
import cx_Oracle
from tkinter import ttk, messagebox

cx_Oracle.init_oracle_client(lib_dir=r"D:\Oracle\instantclient_19_21")

class UsuariosFormulario:
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
        etiquetas = ["Nombre", "Apellido 1", "Apellido 2", "Teléfono", "Correo", "Clave", "Dirección"]
        self.campos = {}
        for i, etiqueta in enumerate(etiquetas):
            tk.Label(root, text=etiqueta).grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            self.campos[etiqueta] = tk.Entry(root)
            self.campos[etiqueta].grid(row=i, column=1, padx=10, pady=5)

        # Etiqueta y combobox para el rol
        tk.Label(root, text="Rol").grid(row=len(etiquetas), column=0, sticky=tk.W, padx=10, pady=5)
        self.combo_rol = ttk.Combobox(root, state="readonly")
        self.combo_rol.grid(row=len(etiquetas), column=1, padx=10, pady=5)

        # Cargar roles automáticamente al iniciar
        self.cargar_roles()

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Enviar", command=self.enviar_formulario)
        btn_enviar.grid(row=len(etiquetas) + 1, column=0, columnspan=2, pady=10)

    def cargar_roles(self):
        # Limpiar valores del Combobox
        self.combo_rol.set("")

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_ROLES', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Configurar valores del Combobox
            roles = [row[1] for row in result_set]
            self.combo_rol["values"] = roles

    def enviar_formulario(self):
        # Obtener los valores del formulario
        valores = [self.campos[etiqueta].get() for etiqueta in self.campos]
        rol_seleccionado = self.combo_rol.get()

        if not all(valores) or not rol_seleccionado:
            print("Por favor, complete todos los campos y seleccione un rol.")
            return

        # Ejecutar el procedimiento almacenado con los valores del formulario
        self.cursor.callproc('INSERTAR_USUARIO', valores + [rol_seleccionado])
        self.connection.commit()

        # Limpiar los campos del formulario
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        self.combo_rol.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = UsuariosFormulario(root)
    root.mainloop()



#-VistaUsuarios----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class VistaUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Usuarios")

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
        self.tree = ttk.Treeview(root, columns=('ID_USUARIO', 'NOMBRE', 'APELIIDO1', 'APELLIDO2', 'TELEFONO', 'CORREO', 'CLAVE', 'DIRECCION', 'ROL'), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar encabezados de columnas
        for col in ('ID_USUARIO', 'NOMBRE', 'APELIIDO1', 'APELLIDO2', 'TELEFONO', 'CORREO', 'CLAVE', 'DIRECCION', 'ROL'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Botón para cargar y mostrar usuarios
        btn_cargar = ttk.Button(root, text="Cargar Usuarios", command=self.cargar_usuarios)
        btn_cargar.pack(pady=10)

    def cargar_usuarios(self):
        # Limpiar árbol antes de cargar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_USUARIOS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Insertar filas en el Treeview
            for row in result_set:
                self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaUsuario(root)
    root.mainloop()



#-EliminarUsuarios-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EliminarUsuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario para Eliminar Usuario")

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
        tk.Label(root, text="ID del Usuario a Eliminar").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_id_usuario = tk.Entry(root)
        self.entry_id_usuario.grid(row=0, column=1, padx=10, pady=5)

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Eliminar Usuario", command=self.eliminar_usuario)
        btn_enviar.grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_usuario(self):
        # Obtener el ID del usuario a eliminar
        id_usuario = int(self.entry_id_usuario.get())

        # Ejecutar el procedimiento almacenado para eliminar el usuario
        self.cursor.callproc('ELIMINAR_USUARIO', (id_usuario,))
        self.connection.commit()

        # Limpiar el campo del formulario
        self.entry_id_usuario.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarUsuarios(root)
    root.mainloop()


#-EditarUsuarios-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EditarUsuario:
    def __init__(self, master, user_info, connection, main_form):
        self.master = master
        self.master.title("Detalles del Usuario")

        # Referencia al formulario principal
        self.main_form = main_form

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Conexión a la base de datos
        self.connection = connection

        # Crear campos de texto para mostrar/permitir la edición de la información del usuario
        self.campos = {}
        labels = ["ID_USUARIO", "NOMBRE", "APELIIDO1", "APELLIDO2", "TELEFONO", "CORREO", "CLAVE", "DIRECCION", "ROL"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=f"{label}:").grid(row=i, column=0, pady=5)
            self.campos[label] = tk.Entry(self.frame)
            self.campos[label].insert(0, user_info[i])  # Insertar la información en el campo
            self.campos[label].grid(row=i, column=1, padx=10, pady=5)

        # Botón para actualizar los datos del usuario
        btn_actualizar = ttk.Button(self.frame, text="Actualizar Usuario", command=self.actualizar_usuario)
        btn_actualizar.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Configurar el evento de cierre del formulario
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_formularios)

    def cerrar_formularios(self):
        # Cerrar ambos formularios
        self.master.destroy()
        self.main_form.root.destroy()

    def actualizar_usuario(self):
        # Obtener los nuevos datos del usuario
        nuevos_datos = {}
        for label, entry in self.campos.items():
            nuevos_datos[label] = entry.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            cursor = self.connection.cursor()

            # Ejecutar el procedimiento almacenado ACTUALIZAR_USUARIO
            cursor.callproc(
                'ACTUALIZAR_USUARIO',
                (
                    nuevos_datos["ID_USUARIO"],
                    nuevos_datos["NOMBRE"],
                    nuevos_datos["APELIIDO1"],
                    nuevos_datos["APELLIDO2"],
                    nuevos_datos["TELEFONO"],
                    nuevos_datos["CORREO"],
                    nuevos_datos["CLAVE"],
                    nuevos_datos["DIRECCION"],
                    nuevos_datos["ROL"]
                )
            )

            # Confirmar los cambios en la base de datos
            self.connection.commit()

            # Cerrar el cursor
            cursor.close()

            # messagebox.showinfo("Usuario Actualizado", "Los datos del usuario han sido actualizados exitosamente.")
            self.cerrar_formularios()  # Cerrar ambos formularios
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar usuario: {str(e)}")

class LlamarUsuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Usuario por ID")

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
        lbl_id_usuario = ttk.Label(root, text="ID del Usuario:")
        lbl_id_usuario.pack(pady=5)
        self.entry_id_usuario = ttk.Entry(root)
        self.entry_id_usuario.pack(pady=5)

        # Botón para enviar el ID del usuario
        btn_enviar = ttk.Button(root, text="Consultar Usuario", command=self.consultar_usuario)
        btn_enviar.pack(pady=10)

    def consultar_usuario(self):
        # Obtener el ID del usuario desde el campo de entrada
        id_usuario = self.entry_id_usuario.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            v_cursor = self.cursor.var(cx_Oracle.CURSOR)

            # Ejecutar el procedimiento almacenado
            self.cursor.callproc('VER_USUARIOSAC', (v_cursor, id_usuario))

            # Obtener los resultados del cursor usando fetchall()
            result_set = v_cursor.getvalue().fetchall()

            if result_set:  # Asegurarse de que haya resultados
                # Mostrar los detalles en un nuevo formulario
                user_info = result_set[0]
                user_details_form = tk.Toplevel(self.root)
                EditarUsuario(user_details_form, user_info, self.connection, self)
            else:
                messagebox.showinfo("Usuario no encontrado", "No se encontró ningún usuario con el ID especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Llamar(root)
    root.mainloop()
