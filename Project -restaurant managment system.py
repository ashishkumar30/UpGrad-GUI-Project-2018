import tkinter
from tkinter import*
from time import gmtime, strftime
import time
import tkinter.messagebox

root=Tk()
root.geometry("1400x750")
root.attributes("-fullscreen", True)
root.title(' Restaurant Managment System Project by "Ashish Kumar" ')



                                                                                     #_________________programe Main code______________#


label=Label(root,text="Restaurant Managment System", fg="blue",
            font=("Blackletter & Lombardic Scripts",22))
label.pack()


                                                                                        #__________________Frame__________________#
#TIME

time1 = (  " " )
clock = Label(root,font=('times', 15))
clock.pack(padx=30,pady=30)

def tick():
    global time1
    time2 = time.strftime('%a, %d %b %Y      %H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)
tick()


#Alingment of frame
                                                                                  
bottomframe=Frame(root,)
bottomframe.pack(side=BOTTOM)

f1=Frame(root)
f1.pack(side=TOP ,padx=60,pady=60)

blank= Label(f1,text=" ").grid(row=9,columnspan=5)
i=( ' * 18 % GST is on Food \n" Goods and Services Tax (GST) is an indirect tax  levied in India on the supply of goods and services from July 1 2017 " ')
infogst= Label(f1,text=i , fg='steel blue')
infogst.grid(row=10,columnspan=5)




                                                                                       #__________________Main Buttons__________________#


#Function performed by Buttons


def price():      # operation performed by out button  ( pop up windwo)
    root = Tk()
    root.geometry("250x300")
    root.title("Price List")
    f1=Frame(root)
    f1.pack(side=TOP ,padx=80,pady=80)

    fries=Label(f1,text="Fries").grid(row=0,column=0)
    friesP=Label(f1,text="Rs 50").grid(row=0,column=1)
    lunch=Label(f1,text="Lunch").grid(row=1,column=0)
    lunchP=Label(f1,text="Rs 50").grid(row=1,column=1)
    burger=Label(f1,text="Burger").grid(row=2,column=0)
    burgerP=Label(f1,text="Rs 50").grid(row=2,column=1)
    piz=Label(f1,text="Fries").grid(row=3,column=0)
    pizP=Label(f1,text="Rs 50").grid(row=3,column=1)
    chzb=Label(f1,text="Lunch").grid(row=4,column=0)
    chzbP=Label(f1,text="Rs 50").grid(row=4,column=1)
    drink=Label(f1,text="Burger").grid(row=5,column=0)
    drinkpP=Label(f1,text="Rs 50").grid(row=5,column=1)
    root.mainloop() 

def drink():
    root = Tk()
    root.geometry("200x25")
    root.title("Drink")
    drin=Label(root,text="Soft drink Coca-cola , Rs.50",fg="red").grid(row=1,column=1)
    root.mainloop()
    
def total():         #operation performed by total button
    print("amount to be paid")
    

def out():            #operation performed by out button
    a=tkinter.messagebox.askokcancel(" Thankyou for visiting us !" ,"  Have a nice day  ")
    if(a):
        print("EXIT")
        quit()


def reset():          #operation performed by reset button
    O.set(0)
    F.set(0)
    L.set(0)
    B.set(0)
    P.set(0)
    Cb.set(0)
    D.set(0)
    C.set("No Value")
    G.set("No Value")
    A.set("No Value")
    S.set("No Value ")
    T.set(" No Value")

def total ():
    fries=float(F.get())
    lunch=float(L.get())
    burger=float(B.get())
    pizza=float(P.get())
    cheeseburger=float(Cb.get())
    drink=float(D.get())

    #mult with cost

    Rfries=fries*50
    Rlunch=lunch*50
    Rburger=burger*50
    Rpizza=pizza*50
    Rcheeseburger=cheeseburger*50
    Rdrink=drink*50

    #overall cost after GST and all 

    cost=(Rfries+Rlunch+Rburger+Rpizza+Rcheeseburger+Rdrink)
    C.set(cost)
    gst=((cost*18)/100)
    G.set(gst)
    aftergst= "Rs.",str ((gst)+(cost))
    A.set(aftergst)
    S.set(aftergst)
    T.set(aftergst)
    

# BUTTON'S

button1=Button(bottomframe,text ="PRICE",fg="red",bg="light green", activebackground="orange",height=2,width=7,command=price)
button1.pack(side=LEFT,padx=54,pady=90)

button2=Button(bottomframe,text ="TOTAL",fg="red",bg="yellow", command=total, activebackground="green",height=2,width=7)
button2.pack(side=LEFT,pady=54,padx=90)

button3=Button(bottomframe,text ="RESET",fg="red",bg="orange", activebackground="yellow",height=2,width=7,command=reset)
button3.pack(side=LEFT,padx=54,pady=90)

button4=Button(bottomframe,text ="EXIT",fg="red",bg="pink", command= out , activebackground="red",height=2,width=7)
button4.pack(side=LEFT,padx=54,pady=90)




                                                                                        #________________Entry Matrix___________________#


#storing of data 

O=StringVar()#for Order_number
F=StringVar()#for fries_Meal
L=StringVar()#for Lunch_meal
B=StringVar()#for Burger_Meal
P=StringVar()#for Pizza_Meal
Cb=StringVar()#for Cheese_Burger
D=StringVar() #for Drinks
C=StringVar() #for Cost
G=StringVar()#for GST
A=StringVar()#for After GST
S=StringVar()#for Subtotal
T=StringVar()#for Total

#Entity names and Entry field

Order_NumberL=Label(f1,text="Order Number").grid(row=0,column=0)
Order_NumberE=Entry(f1,textvariable=O).grid(row=0,column=1)

Fries_MealL=Label(f1,text="Fries Meal").grid(row=1,column=0)
Fries_MealE=Entry(f1,textvariable=F,fg="light green")
Fries_MealE.insert(END,0)
Fries_MealE.grid(row=1,column=1)

Lunch_MealL=Label(f1,text="Lunch Meal").grid(row=2,column=0)
Lunch_MealE=Entry(f1,textvariable=L,fg="light green")
Lunch_MealE.insert(END,0)
Lunch_MealE.grid(row=2,column=1)

Burger_MealL=Label(f1,text="Burger Meal").grid(row=3,column=0)
Burger_MealE=Entry(f1,textvariable=B,fg="light green")
Burger_MealE.insert(END,0)
Burger_MealE.grid(row=3,column=1)

PizzaaL=Label(f1,text="Pizza Meal").grid(row=4,column=0)
PizzaaE=Entry(f1,textvariable=P,fg="light green")
PizzaaE.insert(END,0)
PizzaaE.grid(row=4,column=1)

Cheese_BurgerL=Label(f1,text="Cheese Burger").grid(row=5,column=0)
Cheese_BurgerE=Entry(f1,textvariable=Cb,fg="light green")
Cheese_BurgerE.insert(END,0)
Cheese_BurgerE.grid(row=5,column=1)

DrinkL=Label(f1,text="Drink's").grid(row=0,column=2)
DrinkE=Entry(f1,textvariable=D,fg="light green")
DrinkE.insert(END,0)
DrinkE.grid(row=0,column=3)

CostL=Label(f1,text="Cost").grid(row=1,column=2)
CostE=Entry(f1,textvariable=C,fg="steel blue")
CostE.insert(END,0)
CostE.grid(row=1,column=3)

Service_ChargeL=Label(f1,text="GST").grid(row=2,column=2)
Service_ChargeE=Entry(f1,textvariable=G,fg="blue")
Service_ChargeE.insert(END,0)
Service_ChargeE.grid(row=2,column=3)

TaxL=Label(f1,text="After GST").grid(row=3,column=2)
TaxE=Entry(f1,textvariable=A,fg="red")
TaxE.insert(END,0)
TaxE.grid(row=3,column=3)

SubtotalL=Label(f1,text="Subtotal").grid(row=4,column=2)
SubtotalE=Entry(f1,textvariable=S,fg="red")
SubtotalE.insert(END,0)
SubtotalE.grid(row=4,column=3)

TotalL=Label(f1,text="Total",fg="red").grid(row=5,column=2)
TotalE=Entry(f1,textvariable=T,fg="red")
TotalE.insert(END,0)
TotalE.grid(row=5,column=3)




                                                                                #__________________Extra Buttons__________________#

#radiobutton & menu button's

r=Radiobutton(root,text= " Don't print Recipt" , fg='maroon',value=0)
r.pack(side=BOTTOM)
s=Radiobutton(root,text="Pint Recipt",value=1,fg="maroon")
s.pack(side=BOTTOM)


menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='Available Food',menu=filemenu)
filemenu.add_command(label='Food"s',command=price)
filemenu.add_command(label="Drink's",command=drink)

menu2=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='Rate List',menu=menu2)
menu2.add_command(label="Food's",command=price)
menu2.add_command(label="Drinks",command=drink)
#End of code
