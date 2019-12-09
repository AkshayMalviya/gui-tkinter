from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import pyodbc

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        lbl = Label(parent, text="Application for Twitter Streaming\n To view the tweets:", font=("Arial Bold Italic", 10))
        lbl.pack(side="top", fill="both")

        scrollbar = Scrollbar(parent)
        scrollbar.pack(side="right", fill="both")

        mylist = Listbox(parent, yscrollcommand=scrollbar.set)

        scrollbar.config(command=mylist.yview)

        def get_tweets():
            sql = "select top 5000 text from " + table_name + " where text like '%""%' order by id desc"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                mylist.insert(END, str(row)+'\n\n')

        btn = Button(parent, text="Click Me",  command = get_tweets)
        btn.pack(side="top")
        mylist.pack(side="bottom", fill=BOTH)

def db_connection():
    server = "XXXXX"
    database = "XXXXXX"
    username = "XXXXXX"
    password = "XXXXXXX"
    table_name = "XXXXXXX"
    connection = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';PORT=1443;DATABASE=' +
                                database + ';UID=' + username + ';PWD=' + password)
    cursor = connection.cursor()
    return table_name, cursor, connection


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Twitter Streaming')
    root.geometry('600x300')
    table_name, cursor, connection = db_connection()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    connection.close()