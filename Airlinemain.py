from tkinter import *
from tkinter import simpledialog

root= Tk()
root.title('Airline Reservation Systemn')
lbl = Label(root, text="Welcome To YEBOYO AIRLINES",fg='yellow',bg='blue',font=('roman',70,'bold')).pack()
root.iconbitmap('c:/users/ok/welcome.py')



def open():
	top = Toplevel()
	top.title('Pick A Seat')
	top.iconbitmap('c:/users/ok/welcome.py')
	

btn = Button(root, text= "Pick A Seat", command=open).pack()



mainloop()
