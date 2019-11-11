import sqlite3

#OOP making a class
class Database:

    #Connect Function
    #self parameter passed to fix error
    def __init__(self,db):
        self.conn = sqlite3.connect("books.db")
        self.cur= self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    #Add entry
    def insert(self,title,author,year,isbn):
        self.cur.execute('INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', (title,author,year,isbn))
        self.conn.commit()

    #View all
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#update(4,"The Moon","Kobe Bryant", 1390, 79897028)
#insert("The Sun", "John LEBRON", 1997, 9382048293)
#delete(3)
#print(view())
#print(search(author="John LEBRON"))
#
