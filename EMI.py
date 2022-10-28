from tkinter import *
x=Tk()
x.geometry("500x500")
P1=Label(x,text="Enter the Principal Value: ").grid(row=0,column=0)
P2=Label(x,text="Enter the time Period: ").grid(row=1,column=0)
p=StringVar()
Entry(x).grid(row=0,column=1)
t=StringVar()
Entry(x).grid(row=1,column=1)
def SI(p,t):
    Principal=int(p.get())
    r=8
    time=int(t.get())
    SI=(Principal*r*time)/100
    print(SI)
P3=StringVar()
Simple_Interest=Label(x).grid(row=2,column=0)
P4=StringVar()
EMI=Label(x).grid(row=2,column=1)
bt=Button(x,text="show",commmand=SI(p,t))
bt.pack()
x.mainloop()


