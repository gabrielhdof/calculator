import Tkinter

window = Tkinter.Tk()
window.title("Calculadora")
window.geometry("210x280")
#window.wm_iconbitmap('icon.ico')
d_text = ""
display = Tkinter.Label(window, text=d_text, height = "3", width = "26", bg = "white", fg = "black", anchor="e")


a = ""
operand = ""
display.pack()

r = 0

def calculate(a,b,arg):
    if arg == "+":
        return str(a + b)
    elif arg == "-":
        return str(a-b)
    elif arg == 'x':
        return str(a*b)
    elif arg == '/':
        return str(a/b)

def callback(arg):
    global d_text
    global a
    global operand
    
    if str(arg) in "0123456789":
        d_text += str(arg)
        
    elif str(arg) == 'C':
        d_text == ""
        
    elif str(arg) == '<':
        d_text = d_text[:-1]
    else:
        if arg != '=':
            a = float(d_text)
            d_text = ""
            operand = arg
        else:
            b = float(d_text)
            d_text = calculate(a,b,operand)
      
    display.configure(text = d_text)

for j in range(0,3):
    for i in range(0,3):
        arg = 3*j + i
        button = Tkinter.Button(window, text=arg, command = lambda arg = arg: callback(arg))    
        button.place(x = 30 * i, y = 60 + 30*j)

button9 = Tkinter.Button(window, text = '9', command = lambda: callback(9))
button9.place(x = 90, y = 60)

button_equal = Tkinter.Button(window, text = "=", command = lambda: callback("="))
button_equal.place(x = 90, y = 90, height = 60)
other = ['+', '-', '/', 'x', '<']
for i in range(0,5):
    button = Tkinter.Button(window, text=other[i], command = lambda i = i: callback(other[i]))    
    button.place(x = 30 * i, y = 200)

window.mainloop()
