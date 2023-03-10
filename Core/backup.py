from tkinter import *
#colors
cor1 = '#1b283d' # Deep Blue - bg
cor2 = '#2b333b' # Blue Gray - numbers
cor3 = '#debc28' # Yellow - operations
cor4 = '#b02712' # Red - result
cor5 = '#2d2e33' # Gray - result label

window = Tk()
window.title('Calculadora')
window.geometry('445x650')
window.iconphoto(False, PhotoImage(file='Tkinterlearn/TKL/Core/icon.png'))
window.config(bg=cor1)
window.resizable(width=False, height=False)


# --Buttons Fuctions Num
def b1():
    label['text'] = label['text'] + '1'

def b2():
    label['text'] = label['text'] + '2'

def b3():
    label['text'] = label['text'] + '3'

def b4():
    label['text'] = label['text'] + '4'

def b5():
    label['text'] = label['text'] + '5'

def b6():
    label['text'] = label['text'] + '6'

def b7():
    label['text'] = label['text'] + '7'

def b8():
    label['text'] = label['text'] + '8'

def b9():
    label['text'] = label['text'] + '9'

def b0():
    label['text'] = label['text'] + '0'

# --Buttons Fuctions Op
def bcent():
    var_temp = label['text']
    sliced_temp = var_temp[-1:]
    oper = ['+', '-', 'x', '÷', '.', '**', '%']
    if sliced_temp in oper:
        label['text'] = var_temp[:-1] + '%'
    else:
        label['text'] = label['text'] + '%'

def balldel():
    label['text'] = ''

def bdel():
    var_temp = label['text']
    label['text'] = var_temp[:-1]

def bop1():
    var_temp = label['text']
    sliced_temp = var_temp[-1:]
    oper = ['+', '-', 'x', '÷', '.', '**', '%']
    if sliced_temp in oper:
        label['text'] = var_temp[:-1] + '+'
    else:
        label['text'] = label['text'] + '+'

def bop2():
    var_temp = label['text']
    sliced_temp = var_temp[-1:]
    oper = ['+', '-', 'x', '÷', '.', '**', '%']
    if sliced_temp in oper:
        label['text'] = var_temp[:-1] + '-'
    else:
        label['text'] = label['text'] + '-'

def bop3():
    var_temp = label['text']
    sliced_temp = var_temp[-1:]
    oper = ['+', '-', 'x', '÷', '.', '**', '%']
    if sliced_temp in oper:
        label['text'] = var_temp[:-1] + 'x'
    else:
        label['text'] = label['text'] + 'x'

def bop4():
    var_temp = label['text']
    sliced_temp = var_temp[-1:]
    oper = ['+', '-', 'x', '÷', '.', '**', '%']
    if sliced_temp in oper:
        label['text'] = var_temp[:-1] + '÷'
    else:
        label['text'] = label['text'] + '÷'

def bop5():
    var_temp = label['text']
    sliced_temp = var_temp[-1:]
    oper = ['+', '-', 'x', '÷', '.', '**', '%']
    if sliced_temp in oper:
        label['text'] = var_temp[:-1] + '.'
    else:
        label['text'] = label['text'] + '.'

def bop6():
    var_temp = label['text']
    sliced_temp = var_temp[-1:]
    oper = ['+', '-', 'x', '÷', '.', '**', '%']
    if sliced_temp in oper:
        label['text'] = var_temp[:-1] + '**'
    else:
        label['text'] = label['text'] + '**'

def bresult():
    var_temp = label['text']
    var = var_temp.replace('÷', '/')
    var = var.replace('x', '*')
    try:
        result = eval(var)
        label['text'] = str(result)
    except:
        label['text'] = 'ERROR'
    

# --Label Result
label = Label(window, height=5, text='', bg=cor5, fg='white', font=('Gravity 12 bold'))
label.grid(row=0, column=0, columnspan=4, sticky= 'WE', pady=0, padx=0)

