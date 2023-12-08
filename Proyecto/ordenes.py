import tkinter as tk
import cx_Oracle
from tkinter import ttk, messagebox


class OrdenesFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Orden")

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
        etiquetas = ["Cantidad personas"]
        self.campos = {}
        for i, etiqueta in enumerate(etiquetas):
            tk.Label(root, text=etiqueta).grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            self.campos[etiqueta] = tk.Entry(root)
            self.campos[etiqueta].grid(row=i, column=1, padx=10, pady=5)

       # Contenedor para los Combobox
        combo_frame = tk.Frame(root)
        combo_frame.grid(row=len(etiquetas), column=0, columnspan=2, pady=5)

        # Etiqueta y combobox para el rol
        tk.Label(combo_frame, text="Descripcion").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.combo_descripcion = ttk.Combobox(combo_frame, state="readonly")
        self.combo_descripcion.grid(row=0, column=1, padx=10, pady=5)

        self.cargar_productos()


        tk.Label(combo_frame, text="Relleno").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.combo_relleno = ttk.Combobox(combo_frame, state="readonly")
        self.combo_relleno.grid(row=1, column=1, padx=10, pady=5)
        
        self.cargar_rellenos()


        tk.Label(combo_frame, text="Cubierta").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.combo_cubierta = ttk.Combobox(combo_frame, state="readonly")
        self.combo_cubierta.grid(row=2, column=1, padx=10, pady=5)

        self.cargar_cubiertas()
        
        
        

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Enviar", command=self.enviar_formulario)
        btn_enviar.grid(row=len(etiquetas) + 1, column=0, columnspan=2, pady=10)

    def cargar_productos(self):
        # Limpiar valores del Combobox
        self.combo_descripcion.set("")

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_PRODUCTOS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Configurar valores del Combobox
            productos = [row[1] for row in result_set]
            self.combo_descripcion["values"] = productos

    def cargar_rellenos(self):
        # Limpiar valores del Combobox
        self.combo_relleno.set("")

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_RELLENOS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Configurar valores del Combobox
            rellenos = [row[1] for row in result_set]
            self.combo_relleno["values"] = rellenos

    def cargar_cubiertas(self):
        # Limpiar valores del Combobox
        self.combo_cubierta.set("")

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_CUBIERTAS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Configurar valores del Combobox
            cubertas = [row[1] for row in result_set]
            self.combo_cubierta["values"] = cubertas

    def enviar_formulario(self):
        # Obtener los valores del formulario
        valores = [self.campos[etiqueta].get() for etiqueta in self.campos]
        descripcion_seleccionado = self.combo_descripcion.get()
        relleno_seleccionado = self.combo_relleno.get()
        cubierta_seleccionado = self.combo_cubierta.get()

        if not all(valores) or not descripcion_seleccionado:
            print("Por favor, complete todos los campos.")
            return
        

        # Ejecutar el procedimiento almacenado con los valores del formulario
        self.cursor.callproc('INSERTAR_ORDEN', valores + [descripcion_seleccionado, relleno_seleccionado, cubierta_seleccionado])
        self.connection.commit()

        # Limpiar los campos del formulario
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        self.combo_descripcion.set("")
        self.combo_relleno.set("")
        self.combo_cubierta.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = OrdenesFormulario(root)
    root.mainloop()



