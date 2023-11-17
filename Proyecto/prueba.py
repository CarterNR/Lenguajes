import cx_Oracle
import tkinter as tk

try:
    connection=cx_Oracle.connect(
        user='CAKES',
        password='123456',
        dsn='localhost:1521/orcl',
        encoding='UTF-8'
    )
    print(connection.version)
except cx_Oracle.Error as error:
        print(error)


