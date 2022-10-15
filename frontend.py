import tkinter
from tkinter import *
from backend import Database


database=Database('books.db')




################## Functions ###################
def get_selected_row(event):#note this is static..u have to put in the event parameter
    global selected_tuple
    index=list1.curselection()[0]#this takes the index of the tuple which is the id of the tuple in this case
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

    #print(selected_tuple)

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)



def add_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def update_command():
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    #print(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


def delete_command():
    database.delete(selected_tuple[0])





root=Tk()

l1=Label(root,text='Title')
l1.grid(row=0,column=0)

l2=Label(root,text='Year')
l2.grid(row=1,column=0)

l3=Label(root,text='Author')
l3.grid(row=0,column=2)

l4=Label(root,text='ISBN')
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(root,textvariable=title_text)
e1.grid(row=0,column=1)


year_text=StringVar()
e2=Entry(root,textvariable=year_text)
e2.grid(row=1,column=1)

author_text=StringVar()
e3=Entry(root,textvariable=author_text)
e3.grid(row=0,column=3)

isbn_text=StringVar()
e4=Entry(root,textvariable=isbn_text)
e4.grid(row=1,column=3)


list1=Listbox(root,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)


sb=Scrollbar(root)
sb.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)



list1.bind('<<ListboxSelect>>',get_selected_row)#this binds the selected row function to the listbox


b1=Button(root,text='view all',width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(root,text='search entry',width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(root,text='Add entry',width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(root,text='update entry',width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(root,text='delete entry',width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(root,text='close all',width=12,command=root.destroy)
b6.grid(row=7,column=3)


root.mainloop()


