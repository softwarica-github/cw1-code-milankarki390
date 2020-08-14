import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
class Add_Book:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x400+0+0")
        self.root.title("Add Book")
        self.root.configure(background='cadet blue')
        self.l1=Label(self.root,text="Book ID")
        self.e1=Entry(self.root,width=30)
        self.l2=Label(self.root,text="Book Name")
        self.e2=Entry(self.root,width=30)
        self.l3=Label(self.root,text="Book Pub")
        self.e3=Entry(self.root,width=30)
        self.l4=Label(self.root,text="Book QTY")
        self.e4=Entry(self.root,width=30)
        self.b1=Button(self.root,text="Add Book",command=self.save)
        self.l1.place(x=20,y=30)
        self.e1.place(x=220,y=30)
        self.l2.place(x=20,y=80)
        self.e2.place(x=220,y=80)
        self.l3.place(x=20,y=130)
        self.e3.place(x=220,y=130)
        self.l4.place(x=20,y=180)
        self.e4.place(x=220,y=180)
        self.b1.place(x=20,y=230)
        self.root.mainloop()

    def E_handling(self):
        BookId = self.e1.get()
        BookName = self.e2.get()
        BookPub = self.e3.get()
        BookQty = self.e4.get()
        if BookId=='' or BookName=='' or BookPub=='' or BookQty=='':
            messagebox.showerror('Error', 'please fill all the box')
        else:
            try:
                BookId=int(BookId)
                BookQty=int(BookQty)
            except ValueError:
                messagebox.showerror('title','only digits are allowed in BookId and BookQty')    
      
    def save(self):
        self.E_handling()
        db=sqlite3.connect("lms.db")
        db.execute("create table if not exists books(id int primary key,name varchar(40),pub varchar(40),qty int)")
        db.execute("insert into books values(?,?,?,?)",(int(self.e1.get()),self.e2.get(),self.e3.get(),int(self.e4.get())))
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Saved")
        self.e1.delete(0,"end")
        self.e2.delete(0,"end")
        self.e3.delete(0,"end")
        self.e4.delete(0,"end")
class Delete_Book:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x400+0+0")
        self.root.title("Delete Book")
        self.root.configure(background='cadet blue')
        self.l1=Label(self.root,text="Book ID")
        self.e1=Entry(self.root,width=30)
        self.b1=Button(self.root,text="Delete Book",command=self.del_)
        self.l1.place(x=20,y=30)
        self.b1.place(x=20,y=230)
        self.e1.place(x=220,y=30)
        self.root.mainloop()  
    def del_(self):
        db=sqlite3.connect("lms.db")
        db.execute("DELETE FROM books WHERE id=?;",self.e1.get())
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Delete")
        self.e1.delete(0,"end")
class Add_Customer:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x400+0+0")
        self.root.title("Add customer")
        self.root.configure(background='cadet blue')
        self.l1=Label(self.root,text="Customer ID")
        self.e1=Entry(self.root,width=30)
        self.l2=Label(self.root,text="Customer Name")
        self.e2=Entry(self.root,width=30)
        self.l3=Label(self.root,text="Customer PNo")
        self.e3=Entry(self.root,width=30)
        self.b1=Button(self.root,text="Add Customer",command=self.save)
        self.b2=Button(self.root,text="Add Customer in text file",command=self.f_handling)
        self.l1.place(x=20,y=30)
        self.e1.place(x=220,y=30)
        self.l2.place(x=20,y=80)
        self.e2.place(x=220,y=80)
        self.l3.place(x=20,y=130)
        self.e3.place(x=220,y=130)
        self.b1.place(x=20,y=230)
        self.b2.place(x=200,y=230)
        self.root.mainloop()    
    def f_handling(self):
        txt = open("addcustomer.txt", "w")
        txt.write("  customer Id = " + str(self.e1.get()))
        txt.write("  customer Name = " + str(self.e2.get()))
        txt.write("  customer Pno = " + str(self.e3.get()))
        txt.close()
    def save(self):
        db=sqlite3.connect("lms.db")
        db.execute("create table if not exists customers(id int primary key,name varchar(40),pno varchar(30))")
        db.execute("insert into customers values(?,?,?)",(int(self.e1.get()),self.e2.get(),self.e3.get()))
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Saved")
        self.e1.delete(0,"end")
        self.e2.delete(0,"end")
        self.e3.delete(0,"end")
class Delete_customer:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x400+0+0")
        self.root.title("Delete Customer")
        self.root.configure(background='cadet blue')
        self.l1=Label(self.root,text="Customer ID")
        self.e1=Entry(self.root,width=30)
        self.b1=Button(self.root,text="delete customer",command=self.del_)
        self.l1.place(x=20,y=30)
        self.b1.place(x=20,y=230)
        self.e1.place(x=220,y=30)
        self.root.mainloop  
    def del_(self):
        db=sqlite3.connect("lms.db")
        db.execute("DELETE FROM customers WHERE id=?;",self.e1.get())
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Delete")
        self.e1.delete(0,"end")  
