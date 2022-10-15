import tkinter
from tkinter import *
from tkinter import ttk
import datetime
import time
from backend import Database
import tkinter.messagebox


database=Database('student_list.db')


root=Tk()






def validation():
    return len(Firstname_title.get())!=0 and \
    len(Lastname_title.get())!=0 and \
    len(Department_title.get())!=0 and \
    len(stage_title.get())!=0  




#.....................DATABASE VIEW............................
Tree=ttk.Treeview(height=10,column=['','','',''])
Tree.grid(row=9,column=0,columnspan=2)
Tree.heading('#0',text='ID')
Tree.column('#0',width=50)
Tree.heading('#1',text='Firstname')
Tree.column('#1',width=80)
Tree.heading('#2',text='Lastname')
Tree.column('#2',width=80)
Tree.heading('#3',text='Department')
Tree.column('#3',width=80)
Tree.heading('#4',text='stage')
Tree.column('#4',width=80)
#Tree.heading('#5',text='stage')
#Tree.column('#5',width=80)
#Tree.heading('#6',text='status')
#Tree.column('#6',width=40)






################## Functions ###################
'''def get_selected_row(event):#note this is static..u have to put in the event parameter
    global selected_tuple
    index=list1.curselection()[0]#this takes the index of the tuple which is the id of the tuple in this case
    selected_tuple=list1.get(index)
    Firstname.delete(0,END)
    Firstname.insert(END,selected_tuple[1])
    Lastname.delete(0,END)
    Lastname.insert(END,selected_tuple[2])
    Department.delete(0,END)
    Department.insert(END,selected_tuple[3])
    stage.delete(0,END)
    stage.insert(END,selected_tuple[4])'''



def delete_record():
    message['text']=' '
    try:
            Tree.item(Tree.selection())['values'][1]
    except:
            message['text']='please select a record to delete'
            return
    
    message['text']=' '
    number=Tree.item(Tree.selection())['text']
    database.delete(number)
    message['text']=f'Record {number} is deleted'
    viewing_records()



    
def viewing_records():
    records=Tree.get_children()
    for element in records:
        Tree.delete(element)
    for row in database.view():
        Tree.insert('',1000,text=row[0],values=row[1:])
        









#def add_record():
   # if validation():
         #   def run_query(self,query,parameters=()):
              #      query_results=cursor.execute(query,parameters)
                 #   conn.commit()
          #  return query_results


def add_command():
    if validation():
        database.insert(Firstname_title.get(),Lastname_title.get(),Department_title.get(),stage_title.get())
        message['text']='Record {} {} is added'.format(Firstname_title.get(),Lastname_title.get())
        Firstname.delete(0,END)
        Lastname.delete(0,END)
        Department.delete(0,END)
        stage.delete(0,END)
        viewing_records()
def add():

    ad=tkinter.messagebox.askquestion('Add Record','Do you want to add record?')
    if ad == 'yes':
        add_command()



        
#..................Logo and title......................

photo=PhotoImage(file='capture.png')
label=Label(image=photo)
label.grid(row=0,column=0)
label1=Label(font=('arial',20,'bold'),text='U.B.A Boarding Data',fg='green')
label1.grid(row=8,column=0)






#.................Menu bar...........................
chooser=Menu(tearoff=0)
itemone=Menu()

itemone.add_command(label='Add Record',command=add)
#itemone.add_command(label='Edit Record',command=update_command)
itemone.add_separator()
itemone.add_command(label='Delete Record',command=delete_record)

itemone.add_command(label='Exit',command=root.destroy)

chooser.add_cascade(label='File',menu=itemone)
chooser.add_cascade(label='Add',command=add)
#chooser.add_cascade(label='Edit',command=update_command)
chooser.add_cascade(label='Delete',command=delete_record)

chooser.add_cascade(label='Exit',command=root.destroy)

root.config(menu=chooser)

viewing_records()






#...................adding entries..........
frame=LabelFrame(root,text='Add new record',width=50)
frame.grid(row=0,column=1)

Label(frame,text='Firstname:').grid(column=0,row=0,sticky=W)
Firstname_title=StringVar()
Firstname=Entry(frame,textvariable=Firstname_title)
Firstname.grid(row=0,column=1)
Firstname.focus()


Label(frame,text='Lastname:').grid(column=0,row=2,sticky=W)
Lastname_title=StringVar()
Lastname=Entry(frame,textvariable=Lastname_title)
Lastname.grid(row=2,column=1)

Label(frame,text='Department:').grid(column=0,row=3,sticky=W)
Department_title=StringVar()
Department=Entry(frame,textvariable=Department_title)
Department.grid(row=3,column=1)

Label(frame,text='stage:').grid(column=0,row=4,sticky=W)
stage_title=StringVar()
stage=Entry(frame,textvariable=stage_title)
stage.grid(row=4,column=1)



ttk.Button(frame,text='Add Button',command=add).grid(row=7,column=1,sticky=W)


message=Label(frame,text='',fg='red')
message.grid(column=1,row=8)


#Label(frame,text='stage:').grid(column=0,row=5,sticky=W)
#stage=Entry(frame)
#stage.grid(row=5,column=1)

#Label(frame,text='status:').grid(column=0,row=6,sticky=W)
#status=Entry(frame)
#status.grid(row=6,column=1)



#ttk.Button(frame,text='Add Button',command=add).grid(row=7,column=1,sticky=W)










#.............Time and Date.................
def tick():
    today=time.asctime(time.localtime(time.time()))
    #d=datetime.datetime.now()
    #today='{:b %d,%Y}'.format(d)
    mytime=time.strftime('%I:%M:%S:%p')
    lblinfo.configure(text=(mytime+'\t'+today))
    lblinfo.after(200,tick)



lblinfo=Label(font=('arial',20,'bold'),fg='green')
lblinfo.grid(row=10,column=0,columnspan=2)
tick()




root.mainloop()