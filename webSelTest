from tkinter import *
import webbrowser

def selection_box():
    options = [
    "amazon",
    "youtube",
    "google"
    ]

    master = Tk()
    master.title("Website Opener")
    master.geometry( "200x200")
    variable = StringVar(master)
    variable.set(options[0]) #This will be the default value

    def selection(value):
        global choice
        choice = value
        master.destroy()


    w = OptionMenu(master, variable, *options, command=selection)
    w.pack()

    def ok():
        print ("The selected value is:" +variable.get())

    button = Button(master, text="OK", command=ok)
    button.pack()

    mainloop()

selection_box()

if choice=="amazon":
    print("amazon")
    webbrowser.open('https://amazon.com')
elif choice=="youtube":
    print("youtube")
    webbrowser.open('https://youtube.com')
elif choice=="google":
    print('google')
    webbrowser.open('https://google.com')
else:
    print("Error")
