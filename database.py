from tkinter import *
import sqlite3
root=Tk()
root.title("database")
#_______________________________________________________________
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
#_________________________________
first_name_label=Label(root,text="first name")
last_name_label=Label(root,text="last name")
address_label=Label(root,text="address")
city_label=Label(root,text="city")
state_label=Label(root,text="state")
zipcode_label=Label(root,text="zipcode")
select_id=Label(root,text="select id")
#________________________________________________________________
def query():
    connect=sqlite3.connect("address_book.db")
    c=connect.cursor()
    c.execute("SELECT *, oid FROM addreses")
    records=c.fetchall()
    #print(records)
    print_records=""
    for record in records:
        print_records += str(record[1])+ "\t" +str(record[6])+ "\n"
    query_label=Label(root,text=print_records)
    query_label.grid(row=13,column=2)
    connect.commit()
    connect.close()
#____________________________________________
def delete() :
    connect=sqlite3.connect("address_book.db")
    c=connect.cursor()
    c.execute("DELETE from addreses WHERE oid = "+ delete_entry.get())
    print("delete sucessfullY")
    c.execute("SELECT *, oid FROM addreses")
    records = c.fetchall()
    # print(records)
    print_records = ""
    for record in records:
        print_records += str(record[1]) + "\t" + str(record[6]) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=14, column=2)
    connect.commit()
    connect.close()
def update():
    editor=Tk()
    editor.title("UPDATE DATA")
    connect=sqlite3.connect("address_book.db")
    c=connect.cursor()
    record_id=delete_entry.get()
    c.execute("SELECT * FROM addreses WHERE oid= "+record_id)
    records=c.fetchall()

    #for creting the text box in new window
    first_name_editor=Entry(editor,width=20)
    first_name_editor.grid(row=1,column=1)

    last_name_editor=Entry(editor,width=20)
    last_name_editor.grid(row=2,column=1)

    address_label_editor=Entry(editor,width=20)
    address_label_editor.grid(row=3,column=1)

    city_editor=Entry(editor,width=20)
    city_editor.grid(row=4,column=1)

    state_editor =Entry(editor,width=20)
    state_editor.grid(row=5,column=1)

    zipcode_editor=Entry(editor,width=20)
    zipcode_editor.grid(row=6,column=1)

    for record in records:
        first_name_editor.insert(0,record[0])
        last_name_editor.insert(0,record[1])
        address_label_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])

    first_name_label=Label(editor,text="first name")
    first_name_label.grid(row=1,column=0)
    last_name_label=Label(editor,text="last name")
    last_name_label.grid(row=2,column=0)
    state_label=Label(editor,text="State")
    state_label.grid(row=3,column=0)
    address_label=Label(editor,text="address")
    address_label.grid(row=4,column=0)
    city_label=Label(editor,text="city")
    city_label.grid(row=5,column=0)
    zipcode_label=Label(editor,text="zipcode")
    zipcode_label.grid(row=6,column=0)

    save_buttom=Button(editor,text="Save",width="20")
    save_buttom.grid(row=7,column=2,columnspan=2)


#___________________________________________
first_name_label.grid(row=1,column=0)
last_name_label.grid(row=2,column=0)
address_label.grid(row=3,column=0)
city_label.grid(row=4,column=0)
state_label.grid(row=5,column=0)
zipcode_label.grid(row=6,column=0)
select_id.grid(row=9,column=1)
#______________________________________


e1=Entry(root,width=20)
e2=Entry(root,width=20)
e3=Entry(root,width=20)
e4=Entry(root,width=20)
e5=Entry(root,width=20)
e6=Entry(root,width=20)
#_________________________________________-
e1.grid(row=1,column=3,columnspan=2)
e2.grid(row=2,column=3,columnspan=2)
e3.grid(row=3,column=3,columnspan=2)
e4.grid(row=4,column=3,columnspan=2)
e5.grid(row=5,column=3,columnspan=2)
e6.grid(row=6,column=3,columnspan=2)
delete_entry=Entry(root,width=20)
delete_entry.grid(row=9,column=3)
#_____________________________________________________________
add_buttom=Button(root,text="add",command=add)
add_buttom.grid(row=7,column=2)
show_buttom=Button(root,text="show",command=query)
show_buttom.grid(row=7,column=3)
delete_buttom=Button(root,text="delete",command=delete,width=20)
delete_buttom.grid(row=10,column=3,columnspan=3)
update_buttom=Button(root,text="update",width=20,command=update)
update_buttom.grid(row=11,column=2,columnspan=3)
#________________________________________________________________________________







'''
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
'''

mainloop()