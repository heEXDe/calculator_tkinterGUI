from tkinter import *
import GUI


def ins_to_txtb(number_or_sign):
    GUI.txtBox.config(state=NORMAL)
    GUI.txtBox.insert(END, str(number_or_sign))
    GUI.txtBox.config(state=DISABLED)


def equal():
    try:
        equation = GUI.txtBox.get('1.0', 'end-1c')
        result = eval(equation)
        GUI.txtBox.config(state=NORMAL)
        GUI.txtBox.insert(END, "\n" + str(result))
        GUI.txtBox.config(state=DISABLED)
    except:
        print('error!')


def clean():
    GUI.txtBox.config(state=NORMAL)
    GUI.txtBox.delete('1.0', END)
    GUI.txtBox.config(state=DISABLED)

