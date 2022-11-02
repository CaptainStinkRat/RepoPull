from tkinter import *
import tkinter.messagebox

class car:
    def __init__(self, color, powerState, moving):
        self.color = color
        self.powerState = powerState
        self.moving = moving

    def __str__(self):
        if self.powerState == "on":
            return f"The {self.color} {self} is running!"
        else:
            return f"The {self.color} car is off!"

    def __str__(self):
        if new_car.powerState == True: 
            return f"The {self.color} {choice} is running!"
        else:
            return("The car will remain off.")

def selection_box():
    options = [
    "Acura",
    "Audi",
    "BMW",
    "Ferrari"
    ]

    master = Tk()
    master.title("Car Selector")
    master.geometry( "150x150")
    variable = StringVar(master)
    variable.set(options[0]) #This will be the default value

    def selection(value):
        global choice
        choice = value
        master.destroy()


    w = OptionMenu(master, variable, *options, command=selection)
    w.pack()

#    def ok():
#        print ("The selected value is:" +variable.get())#
#
#    button = Button(master, text="OK", command=ok)
#    button.pack()

    mainloop()    

def color_pick():
    root = Tk()
    root.title("Car color")
    choices = ['Black','Blue','Red','Orange','White']
    variable = StringVar(root)
    variable.set(choices[0])
    def choice_box(a):
        global pick
        pick = a
        root.destroy()
    w =OptionMenu(root, variable, *choices, command=choice_box)
    w.pack()
    mainloop()

def confirmation():
    root=Tk()
    result=tkinter.messagebox.askquestion('Start car?','Do you want to start this car?')
    if result == 'yes':
        theLabel=Label(root,text="The car is starting up!")
        global car_start
        car_start = True
        theLabel.pack()
    elif result == 'no':
        car_start = False
        theLabel=Label(root,text="The car will stay off.")
        theLabel.pack()
    else:
        print("error")
    root.mainloop()


selection_box()
if choice == "Acura":
    color_pick()
    confirmation()
    new_car = car(pick,car_start,"no")
elif choice == "Audi":
    color_choice = color_pick()
    confirmation()
    new_car = car(pick,car_start,"no")
elif choice == "BMW":
    color_choice = color_pick()
    confirmation()
    new_car = car(pick,car_start,"no")
elif choice == "Ferrari":
    color_choice = color_pick()
    confirmation()
    new_car = car(pick,car_start,"no")
else:
    print("error")

print(new_car)

