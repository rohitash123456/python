from Tkinter import *
import tkMessageBox
#import Tkinter
#right=Tkinter.Tk()

f=open("text.csv","w")
f.write("FIRST NAME ,LAST NAME,DOB,MOB_NUM\n")
master = Tk()
def callback():
	f.write(e.get())
    	print e.get()
#	f.write("\n")

def callback1():
	f.write(",")
	f.write(e1.get())
    	print e1.get()
#	f.write("\n")


def callback2():
	f.write(",")
	f.write(e2.get())
    	print e2.get()
#	f.write("\n")


def callback3():
	f.write(",")
	f.write(e3.get())
    	print e3.get()
	f.write("\n")

def okay():
	callback()
	callback1()
	callback2()
	callback3()
	print "data submited..."
def close_window():
	#oot.destroy()	
        sys.exit()

#b = Button(master, text="First name", width=10, command=callback)
b = Label(master, text="First name", width=12)#, command=callback)
b.pack()
e = Entry(master)
e.pack()
e.focus_set()

b1 = Label(master, text="Last name", width=12)#, command=callback1)
b1.pack()
e1 = Entry(master)
b1.pack()
e1.pack()
e1.focus_set()

b2 = Label(master, text="DOB dd/mm/yy ", width=12)#, command=callback2)
b2.pack()
e2 = Entry(master)
#b1.pack(side=LEFT)
e2.pack()
e2.focus_set()


b3 = Label(master, text="Moible no.", width=12)#, command=callback3)
b3.pack()
e3 = Entry(master)
e3.pack()
e3.focus_set()

ok=Button(master,text="submit",width=10,command=okay)
ok.pack()
ok.focus_set()


exit=Button(master,text="exit",width=10,command=close_window)
exit.pack()
#exit.focus_set()
mainloop()
"""Entry(master )
#e.pack()

e1 = Entry(master )
#e1.pack()
e2 = Entry(master, width=50)
#e2.pack()
e3 = Entry(master, width=10)
#e3.pack()"""
f.close()


