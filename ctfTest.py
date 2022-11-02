import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
from tkinter import simpledialog
import webbrowser
import PyPDF2
from time import sleep
from tkinter import ttk

teams=range(100)

def port_scanner():
    master=tk.Tk()
    master.withdraw()
    ip_a = simpledialog.askstring(title="PDF Name", prompt="What is the host that will be scanned?")
    print(ip_a)


def button_command():
    popup=tk.Toplevel()
    tk.Label(popup, text="Ports are being scanned.").grid(row=0,column=0)

    progress=0
    progress_var=tk.DoubleVar()
    progress_bar=ttk.Progressbar(popup,variable=progress_var, maximum=100)
    progress_bar.grid(row=1, column=0)
    popup.pack_slaves()

    progress_step = float(100.0/len(teams))
    for team in teams:
        popup.update()
        sleep(5)
        progress += progress_step
        progress_var.set(progress)

    return 0

#root=tk.Tk()
#tk.Button(root, text="Launch", command=button_command).pack()

#root.mainloop()


def confirmation():
    root=Tk()
    result=tkinter.messagebox.askquestion('Execel','Do you want to export this to an excel?')
    if result == 'yes':
        theLabel=Label(root,text="Copying to excel.")
        theLabel.pack()
    else:
        root.destroy()
    root.mainloop()


def pick_box():
    root = Tk()

    def choice_box(a):
        global pick
        pick = a
        messagebox.showinfo("!","Loading "+pick+" tool")
        root.destroy()
    root.title("CTF")
    choices = ['Port Scanner','PDF Reader','Cipher']
    variable = StringVar(root)
    variable.set('Port Scanner')
    w =OptionMenu(root, variable, *choices, command=choice_box)
    w.pack()
    mainloop()

def pdf_reader():
    master=tk.Tk()
    master.withdraw()
    input = simpledialog.askstring(title="PDF Name", prompt="What PDF do you want to pull the Text from?")
    pdfFileObj = open(f'{input}','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    global pdf_message
    pdf_message=(pageObj.extractText())


pick_box()
if pick == 'Port Scanner':
    port_scanner()
    confirmation()
elif pick == 'PDF Reader':
    pdf_reader()
    confirmation()
elif pick == 'cipher':
    print('error')
