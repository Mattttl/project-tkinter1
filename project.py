from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with widgets')
root.geometry("400x300")

labelle = Label(text="Hey There!",bg="#030B76",fg="white",height=1,width=300)
operation_labelle = Label(text="Numbers: ", bg="#3895D3")
n1_entry = Entry()
n2_entry = Entry()

text_box = Text(height=3)
def display():
    num1 = n1_entry.get()
    num2 = n2_entry.get()
    global message
    message = f"Welcome to the Application! The result is {int(num1)*int(num2)}" 
    text_box.insert(END,message)
btn = Button(text="Run", command=display, height=1,bg = "#030B76", fg='white')

labelle.pack()
operation_labelle.pack()
n1_entry.pack()
n2_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()