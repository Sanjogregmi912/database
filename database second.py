from tkinter import *
import sqlite3
root=Tk()
#create an database  and connecting
connect =sqlite3.connect("registration form")
#creating an cursor
c=connect.cursor()
c.execute("""CREATE TABLE addreses(
            





""")