from tkinter import *
import tkinter as tk

window = tk.Tk()
window.geometry('700x500')
window.title("Welcome to my app")

#Tab
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')

lbl1 = Label(tab1, text='label1', padx=5, pady=5)
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='label2', padx=5, pady=5)
lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')


#Image
logo = tk.PhotoImage(file="source.gif")
w1 = tk.Label(window, image=logo).pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(window,
              justify=tk.LEFT,
              padx = 10,
              text=explanation).pack(side="left")

window.mainloop()