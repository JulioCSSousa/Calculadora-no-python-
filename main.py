from tkinter import *

#colours

black = '#050101'
blue = '#abbfd4'
green = '#1a9641'
grey = '#b0bfb4'
grey2 = '#b9c7c5'
green2 = '#1a9641'

window = Tk()
window.title('Calculator')
window.geometry('235x318')


#display
window.config(bg=black)

frame_window = Frame(window, width=235, height=50,bg=black)
frame_window.grid(row=0,column=0)

frame_body = Frame(window, width=235, height=268,bg=black)
frame_body.grid(row=1,column=0)

allValue = ''

#put value when you press bottoms
def putValue(enter):
    global allValue
    allValue = allValue + str(enter)

#show the operation on display
    valueText.set(allValue)


#calculing function
def calcular():
    global allValue
    result = eval(allValue)
    valueText.set(str(result))
#clean window
def clear():
    global allValue
    allValue = ''
    valueText.set('')

#labels
valueText = StringVar()

cal_label = Label(frame_window, textvariable=valueText, width=16, height=2, padx= 7, relief=FLAT, anchor= "e", justify=LEFT, font=('ivy 18'),bg=grey)
cal_label.place(x=0,y=0)


#bottoms
b1 = Button(frame_body, command=clear, text='c', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b1.place(x=0, y=0)
b2 = Button(frame_body, command=lambda: putValue('%'), text='%', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b2.place(x=59, y=0)
b3 = Button(frame_body, command=lambda: putValue('/'), text='/', width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg=green)
b3.place(x=178, y=0)

b4 = Button(frame_body, command=lambda: putValue('7'), text='7', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b4.place(x=0, y=52)
b5 = Button(frame_body, command=lambda: putValue('8'), text='8', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b5.place(x=59, y=52)
b6 = Button(frame_body, command=lambda: putValue('9'), text='9', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b6.place(x=118, y=52)
b7 = Button(frame_body, command=lambda: putValue('*'), text='*', width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg=green)
b7.place(x=177, y=52)

b8 = Button(frame_body, command=lambda: putValue('4'), text='4', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b8.place(x=0, y=104)
b9 = Button(frame_body, command=lambda: putValue('5'), text='5', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b9.place(x=59, y=104)
b10 = Button(frame_body, command=lambda: putValue('6'), text='6', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b10.place(x=118, y=104)
b11 = Button(frame_body, command=lambda: putValue('-'), text='-', width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg=green)
b11.place(x=177, y=104)

b12 = Button(frame_body, command=lambda: putValue('1'), text='1', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b12.place(x=0, y=156)
b13 = Button(frame_body, command=lambda: putValue('2'), text='2', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b13.place(x=59, y=156)
b14 = Button(frame_body, command=lambda: putValue('3'), text='3', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b14.place(x=118, y=156)
b15 = Button(frame_body, command=lambda: putValue('+'), text='+', width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE,bg=green)
b15.place(x=177, y=156)

b16 = Button(frame_body, command=lambda: putValue('0'), text='0', width=11, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b16.place(x=0, y=208)
b17 = Button(frame_body, command=lambda: putValue('.'), text='.', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b17.place(x=118, y=208)
b18 = Button(frame_body, command= calcular, text='=', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=green)
b18.place(x=177, y=208)
b19 = Button(frame_body, command=lambda: putValue('**'), text='^', width=5, height=2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE,bg=grey)
b19.place(x=118, y=0)

window.mainloop()


