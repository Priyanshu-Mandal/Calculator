from tkinter import*
root=Tk()
root.title("Scientific calculator")

e=Entry(root,width=58,borderwidth=7)
e.grid(row=0, column=0,columnspan=5)
e1=Entry(root,width=8,borderwidth=3)
e1.grid(row=1,column=4)

def clear():
    e1.delete(0,END)
    e.delete(0, END)
    
def numbe(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))
    
def dot():
    current=e.get()
    if str(current)=="":
        e.insert(0, "0.")
    else:
        e.delete(0, END)
        e.insert(0, str(current)+".")

def add():
    first_number = e.get()
    if first_number=="":
        e.insert(0, "+")
    else:
        global f_num
        global mat
        mat="addition"
        f_num=float(first_number)
        e.delete(0, END)
        e1.insert(0, "+")
        
def sub():
    first_number = e.get()
    if first_number=="":
        e.insert(0, "-")
    else:
        e1.delete(0,END)
        e1.insert(0, "-")
        global f_num
        global mat
        mat = "subtraction"
        f_num = float(first_number)
        e.delete(0, END)
        
def mul():
    e1.delete(0,END)
    e1.insert(0, "*")
    first_number = e.get()
    global f_num
    global mat
    mat = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def div():
    e1.delete(0,END)
    e1.insert(0, "/")
    first_number = e.get()
    global f_num
    global mat
    mat = "division"
    f_num = float(first_number)
    e.delete(0, END)
    
def power():
    e1.delete(0,END)
    e1.insert(0, "^")
    first_number = e.get()
    global f_num
    global mat
    mat = "power"
    f_num = float(first_number)
    e.delete(0, END)

def expo():
    e1.delete(0,END)
    e1.insert(0, "EXP")
    first_number = e.get()
    global f_num
    global mat
    mat = "exp"
    f_num = float(first_number)
    e.delete(0, END)
    
def ln():
    e1.delete(0,END)
    e1.insert(0, "Log")
    first_number = e.get()
    global f_num
    global mat
    mat = "log"
    f_num = float(first_number)
    e.delete(0, END)
    
def fact():
    e1.delete(0,END)
    e1.insert(0, "!")
    global mat
    mat = "fact"
    e.delete(0, END)
    
def epow():
    e1.delete(0,END)
    e1.insert(0, "e^")
    global mat
    mat = "epow"
    e.delete(0, END)

def sroot():
    e1.delete(0,END)
    e1.insert(0, "Sqr root")
    global mat
    mat = "root"
    e.delete(0, END)
    
def sine():
    e1.delete(0,END)
    e1.insert(0, "Sin")
    global mat
    mat = "sin"
    e.delete(0, END)
    
def cose():
    e1.delete(0,END)
    e1.insert(0, "Cos")
    global mat
    mat = "cos"
    e.delete(0, END)
    
def tane():
    e1.delete(0,END)
    e1.insert(0, "Tan")
    global mat
    mat = "tan"
    e.delete(0, END)
    
def cosece():
    e1.delete(0,END)
    e1.insert(0, "Cosec")
    global mat
    mat = "cosec"
    e.delete(0, END)
    
def sece():
    e1.delete(0,END)
    e1.insert(0, "Sec")
    global mat
    mat = "sec"
    e.delete(0, END)
    
def cote():
    e1.delete(0,END)
    e1.insert(0, "Cot")
    global mat
    mat = "cot"
    e.delete(0, END)
    
def mode():
    e1.delete(0,END)
    e1.insert(0, "|     |")
    global mat
    mat = "mod"
    e.delete(0, END)

def equal():
    import math
    second_number = eval(e.get())
    e.delete(0, END)
	
    if mat == "addition":
        e.insert(0, f_num + second_number)

    elif mat == "subtraction":
        e.insert(0, f_num - second_number)

    elif mat == "multiplication":
        e.insert(0, f_num * second_number)

    elif mat == "division":
        e.insert(0, f_num / second_number)
    
    elif mat=="power":
        e.insert(0, f_num**second_number)
        
    elif mat=="exp":
        e.insert(0, f_num*(10**second_number))
        
    elif mat=="epow":
        e.insert(0, 2.718**second_number)
        
    elif mat=="fact":
        a=second_number
        j=1
        for i in range(1,a+1):
            j=j*i
        e.insert(0, j)
        
    elif mat=="log":
        e.insert(0, math.log(f_num,second_number))
        
    elif mat=="root":
        e.insert(0, math.sqrt(second_number))
        
    elif mat=="sin":
        e.insert(0, math.sin(second_number*(math.pi/180)))
        
    elif mat=="cos":
        e.insert(0, math.cos(second_number*(math.pi/180)))
        
    elif mat=="tan":
        e.insert(0, math.tan(second_number*(math.pi/180)))
        
    elif mat=="cosec":
        e.insert(0, 1/(math.sin(second_number*(math.pi/180))))
        
    elif mat=="sec":
        e.insert(0, 1/(math.cos(second_number*(math.pi/180))))
        
    elif mat=="cot":
        e.insert(0, 1/(math.tan(second_number*(math.pi/180))))
        
    elif mat=="mod":
        a=second_number
        if a<0:
            a=-1*a
        e.insert(0, a)
        
    e1.delete(0,END)
    e1.insert(0, "Ans")
    

