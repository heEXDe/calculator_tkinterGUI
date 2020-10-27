from tkinter import *
import GUI


def ins_to_txtb(number_or_sign):
    GUI.txtBox.config(state=NORMAL)
    GUI.txtBox.insert(END, str(number_or_sign))
    GUI.txtBox.config(state=DISABLED)


def push_operation(sign):
    GUI.txtBox.get('1.0', 'end-1c')