class Issue_Book:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x400+0+0")
        self.root.title("Issue Book")
        self.root.configure(background='cadet blue')
        self.l1=Label(self.root,text="Transaction ID")
        self.e1=Entry(self.root,width=30)
        self.l2=Label(self.root,text="Book Id")
        self.e2=Entry(self.root,width=30)
        self.l3=Label(self.root,text="Customer ID")
        self.e3=Entry(self.root,width=30)
        self.l4=Label(self.root,text="Date")
        self.e4=Entry(self.root,width=30)
        self.b1=Button(self.root,text="Issue",command=self.save)
        self.l1.place(x=20,y=30)
        self.e1.place(x=220,y=30)
        self.l2.place(x=20,y=80)
        self.e2.place(x=220,y=80)
        self.l3.place(x=20,y=130)
        self.e3.place(x=220,y=130)
        self.l4.place(x=20,y=180)
        self.e4.place(x=220,y=180)
        self.b1.place(x=20,y=230)
        self.root.mainloop()
    def checkbookid(self):
        db=sqlite3.connect("lms.db")
        db.execute("create table if not exists books(id int primary key,name varchar(40),pub varchar(40),qty int)")
        cursor=db.execute("select * from books where id=?",(int(self.e2.get()),))
        records=cursor.fetchall()
        if len(records)==0:
            db.close()
            return False
        else:
            print(records)
            print(type(records))
            
            
            s=int(records[0][3])
            db.close()
            if s>0:
                return True
            else:
                return False
    def checkcustomerid(self):
        db=sqlite3.connect("lms.db")
        db.execute("create table if not exists customers(id int primary key,name varchar(40),pno varchar(30))")
        cursor=db.execute("select * from customers where id=?",(int(self.e3.get()),))
        records=cursor.fetchall()
        if len(records)==0:
            db.close()
            return False
        else:
            db.close()
            return True
    def updateqty(self):
        db=sqlite3.connect("lms.db")
        db.execute("update books set qty=qty-1 where id=?",(int(self.e2.get()),))
        db.commit()
        db.close()
      
    def save(self):
        db=sqlite3.connect("lms.db")
        db.execute("create table if not exists trans(id int primary key,bid int,cid int,idate varchar(50),rdate varchar(50))")
        
        if self.checkbookid()==False:
            messagebox.showinfo("Error","Sorry invalid id or insufficient copies")
            return
        if self.checkcustomerid()==False:
            messagebox.showinfo("Error","Sorry invalid id")
            return
        self.updateqty()
        
        db.execute("insert into trans values(?,?,?,?,?)",(int(self.e1.get()),int(self.e2.get()),int(self.e3.get()),self.e4.get(),"NA"))
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Saved")
        self.e1.delete(0,"end")
        self.e2.delete(0,"end")
        self.e3.delete(0,"end")
        self.e4.delete(0,"end")
        

class Return_Book:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x400+0+0")
        self.root.title("Return Book")
        self.root.configure(background='cadet blue')
        self.l1=Label(self.root,text="Transaction ID")
        self.e1=Entry(self.root,width=30)
        self.l2=Label(self.root,text="Date")
        self.e2=Entry(self.root,width=30)
        self.b1=Button(self.root,text="Issue",command=self.save)
        self.l1.place(x=20,y=30)
        self.e1.place(x=220,y=30)
        self.l2.place(x=20,y=80)
        self.e2.place(x=220,y=80)
        self.b1.place(x=20,y=230)
        self.root.mainloop()
    def checktransid(self):
        db=sqlite3.connect("lms.db")
        cursor=db.execute("select * from trans where id=?",(int(self.e1.get()),))
        records=cursor.fetchall()
        if len(records)==0:
            db.close()
            return FALSE
        else:
            return int(records[0][1])
    def updateqty(self,id):
        db=sqlite3.connect("lms.db")
        db.execute("update books set qty=qty+1 where id=?",(id,))
        db.commit()
        db.close()
      
    def save(self):
        db=sqlite3.connect("lms.db")
        bid=self.checktransid()
        if bid==False:
            messagebox.showinfo("Error","Sorry invalid id")
            return
        self.updateqty(bid)
        db.execute("update trans set rdate=? where id=?",(self.e2.get(),int(self.e1.get())))
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Saved")
        



class Book_Lenders:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x400+0+0")
        self.root.configure(background='cadet blue')
        db=sqlite3.connect("lms.db")
        cursor=db.execute("select * from trans where rdate='NA'")
        records=cursor.fetchall()
        self.l=Listbox(self.root)
        for row in records:
            bname=self.getbookname(int(row[1]))
            c=self.getcustdetails(int(row[2]))
            cname=c[0]
            pno=c[1]
            self.l.insert("end",bname+"-"+cname+"--"+pno)
        db.close()
        self.l.place(x=30,y=60)
        self.root.mainloop()
        
    def getbookname(self,id):
        db=sqlite3.connect("lms.db")
        db.execute("create table if not exists books(id int primary key,name varchar(40),pub varchar(40),qty int)")
        cursor=db.execute("select * from books where id=?",(id,))
        records=cursor.fetchall()
        name=records[0][1]
        db.close()
        return name
    def getcustdetails(self,id):
        db=sqlite3.connect("lms.db")
        cursor=db.execute("select * from customers where id=?",(id,))
        records=cursor.fetchall()
        name=records[0][1]
        pno=records[0][2]
        db.close()
        return (name,pno)    

def addbook():
    a=Add_Book()
def addcustomer():
    a=Add_Customer()
def issuebook():
    o=Issue_Book()
def returnbook():
    r=Return_Book()
def booklenders():
    d=Book_Lenders
     
root=Tk()
root.title("Library Management System")
root.geometry("700x400+0+0")
bg = ImageTk.PhotoImage(file='lib1.jpg')
bg_image = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
b1=Button(text="Add Book",command=Add_Book)
b2=Button(text="Add customer",command=Add_Customer)
b3=Button(text="Issue Book",command=Issue_Book)
b4=Button(text="Return Book",command=Return_Book)
b5=Button(text="Book Lenders",command=Book_Lenders)
b6=Button(text="Delete Book",command=Delete_Book)
b7=Button(text="delete customer",command=Delete_customer)
b1.place(x=30,y=50)
b2.place(x=30,y=100)
b3.place(x=30,y=150)
b4.place(x=30,y=200)
b5.place(x=30,y=250)
b6.place(x=30,y=300)
b7.place(x=30,y=350)
root.mainloop()
