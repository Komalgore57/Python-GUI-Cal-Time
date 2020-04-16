from datetime import date
from tkinter import *

def check(dd,mm,yy):
    if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
        max1=31
    elif(mm==4 or mm==6 or mm==9 or mm==11):
        max1=30
    elif(yy%4==0 and yy%100!=0 or yy%400==0):
        max1=29
    else:
        max1=28
    if(mm<1 or mm>12):
        return True
    elif(dd<1 or dd>max1):
        return True
    else:
        return False  
def cal():
    x=[]
    y=[]
    k=1
    global s1,s2
    try:
        x.append(int(e1.get()))
        x.append(int(e3.get()))
        x.append(int(e5.get()))
        y.append(int(e2.get()))
        y.append(int(e4.get()))
        y.append(int(e6.get()))
    except:
        k=0
        s1.set("INVALID!!")
        s2.set("INVALID!!")  
    if k==1:
        if check(x[0],x[1],x[2]) and check(y[0],y[1],y[2]):
            s1.set("Birth Date Does Not Exist!!.")
            s2.set("Current Date Does Not Exist!!.")
        elif check(x[0],x[1],x[2]):
            s1.set("Birth Date Does Not Exist!!.")
            s2.set("Birth Date Does Not Exist!!.")
        elif check(y[0],y[1],y[2]):
            s1.set("Current Date Does Not Exist!!.")
            s2.set("Current Date Does Not Exist!!.")
        else:
            d0=date(int(x[2]),int(x[1]),int(x[0]))
            d1=date(int(y[2]),int(y[1]),int(y[0]))
            no_of_days=str(d1-d0)
            no_of_days=no_of_days.split()
            no_of_days=int(no_of_days[0])
            #print(no_of_days)
            if no_of_days<0:
                s1.set("NOT POSSSIBLE THAT YOU ARE NOT TAKEN BIRTH YET AND USING THIS!!!")
                s2.set("INVALID!!")
            else:
                t=abs(no_of_days)*24*8
                s1.set("You have been alive for "+str(no_of_days)+" days.")
                s2.set("You have slept "+str(t)+" hours.")   
def end():
    windows.destroy() 
windows = Tk()
windows.title("Sleep Calculator")
windows.geometry('800x800')
#windows.config(bg='#02fff7')
logo = PhotoImage(file="k1.gif",width=400,height=350)
w1 = Label(windows, image=logo).pack()
lbl = Label(windows, text="Sleep Calculator",font=("Arial Bold", 25), fg='#1abc9c')
lbl.place(x=200,y=350)
lb2 = Label(windows, text="Enter Your Birthdate",font=("Arial Bold", 15), fg='#1abc9c')
lb2.place(x=50,y=390)
lb3 = Label(windows, text="Enter Today's Date",font=("Arial Bold", 15), fg='#1abc9c')
lb3.place(x=450,y=390)
lb4 = Label(windows, text="Date",font=("Arial Bold", 15), fg='#1abc9c')
lb4.place(x=50,y=420)
e1 = Entry(windows,width=10)
e1.place(x=150,y=420)
lbl = Label(windows, text="Date",font=("Arial Bold", 15), fg='#1abc9c')
lbl.place(x=450,y=420)
e2 = Entry(windows,width=10)
e2.place(x=550,y=420)
lbl = Label(windows, text="Month",font=("Arial Bold", 15), fg='#1abc9c')
lbl.place(x=50,y=450)
e3 = Entry(windows,width=10)
e3.place(x=150,y=450)
lbl = Label(windows, text="Month",font=("Arial Bold", 15), fg='#1abc9c')
lbl.place(x=450,y=450)
e4 = Entry(windows,width=10)
e4.place(x=550,y=450)
lbl = Label(windows, text="Year",font=("Arial Bold", 15), fg='#1abc9c')
lbl.place(x=50,y=480)
e5 = Entry(windows,width=10)
e5.place(x=150,y=480)
lbl = Label(windows, text="Year",font=("Arial Bold", 15), fg='#1abc9c')
lbl.place(x=450,y=480)
e6 = Entry(windows,width=10)
e6.place(x=550,y=480)
b1=Button(windows,text='Calculate',font=("Arial Bold", 10), bg='#1abc9c', fg='#ecf0f1',command=cal)
b1.place(x=50,y=550)
b2=Button(windows,text='Exit',font=("Arial Bold", 10), bg='#1abc9c', fg='#ecf0f1',command=end)
b2.place(x=50,y=580)
s1=StringVar()
s2=StringVar()
e7 =Entry(windows,width=80,fg='#1abc9c', bg='#ffffff',textvariable=s1)
e7.place(x=150,y=550)
e8 = Entry(windows,width=80,fg='#1abc9c', bg='#ffffff',textvariable=s2)
e8.place(x=150,y=580)
windows.mainloop()


