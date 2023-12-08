import tkinter as tk
import cx_Oracle
from tkinter import ttk, messagebox


class FacturasFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Factura")

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
        etiquetas = ["SUBTOTAL", "IMPUESTOS", "TOTAL", "ENVIO"]
        self.campos = {}
        for i, etiqueta in enumerate(etiquetas):
            tk.Label(root, text=etiqueta).grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            self.campos[etiqueta] = tk.Entry(root)
            self.campos[etiqueta].grid(row=i, column=1, padx=10, pady=5)

       # Contenedor para los Combobox
        combo_frame = tk.Frame(root)
        combo_frame.grid(row=len(etiquetas), column=0, columnspan=2, pady=5)

        # Etiqueta y combobox para el rol
        tk.Label(combo_frame, text="Orden").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.combo_orden = ttk.Combobox(combo_frame, state="readonly")
        self.combo_orden.grid(row=0, column=1, padx=10, pady=5)

        self.cargar_ordenes()


        tk.Label(combo_frame, text="Emisor").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.combo_emisor = ttk.Combobox(combo_frame, state="readonly")
        self.combo_emisor.grid(row=1, column=1, padx=10, pady=5)
        
        self.cargar_emisor()


        tk.Label(combo_frame, text="Receptor").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.combo_receptor = ttk.Combobox(combo_frame, state="readonly")
        self.combo_receptor.grid(row=2, column=1, padx=10, pady=5)

        self.cargar_receptores()
        
        
        

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Enviar", command=self.enviar_formulario)
        btn_enviar.grid(row=len(etiquetas) + 1, column=0, columnspan=2, pady=10)

    def cargar_ordenes(self):
        # Limpiar valores del Combobox
        self.combo_orden.set("")

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_ORDENEEEEES', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Configurar valores del Combobox
            ordenes = [row[0] for row in result_set]
            self.combo_orden["values"] = ordenes

    def cargar_emisor(self):
        # Limpiar valores del Combobox
        self.combo_emisor.set("")

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_USUARIOS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Configurar valores del Combobox
            emisors = [row[1] for row in result_set]
            self.combo_emisor["values"] = emisors

    def cargar_receptores(self):
        # Limpiar valores del Combobox
        self.combo_receptor.set("")

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_USUARIOS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Configurar valores del Combobox
            cubertas = [row[1] for row in result_set]
            self.combo_receptor["values"] = cubertas

    def enviar_formulario(self):
        # Obtener los valores del formulario
        valores = [self.campos[etiqueta].get() for etiqueta in self.campos]
        orden_seleccionado = self.combo_orden.get()
        emisor_seleccionado = self.combo_emisor.get()
        receptor_seleccionado = self.combo_receptor.get()

        if not all(valores) or not orden_seleccionado:
            print("Por favor, complete todos los campos.")
            return
        

        # Ejecutar el procedimiento almacenado con los valores del formulario
        self.cursor.callproc('INSERTAR_FACTURA', valores + [orden_seleccionado, emisor_seleccionado, receptor_seleccionado])
        self.connection.commit()

        # Limpiar los campos del formulario
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        self.combo_orden.set("")
        self.combo_emisor.set("")
        self.combo_receptor.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = FacturasFormulario(root)
    root.mainloop()



