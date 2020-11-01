from tkinter import *
import GUI
from math import log as log
from math import sqrt as sqrt


def inp_to_txtb(number_or_sign):
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
        GUI.txtBox.config(state=NORMAL)
        GUI.txtBox.insert(END, "\n" + "error")
        GUI.txtBox.config(state=DISABLED)


def clean():
    GUI.txtBox.config(state=NORMAL)
    GUI.txtBox.delete('1.0', END)
    GUI.txtBox.config(state=DISABLED)


def backspace():
    try:
        s_str = GUI.txtBox.get('1.0', 'end-1c')
        res_str = ''.join([s_str[i] for i in range(len(s_str)) if i != len(s_str) - 1])
        GUI.txtBox.config(state=NORMAL)
        GUI.txtBox.delete('1.0', END)
        GUI.txtBox.insert(END, str(res_str))
        GUI.txtBox.config(state=DISABLED)
    except:
        print('error!')

