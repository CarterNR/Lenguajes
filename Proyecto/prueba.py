import cx_Oracle
import tkinter as tk
cx_Oracle.init_oracle_client(lib_dir=r"D:\Oracle\instantclient_19_21")




try:
    connection=cx_Oracle.connect(
        user='CAKES',
        password='123456',
        dsn='localhost:1521/orcl',
        encoding='UTF-8'
    )
    print(connection.version)
    print("hola")
except cx_Oracle.Error as error:
    print(error)