# --Numbers
button1 = Button(window, command=b1, height=5, width=10, text='1', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button1.grid(row=2, column=0, pady=1, padx=1)

button2 = Button(window, command=b2, height=5, width=10, text='2', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button2.grid(row=2, column=1, pady=1, padx=1)

button3 = Button(window, command=b3, height=5, width=10, text='3', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button3.grid(row=2, column=2, pady=1, padx=1)

button4 = Button(window, command=b4, height=5, width=10, text='4', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button4.grid(row=3, column=0, pady=1, padx=1)

button5 = Button(window, command=b5, height=5, width=10, text='5', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button5.grid(row=3, column=1, pady=1, padx=1)

button6 = Button(window, command=b6, height=5, width=10, text='6', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button6.grid(row=3, column=2, pady=1, padx=1)

button7 = Button(window, command=b7, height=5, width=10, text='7', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button7.grid(row=4, column=0, pady=1, padx=1)

button8 = Button(window, command=b8, height=5, width=10, text='8', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button8.grid(row=4, column=1, pady=1, padx=1)

button9 = Button(window, command=b9, height=5, width=10, text='9', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button9.grid(row=4, column=2, pady=1, padx=1)

button0 = Button(window, command=b0, height=5, width=10, text='0', relief='flat', bg=cor2, fg='white', font=('Gravity 12 bold'))
button0.grid(row=5, column=1, pady=1, padx=1)

# --Operations
buttonporcent = Button(window, command=bcent, height=5, width=10, text='%', relief='flat', bg=cor3, fg='white', font=('Gravity 12 bold'))
buttonporcent.grid(row=1, column=0, pady=1, padx=1 )

buttonalldel = Button(window, command=balldel, height=5, width=10, text='CE', relief='flat', bg=cor3, fg='white', font=('Gravity 12 bold'))
buttonalldel.grid(row=1, column=1, pady=1, padx=1 )

buttonresult = Button(window, command=bresult, height=5, width=10, text='=', relief='flat', bg=cor4, fg='white', font=('Gravity 12 bold'))
buttonresult.grid(row=1, column=2, pady=1, padx=1 )

buttondelete = Button(window, command=bdel, height=5, width=10, text='⌫', relief='flat', bg=cor3, fg='white', font=('Gravity 12 bold'))
buttondelete.grid(row=1, column=3, pady=1, padx=1 )

buttonop1 = Button(window, command=bop1, height=5, width=10, text='+', relief='flat', bg=cor3, fg='white', font=('Gravity 12 bold'))
buttonop1.grid(row=2, column=3, pady=1, padx=1)

buttonop2 = Button(window, command=bop2, height=5, width=10, text='-', relief='flat', bg=cor3, fg='white', font=('Gravity 12 bold'))
buttonop2.grid(row=3, column=3, pady=1, padx=1)

buttonop3 = Button(window, command=bop3, height=5, width=10, text='X', relief='flat', bg=cor3, fg='white', font=('Gravity 12 bold'))
buttonop3.grid(row=4, column=3, pady=1, padx=1)

buttonop4 = Button(window,command=bop4, height=5, width=10, text='÷', relief='flat', bg=cor3, fg='white', font=('Gravity 12 bold'))
buttonop4.grid(row=5, column=3, pady=1, padx=1)

buttonop5 = Button(window, command=bop5, height=5, width=10, text='.', relief='flat', bg=cor3, fg='white', font=('Gravity 12 bold'))
buttonop5.grid(row=5, column=2, pady=1, padx=1)

buttonop6 = Button(window, command=bop6, height=5, width=10, text='^', relief='flat', bg=cor3, fg='white', font=('Gravity 12 bold'))
buttonop6.grid(row=5, column=0, pady=1, padx=1)

window.mainloop()

#Gerentes de Geometria - para organizar os widgets.
#place() - recebe x=, y= como coordenadas absolutas;
#grid() - recebe row=, column =, padx= e pady=, formato excel;
#pack() - recebe side=x (x é LEFT OU RIGHT), é difícil de usar.

#Estilos:
#'flat'
#'groove'
#'solid'
#'raised'
#'sunken'
#'ridge'