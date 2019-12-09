from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from os import path
from tkinter import Menu

window = Tk()

window.geometry('350x200')
window.title("Welcome to my app")


#Label
lbl = Label(window, text="Hello", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

#TextBox
txt = Entry(window, width=10)#, state='disabled')
txt.grid(column=1, row=0)
txt.focus()

#Button
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)
btn = Button(window, text="Click Me", bg="white", fg="black", command=clicked)
btn.grid(column=2, row=0)


#ComboBox
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5)
combo.current(1)  # set the selected item
combo.grid(column=0, row=0)
z= combo.get()
print(z)


#CheckBox
chk_state = BooleanVar()
chk_state.set(True)  # set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=1)
chk_state = IntVar()
chk_state.set(0)  # uncheck
chk_state.set(1)  # check


#RadioButton
def clicked():
    print(selected.get())
selected = IntVar()
rad1 = Radiobutton(window, text='First', value=1, variable=selected)
rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window, text='Third', value=3, variable=selected)
btn = Button(window, text="Click Me", command=clicked)
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)
btn.grid(column=3, row=2)


#ScrollText
txt = scrolledtext.ScrolledText(window, width=10, height=2)
txt.grid(column=0, row=4)


#MessageBox
def clicked():
    messagebox.showinfo('Message title', 'Message content')
    messagebox.showwarning('Message title', 'Message content')
    messagebox.showerror('Message title', 'Message content')
    res = messagebox.askquestion('Message title', 'Message content')
    res = messagebox.askyesno('Message title', 'Message content')
    res = messagebox.askyesnocancel('Message title', 'Message content')
    res = messagebox.askokcancel('Message title', 'Message content')
    res = messagebox.askretrycancel('Message title', 'Message content')
btn = Button(window, text='Click here', command=clicked)
btn.grid(column=0, row=7)


#SpinBox
#spin = Spinbox(window, from_=0, to=100, width=5)
spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0, row=8)

var = IntVar()
var.set(36)
spin1 = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin1.grid(column=0, row=9)


#Progressbar
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=0, row=10)


#filedialog
file = filedialog.askopenfilename()
files = filedialog.askopenfilenames()  #you can ask for multiple files like this
file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
dir = filedialog.askdirectory()
file1 = filedialog.askopenfilename(initialdir= path.dirname(__file__))


#MenuBar
menu = Menu(window)
new_menu = Menu(menu, tearoff=0)
new_menu.add_command(label='New')
new_menu.add_separator()
new_menu.add_command(label='Edit', command=clicked)
menu.add_cascade(label='File', menu=new_menu)
window.config(menu=menu)

window.mainloop()