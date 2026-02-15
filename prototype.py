# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 13:40:54 2026

@author: laisz
"""

from tkinter import Tk, Frame, Button, Entry, END

root = Tk()
root.title("My Calculator")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

## display
expression = Entry(root, font=("Arial", 20), justify="right")
expression.grid(row=0, 
                column=0,
                sticky="news")

def input_0(event=None):
    expression.insert(END, "0")
    
def input_1(event=None):
    expression.insert(END, "1")
    
def input_2(event=None):
    expression.insert(END, "2")
    
def input_3(event=None):
    expression.insert(END, "3")
    
def input_4(event=None):
    expression.insert(END, "4")
    
def input_5(event=None):
    expression.insert(END, "5")
    
def input_6(event=None):
    expression.insert(END, "6")
    
def input_7(event=None):
    expression.insert(END, "7")
    
def input_8(event=None):
    expression.insert(END, "8")
    
def input_9(event=None):
    expression.insert(END, "9")
    
def left_parentheses(event=None):
    expression.insert(END, "(")

def right_parentheses(event=None):
    expression.insert(END, ")")
    
def add(event=None):
    expression.insert(END, "+")
    
def subtract(event=None):
    expression.insert(END, "-")
    
def multiply(event=None):
    expression.insert(END, "*")
    
def divide(event=None):
    expression.insert(END, "/")
    
def equal(event=None):
    text = expression.get()
    
    if text:
        expression.delete(0, END)
        expression.insert(0, eval(text))
        
def clear(event=None):
    expression.delete(0, END)
    

expression.bind("<Return>", equal)

## Input
keypad = Frame(root)
keypad.grid(row=1,
            column=0,
            sticky="news")
for i in range(5):
    keypad.rowconfigure(i, weight=1)
for i in range(4):
    keypad.columnconfigure(i, weight=1)

no_0 = Button(keypad, text="0", command=input_0)
no_1 = Button(keypad, text="1", command=input_1)
no_2 = Button(keypad, text="2", command=input_2)
no_3 = Button(keypad, text="3", command=input_3)
no_4 = Button(keypad, text="4", command=input_4)
no_5 = Button(keypad, text="5", command=input_5)
no_6 = Button(keypad, text="6", command=input_6)
no_7 = Button(keypad, text="7", command=input_7)
no_8 = Button(keypad, text="8", command=input_8)
no_9 = Button(keypad, text="9", command=input_9)
add_btn = Button(keypad, text="+", command=add)
sub_btn = Button(keypad, text="-", command=subtract)
mul_btn = Button(keypad, text="*", command=multiply)
div_btn = Button(keypad, text="/", command=divide)
eq_btn = Button(keypad, text="=", command=equal)
left_btn = Button(keypad, text="(", command=left_parentheses)
right_btn = Button(keypad, text=")", command=right_parentheses)
clear_btn = Button(keypad, text="C", command=clear)

no_0.grid(row=4, column=1, sticky="news")
no_1.grid(row=3, column=0, sticky="news")
no_2.grid(row=3, column=1, sticky="news")
no_3.grid(row=3, column=2, sticky="news")
no_4.grid(row=2, column=0, sticky="news")
no_5.grid(row=2, column=1, sticky="news")
no_6.grid(row=2, column=2, sticky="news")
no_7.grid(row=1, column=0, sticky="news")
no_8.grid(row=1, column=1, sticky="news")
no_9.grid(row=1, column=2, sticky="news")
add_btn.grid(row=3, column=3, sticky="news")
sub_btn.grid(row=2, column=3, sticky="news")
mul_btn.grid(row=1, column=3, sticky="news")
div_btn.grid(row=0, column=3, sticky="news")
eq_btn.grid(row=4, column=3, sticky="news")
left_btn.grid(row=0, column=0, sticky="news")
right_btn.grid(row=0, column=1, sticky="news")
clear_btn.grid(row=0, column=2, sticky="news")


root.mainloop()