import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def name():
 #  tkMessageBox.showinfo( "student Database", "name","age","class")
   str=raw_input("enter thr age:")
   tkMessageBox.showinfo( "student Database", str,)
   print str
  # tkMessageBox.showinfo( "student Database", "class")
"""
def age():
 #  tkMessageBox.showinfo( "student Database", "name","age","class")
   tkMessageBox.showinfo( "student Database", "age")
   #tkMessageBox.showinfo( "student Database", "class")"""
B = Tkinter.Button(top, text ="name", command = name)
#B1 = Tkinter.Button(top, text ="age", command = age)


B.pack()
#B1.pack()
top.mainloop()