#-VistaFacturas----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class VistaFactura:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Facturas")

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
        self.tree = ttk.Treeview(root, columns=('ID_FACTURA', 'CANTIDAD_PERSONAS', 'PRODUCTO', 'EMISOR', 'RECEPTOR'), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar encabezados de columnas
        for col in ('ID_FACTURA', 'CANTIDAD_PERSONAS', 'PRODUCTO', 'EMISOR', 'RECEPTOR'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Botón para cargar y mostrar facturas
        btn_cargar = ttk.Button(root, text="Cargar Facturas", command=self.cargar_facturas)
        btn_cargar.pack(pady=10)

    def cargar_facturas(self):
        # Limpiar árbol antes de cargar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Crear un cursor para el procedimiento almacenado
        v_cursor = self.cursor.var(cx_Oracle.CURSOR)

        # Ejecutar el procedimiento almacenado
        self.cursor.callproc('VER_FACTURAS', (v_cursor,))

        # Obtener los resultados del cursor usando fetchall()
        result_set = v_cursor.getvalue().fetchall()

        if result_set:  # Asegurarse de que haya resultados
            # Insertar filas en el Treeview
            for row in result_set:
                self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaFactura(root)
    root.mainloop()



#-EliminarFacturas-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EliminarFacturas:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario para Eliminar Factura")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta y campo de entrada para el ID del factura a eliminar
        tk.Label(root, text="ID del Factura a Eliminar").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_id_factura = tk.Entry(root)
        self.entry_id_factura.grid(row=0, column=1, padx=10, pady=5)

        # Botón para enviar el formulario
        btn_enviar = ttk.Button(root, text="Eliminar Factura", command=self.eliminar_factura)
        btn_enviar.grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_factura(self):
        # Obtener el ID del factura a eliminar
        id_factura = int(self.entry_id_factura.get())

        # Ejecutar el procedimiento almacenado para eliminar el factura
        self.cursor.callproc('ELIMINAR_FACTURA', (id_factura,))
        self.connection.commit()

        # Limpiar el campo del formulario
        self.entry_id_factura.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarFacturas(root)
    root.mainloop()


#-EditarFacturas-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EditarFactura:
    def __init__(self, master, user_info, connection, main_form):
        self.master = master
        self.master.title("Detalles del Factura")

        # Referencia al formulario principal
        self.main_form = main_form

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Conexión a la base de datos
        self.connection = connection

        # Crear campos de texto para mostrar/permitir la edición de la información del factura
        self.campos = {}
        labels = ["ID_FACTURA", "CANTIDAD_PERSONAS", "PRODUCTO", "EMISOR", "RECEPTOR"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=f"{label}:").grid(row=i, column=0, pady=5)
            self.campos[label] = tk.Entry(self.frame)
            self.campos[label].insert(0, user_info[i])  # Insertar la información en el campo
            self.campos[label].grid(row=i, column=1, padx=10, pady=5)

        # Botón para actualizar los datos del factura
        btn_actualizar = ttk.Button(self.frame, text="Actualizar Factura", command=self.actualizar_factura)
        btn_actualizar.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Configurar el evento de cierre del formulario
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_formularios)

    def cerrar_formularios(self):
        # Cerrar ambos formularios
        self.master.destroy()
        self.main_form.root.destroy()

    def actualizar_factura(self):
        # Obtener los nuevos datos del factura
        nuevos_datos = {}
        for label, entry in self.campos.items():
            nuevos_datos[label] = entry.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            cursor = self.connection.cursor()

            # Ejecutar el procedimiento almacenado ACTUALIZAR_FACTURA
            cursor.callproc(
                'ACTUALIZAR_FACTURA',
                (
                    nuevos_datos["ID_FACTURA"],
                    nuevos_datos["CANTIDAD_PERSONAS"],
                    nuevos_datos["PRODUCTO"],
                    nuevos_datos["EMISOR"],
                    nuevos_datos["RECEPTOR"]
                )
            )

            # Confirmar los cambios en la base de datos
            self.connection.commit()

            # Cerrar el cursor
            cursor.close()

            # messagebox.showinfo("Factura Actualizado", "Los datos del factura han sido actualizados exitosamente.")
            self.cerrar_formularios()  # Cerrar ambos formularios
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar factura: {str(e)}")

class LlamarFacturas:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Factura por ID")

        # Conectar a la base de datos Oracle
        self.connection = cx_Oracle.connect(
            user='CAKES',
            password='123456',
            dsn='localhost:1521/orcl',
            encoding='UTF-8'
        )

        # Crear un cursor
        self.cursor = self.connection.cursor()

        # Etiqueta e input para el ID del factura
        lbl_id_factura = ttk.Label(root, text="ID del Factura:")
        lbl_id_factura.pack(pady=5)
        self.entry_id_factura = ttk.Entry(root)
        self.entry_id_factura.pack(pady=5)

        # Botón para enviar el ID del factura
        btn_enviar = ttk.Button(root, text="Consultar Factura", command=self.consultar_factura)
        btn_enviar.pack(pady=10)

    def consultar_factura(self):
        # Obtener el ID del factura desde el campo de entrada
        id_factura = self.entry_id_factura.get()

        try:
            # Crear un cursor para el procedimiento almacenado
            v_cursor = self.cursor.var(cx_Oracle.CURSOR)

            # Ejecutar el procedimiento almacenado
            self.cursor.callproc('VER_FACTURASAC', (v_cursor, id_factura))

            # Obtener los resultados del cursor usando fetchall()
            result_set = v_cursor.getvalue().fetchall()

            if result_set:  # Asegurarse de que haya resultados
                # Mostrar los detalles en un nuevo formulario
                user_info = result_set[0]
                user_details_form = tk.Toplevel(self.root)
                EditarFactura(user_details_form, user_info, self.connection, self)
            else:
                messagebox.showinfo("Factura no encontrado", "No se encontró ningún factura con el ID especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Llamar(root)
    root.mainloop()
