from Tkinter import *
f=open("abc.txt","w+")
top = Tk()
L1 = Label(top, text="User Name")
print Label
L1.pack( side = LEFT)
#E1 = Entry(top, bd =5)

E2=Entry(top,textvariable=input(""),bd=10)
#f.write(E1)
E2.pack(side = RIGHT)
top.mainloop()
f.close()
