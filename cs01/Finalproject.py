from tkinter import*
def clear():
    global expression
    global lable_show_cal
    result="0"
    expression =""
    lable_show_cal.set(result)

def press(number):
    global expression
    global lable_show_cal
    expression=expression+number
    lable_show_cal.set(expression)
def equal():
    try:
        global expression
        global lable_show_cal
        result=str(eval(expression))
        lable_show_cal.set(result)
    except:
        result="error"
        expression=""
        lable_show_cal
    lable_show_cal.set(result)
Proud = Tk()
Proud.title("Proud Calculator")
Proud.option_add("font","consolas 30")
lable_show_cal=StringVar()
lable_show_cal.set(0)
expression=""
Label(Proud,textvariable=lable_show_cal).grid(row=0,column=0,columnspan=4)
Button(Proud,text="clear",command=clear).grid(row=1,column=0,columnspan=4,sticky="news")
Button(Proud,text="7",command=lambda:press("7")).grid(row=2,column=0)
Button(Proud,text="8",command=lambda:press("8")).grid(row=2,column=1)
Button(Proud,text="9 ",command=lambda:press("9")).grid(row=2,column=2)
Button(Proud,text="/",command=lambda:press("/")).grid(row=2,column=3)

Button(Proud,text="4",command=lambda:press("4")).grid(row=3,column=0)
Button(Proud,text="5",command=lambda:press("5")).grid(row=3,column=1)
Button(Proud,text="6",command=lambda:press("6")).grid(row=3,column=2)
Button(Proud,text="",command=lambda:press("")).grid(row=3,column=3)

Button(Proud,text="1",command=lambda:press("1")).grid(row=4,column=0)
Button(Proud,text="2",command=lambda:press("2")).grid(row=4,column=1)
Button(Proud,text="3",command=lambda:press("3")).grid(row=4,column=2)
Button(Proud,text="-",command=lambda:press("-")).grid(row=4,column=3)

Button(Proud,text="0",command=lambda:press("0")).grid(row=5,column=0)
Button(Proud,text=".",command=lambda:press(".")).grid(row=5,column=1,columnspan=2,sticky="news")
Button(Proud,text="+",command=lambda:press("+")).grid(row=5,column=3)

Button(Proud,text="=",command=equal).grid(row=6,column=0,columnspan=4,sticky="news")

Proud.mainloop()