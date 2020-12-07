from tkinter import *

window = Tk()
window.title("my first gui program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


#Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="button clicked")

button = Button(text="Click me",command=button_clicked)
button.pack()


#Entry
input = Entry(width=10)
input.pack()


window.mainloop()