#-VistaOrdenes----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class VistaOrden:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Ordenes")

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
        self.tree = ttk.Treeview(root, columns=('ID_ORDEN', 'CANTIDAD_PERSONAS', 'PRODUCTO', 'RELLENO', 'CUBIERTA'), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar encabezados de columnas
        for col in ('ID_ORDEN', 'CANTIDAD_PERSONAS', 'PRODUCTO', 'RELLENO', 'CUBIERTA'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Botón para cargar y mostrar ordenes
        btn_cargar = ttk.Button(root, text="Cargar Ordenes", command=self.cargar_ordenes)
        btn_cargar.pack(pady=10)

    def cargar_ordenes(self):
        # Limpiar árbol antes de cargar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_ORDENES', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Insertar filas en el Treeview
            for row in result_set:
                self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaOrden(root)
    root.mainloop()



#-EliminarOrdenes-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EliminarOrdenes:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario para Eliminar Orden")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta y campo de entrada para el ID del orden a eliminar
        tk.Label(root, text="ID del Orden a Eliminar").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_id_orden = tk.Entry(root)
        self.entry_id_orden.grid(row=0, column=1, padx=10, pady=5)

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Eliminar Orden", command=self.eliminar_orden)
        btn_enviar.grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_orden(self):
        # Obtener el ID del orden a eliminar
        id_orden = int(self.entry_id_orden.get())

        # Ejecutar el procedimiento almacenado para eliminar el orden
        self.cursor.callproc('ELIMINAR_ORDEN', (id_orden,))
        self.connection.commit()

        # Limpiar el campo del formulario
        self.entry_id_orden.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarOrdenes(root)
    root.mainloop()


#-EditarOrdenes-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EditarOrden:
    def __init__(self, master, user_info, connection, main_form):
        self.master = master
        self.master.title("Detalles del Orden")

        # Referencia al formulario principal
        self.main_form = main_form

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Conexión a la base de datos
        self.connection = connection

        # Crear campos de texto para mostrar/permitir la edición de la información del orden
        self.campos = {}
        labels = ["ID_ORDEN", "CANTIDAD_PERSONAS", "PRODUCTO", "RELLENO", "CUBIERTA"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=f"{label}:").grid(row=i, column=0, pady=5)
            self.campos[label] = tk.Entry(self.frame)
            self.campos[label].insert(0, user_info[i])  # Insertar la información en el campo
            self.campos[label].grid(row=i, column=1, padx=10, pady=5)

        # Botón para actualizar los datos del orden
        btn_actualizar = ttk.Button(self.frame, text="Actualizar Orden", command=self.actualizar_orden)
        btn_actualizar.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Configurar el evento de cierre del formulario
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_formularios)

    def cerrar_formularios(self):
        # Cerrar ambos formularios
        self.master.destroy()
        self.main_form.root.destroy()

    def actualizar_orden(self):
        # Obtener los nuevos datos del orden
        nuevos_datos = {}
        for label, entry in self.campos.items():
            nuevos_datos[label] = entry.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            cursor = self.connection.cursor()

            # Ejecutar el procedimiento almacenado ACTUALIZAR_ORDEN
            cursor.callproc(
                'ACTUALIZAR_ORDEN',
                (
                    nuevos_datos["ID_ORDEN"],
                    nuevos_datos["CANTIDAD_PERSONAS"],
                    nuevos_datos["PRODUCTO"],
                    nuevos_datos["RELLENO"],
                    nuevos_datos["CUBIERTA"]
                )
            )

            # Confirmar los cambios en la base de datos
            self.connection.commit()

            # Cerrar el cursor
            cursor.close()

            # messagebox.showinfo("Orden Actualizado", "Los datos del orden han sido actualizados exitosamente.")
            self.cerrar_formularios()  # Cerrar ambos formularios
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar orden: {str(e)}")

class LlamarOrdenes:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Orden por ID")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta e input para el ID del orden
        lbl_id_orden = ttk.Label(root, text="ID del Orden:")
        lbl_id_orden.pack(pady=5)
        self.entry_id_orden = ttk.Entry(root)
        self.entry_id_orden.pack(pady=5)

        # Botón para enviar el ID del orden
        btn_enviar = ttk.Button(root, text="Consultar Orden", command=self.consultar_orden)
        btn_enviar.pack(pady=10)

    def consultar_orden(self):
        # Obtener el ID del orden desde el campo de entrada
        id_orden = self.entry_id_orden.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            v_cursor = self.cursor.var(cx_Oracle.CURSOR)

            # Ejecutar el procedimiento almacenado
            self.cursor.callproc('VER_ORDENESAC', (v_cursor, id_orden))

            # Obtener los resultados del cursor usando fetchall()
            result_set = v_cursor.getvalue().fetchall()

            if result_set:  # Asegurarse de que haya resultados
                # Mostrar los detalles en un nuevo formulario
                user_info = result_set[0]
                user_details_form = tk.Toplevel(self.root)
                EditarOrden(user_details_form, user_info, self.connection, self)
            else:
                messagebox.showinfo("Orden no encontrado", "No se encontró ningún orden con el ID especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Llamar(root)
    root.mainloop()
