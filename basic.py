'''from tkinter import *
 
# Create an empty Tkinter window
window=Tk()
 
def from_kg():
    # Get user value from input box and multiply by 1000 to get kilograms
    gram=float(e2_value.get())*1000
 
    # Get user value from input box and multiply by 2.20462 to get pounds
    pound=float(e2_value.get())*2.20462
 
    # Get user value from input box and multiply by 35.274 to get ounces
    ounce=float(e2_value.get())*35.274
 
    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
    t1.insert(END,gram)  # Fill in the text box with the value of gram variable
    t2.delete("1.0", END)
    t2.insert(END,pound)
    t3.delete("1.0", END)
    t3.insert(END,ounce)
 
# Create a Label widget with "Kg" as label
e1=Label(window,text="Kg")
e1.grid(row=0,column=0) # The Label is placed in position 0, 0 in the window
 
e2_value=StringVar()  # Create a special StringVar object
e2=Entry(window,textvariable=e2_value)  # Create an Entry box for users to enter the value
e2.grid(row=0,column=1)
 
# Create a button widget
# The from_kg() function is called when the button is pushed
b1=Button(window,text="Convert",command=from_kg)
b1.grid(row=0,column=2)
 
# Create three empty text boxes, t1, t2, and t3
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)
 
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)
 
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)
 
# This makes sure to keep the main window open
window.mainloop()
'''

#import datetime
#print("date and time here :",datetime.datetime.now())
#
#
#a = "hello"
#w =  1222
#print(a,w)
#
#a = '10'
#b = 10
#
#print(a+a)
#print(b+b)
#print(type(a),type(b))
#
#student_grades = [9.1,8.8,7.5]
#print("the average is .",sum(student_grades)/len(student_grades))
##print(dir(str))
##print(dir(__builtins__))
#student_dict = {"urvi":11,"dhruv":20,"me":23}
#print(student_dict)
#print(student_dict.values())
#print(student_dict.keys())


#temp = (1,3,4,5)
#temp2 = [1,3,4,5]
#temp2 = temp2.append("eee")
#print(temp2)
##
# print(temp2.pop())
#print(temp)
"""def mean(mylist):
    if type(mylist) == dict:
        the_mean = sum(mylist.values())/len(mylist)
    else:
         the_mean = sum(mylist)/len(mylist)
    
    return the_mean

print(mean([1,2,3,4,5,32.324]))
mymean = mean({"urvi":11,"dhruv":20,"me":23})
print(mymean)

if 3 > 1:
    print("true")
else:
    print("false")"""

'''
def sentance_make(phase):
    ass = ("why", "how" ,"where","what")
    cap = phase.capitalize()
    if phase.startswith(ass):
        return "{} ?".format(cap)
    else:/end
        return "{} ".format(cap)

result = []

while True:
    us = input("enter somthing")
    if us == "/end":
        break
    else:
        result.append(sentance_make(us))

print(" .".join(result))'''

'''
myfile = open("fruits.txt")


c = myfile.read()
print(c)
print(c)
print(c)

myfile.close()
with open("fruits.txt") as myfile:
    content = myfile.read()
print(content)

with open("mr.txt","w") as myfile1:
    myfile1.write("hry\nhiii\nreagr")


with open("mr.txt","a+") as myfile1:
    myfile1.write("hry\nhiii\nreagr")
    myfile1.seek(2)
    myfile1.read()
'''
'''
import sqlite3

def create_table():
    Conn = sqlite3.Connection('db1.db')
    Cur = Conn.cursor()
    Cur.execute('CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)')
    
    Conn.commit()
    Conn.close()

def insert(item, quantity,price):
    Conn = sqlite3.Connection('db1.db')
    Cur = Conn.cursor()
    Cur.execute('INSERT INTO store VALUES(?,?,?)',(item,quantity,price))
    Conn.commit()
    Conn.close()



insert("water ",10,10.5)
insert("none ",40,0.5)
insert("par ",10,14.5)
insert("erer ",14,10.5)

def view():
    Conn = sqlite3.Connection('db1.db')
    Cur = Conn.cursor()
    Cur.execute('SELECT * FROM store')
    rows = Cur.fetchall()
    Conn.close()
    return rows
def delete(item):
    Conn = sqlite3.Connection('db1.db')
    Cur = Conn.cursor()
    Cur.execute('DELETE FROM store WHERE item=?',(item,))
    Conn.commit()
    Conn.close()
#delete('none ')
def update(quantity,price,item):
    Conn = sqlite3.Connection('db1.db')
    Cur = Conn.cursor()
    Cur.execute('UPDATE store SET quantity=?,price=? WHERE item=?',(quantity,price,item))
    Conn.commit()
    Conn.close()
#update(44,54,'water ')

print(view())
'''
'''

import psycopg2

def create_table():
    Conn = psycopg2.connect(" dbname='database1' user='postgres' password='post@123'  port='5432'")
    Cur = Conn.cursor()
    Cur.execute('CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)')
    
    Conn.commit()
    Conn.close()

def insert(item, quantity,price):
    Conn = psycopg2.connect(" dbname='database1' user='postgres' password='post@123'  port='5432'")
    Cur = Conn.cursor()
    Cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    Conn.commit()
    Conn.close()




create_table()
insert('orange',1,23)
'''

class Account():
    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())
    def withdrow(self,amt):
        self.balance = self.balance-amt
    def deposit(self,dipo):
        self.balance = self.balance+dipo

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))


class cheking(Account):
    '''hey there i also will with you'''
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def trasfer(self,amt):
        self.balance = self.balance-amt-self.fee




check = cheking('mr.txt',12)
check.trasfer(100)

print(check.balance)
check.commit()
print(check.__doc__)