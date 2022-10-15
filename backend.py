import sqlite3

class Database:


    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS student_list (id INTEGER PRIMARY KEY,Firstname TEXT, \
        Lastname TEXT,Department INTEGER,stage INTEGER)')
        self.conn.commit()
       

  

    def insert(self,Firstname,Lastname,Department,stage):
        self.cur.execute('INSERT INTO student_list VALUES(NULL,?,?,?,?)',(Firstname,Lastname,Department,stage))
        self.conn.commit()
        




    def view(self):
        
        self.cur.execute('SELECT * FROM student_list')
        rows=self.cur.fetchall()
        
        return rows


    def search(self,Firstname='',Lastname='',Department='',stage=''):
        
        self.cur.execute('SELECT * FROM student_list WHERE Firstname=? OR Lastname=? OR Department=? OR stage=?',(Firstname,Lastname,Department, stage))
        rows=self.cur.fetchall()
        
        return rows


    def delete(self,id):
        
        self.cur.execute('DELETE FROM student_list WHERE id=?',(id,))
        self.conn.commit()
        


    def update(self,id,Firstname,Lastname,Department,stage):
        
        self.cur.execute('UPDATE student_list SET Firstname=?,Lastname=?,Department=?,stage=? WHERE id=?',(Firstname,Lastname,Department,stage,id))
        self.conn.commit()
        





