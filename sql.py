import sqlite3

def create_table():
    Conn = sqlite3.Connection('lite.db')
    Cur = Conn.cursor()
    Cur.execute('CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)')
    
    Conn.commit()
    Conn.close()

def insert(item, quantity,price):
    Conn = sqlite3.Connection('lite.db')
    Cur = Conn.cursor()
    Cur.execute('INSERT INTO store VALUES(?,?,?)',(item,quantity,price))
    Conn.commit()
    Conn.close()



insert("water ",10,10.5)
insert("none ",40,0.5)
insert("par ",10,14.5)
insert("erer ",14,10.5)

def view():
    Conn = sqlite3.Connection('lite.db')
    Cur = Conn.cursor()
    Cur.execute('SELECT * FROM store')
    rows = Cur.fetchall()
    Conn.close()
    return rows

print(view())