b1=Button(root,text="1",padx=25,pady=5,command=lambda: numbe(1)).grid(row=4,column=0,padx=5,pady=5)
b2=Button(root,text="2",padx=25,pady=5,command=lambda: numbe(2)).grid(row=4,column=1,padx=5,pady=5)
b3=Button(root,text="3",padx=25,pady=5,command=lambda: numbe(3)).grid(row=4,column=2,padx=5,pady=5)
b4=Button(root,text="4",padx=25,pady=5,command=lambda: numbe(4)).grid(row=3,column=0,padx=5,pady=5)
b5=Button(root,text="5",padx=25,pady=5,command=lambda: numbe(5)).grid(row=3,column=1,padx=5,pady=5)
b6=Button(root,text="6",padx=25,pady=5,command=lambda: numbe(6)).grid(row=3,column=2,padx=5,pady=5)
b7=Button(root,text="7",padx=25,pady=5,command=lambda: numbe(7)).grid(row=2,column=0,padx=5,pady=5)
b8=Button(root,text="8",padx=25,pady=5,command=lambda: numbe(8)).grid(row=2,column=1,padx=5,pady=5)
b9=Button(root,text="9",padx=25,pady=5,command=lambda: numbe(9)).grid(row=2,column=2,padx=5,pady=5)
b0=Button(root,text="0",padx=25,pady=5,command=lambda: numbe(0)).grid(row=5,column=0,padx=5,pady=5)
bdot=Button(root,text=".",padx=26,pady=5,command=dot).grid(row=5,column=1,padx=5,pady=5)

bplus=Button(root,text="+",padx=23,pady=26,command=add).grid(row=4,column=4,padx=3,pady=3,rowspan=2)
bsub=Button(root,text="-",padx=25,pady=26,command=sub).grid(row=6,column=4,padx=3,pady=3,rowspan=2)
bdiv=Button(root,text="/",padx=27,pady=5,command=div).grid(row=3,column=3,padx=3,pady=3)
bmul=Button(root,text="*",padx=27,pady=5,command=mul).grid(row=2,column=3,padx=3,pady=3)
bpow=Button(root,text="^",padx=23,pady=5,command=power).grid(row=2,column=4,padx=3,pady=3)
bclear=Button(root,text="Clear",padx=52,pady=5,command=clear).grid(row=8,column=0,padx=3,pady=3,columnspan=2)
bequal=Button(root,text="=",padx=62,pady=5,command=equal).grid(row=8,column=2,padx=3,pady=3,columnspan=2)
bexp=Button(root,text="EXP",padx=18,pady=5,command=expo).grid(row=5,column=2,padx=3,pady=3)
blog=Button(root,text="log",padx=21,pady=5,command=ln).grid(row=6,column=3,padx=3,pady=3)

bexppow=Button(root,text="e^",padx=23,pady=5,command=epow).grid(row=4,column=3,padx=3,pady=3)
bfact=Button(root,text="!",padx=28,pady=5,command=fact).grid(row=7,column=3,padx=3,pady=3)
broot=Button(root,text="sqr root",padx=9,pady=5,command=sroot).grid(row=5,column=3,padx=3,pady=3)
bcos=Button(root,text="cos",padx=19,pady=5,command=cose).grid(row=6,column=1,padx=3,pady=3)
btan=Button(root,text="tan",padx=19,pady=5,command=tane).grid(row=6,column=2,padx=3,pady=3)
bcosec=Button(root,text="cosec",padx=13,pady=5,command=cosece).grid(row=7,column=0,padx=3,pady=3)
bsec=Button(root,text="sec",padx=20,pady=5,command=sece).grid(row=7,column=1,padx=3,pady=3)
bcot=Button(root,text="cot",padx=19,pady=5,command=cote).grid(row=7,column=2,padx=3,pady=3)
bmod=Button(root,text="|     |",padx=17,pady=5,command=mode).grid(row=3,column=4,padx=3,pady=3)
bsin=Button(root,text="sin",padx=21,pady=5,command=sine).grid(row=6,column=0,padx=3,pady=3)
bexit=Button(root,text="Exit",padx=21,pady=5,command=root.destroy).grid(row=8,column=4,padx=3,pady=3)
root.mainloop()