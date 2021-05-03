from tkinter import *
import sqlite3
root=Tk()
root.title("database")
def add():
    #connect to database
    connect=sqlite3.connect("address_book.db")
    c=connect.cursor()
    #insert into table
    c.execute("INSERT INTO addreses VALUES (:e1, :e2, :e3, :e4, :e5, :e6)",{
        'e1':e1.get(),
        'e2' :e2.get(),
        "e3" :e3.get(),
        "e4" :e4.get(),
        "e5":e5.get(),
        "e6":e6.get()

    })
    print("addresses inserted")
    connect.commit()
    connect.close()

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
first_name_label=Label(root,text="first name")
last_name_label=Label(root,text="last name")
address_label=Label(root,text="address")
city_label=Label(root,text="city")
state_label=Label(root,text="state")
zipcode_label=Label(root,text="zipcode")
def query():
    connect=sqlite3.connect("address_book.db")
    c=connect.cursor()
    c.execute("SELECT *, oid FROM addreses")
    records=c.fetchall()
    #print(records)
    print_records=""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) +"\n"
    query_label=Label(root,text=print_records)
    query_label.grid(row=7,column=5)
    connect.commit()
    connect.close()


first_name_label.grid(row=1,column=0)
last_name_label.grid(row=2,column=0)
address_label.grid(row=3,column=0)
city_label.grid(row=4,column=0)
state_label.grid(row=5,column=0)
zipcode_label.grid(row=6,column=0)
e1=Entry(root,width=20)
e2=Entry(root,width=20)
e3=Entry(root,width=20)
e4=Entry(root,width=20)
e5=Entry(root,width=20)
e6=Entry(root,width=20)
e1.grid(row=1,column=3,columnspan=2)
e2.grid(row=2,column=3,columnspan=2)
e3.grid(row=3,column=3,columnspan=2)
e4.grid(row=4,column=3,columnspan=2)
e5.grid(row=5,column=3,columnspan=2)
e6.grid(row=6,column=3,columnspan=2)
add_buttom=Button(root,text="add",command=add)
add_buttom.grid(row=7,column=2)
show_buttom=Button(root,text="show",command=query)
show_buttom.grid(row=7,column=3)





#create an database and connect to database
connect=sqlite3.connect("address_book.db")
#creating an cursor
#cursor class is an instance using which you can invoke methods that
#excute SQLITe statements,fetch data from the results sets of query
c=connect.cursor()

c.execute("""CREATE TABLE addreses(
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer

)
""")
print("table created successfully")
#commit change
connect.commit()
#close connection
connect.close()

mainloop()