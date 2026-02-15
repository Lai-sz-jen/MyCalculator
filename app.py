# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 19:16:16 2026

@author: laisz
"""
import tkinter as tk

class Controller:
    def __init__(self):
        self._model = CalculatorModel()
        self._view = CalculatorUI(self.process)
        self._view.run()
        
    def process(self) -> None:
        result = self._model.calculate(self._view.fetch())
        self._view.display(result)
        
class CalculatorModel:
    def calculate(self, expr: str) -> str:
        ans = eval(expr)
        return ans
    
class CalculatorUI:
    def __init__(self, callback):
        root = tk.Tk()
        root.title("MyCalculator")
        
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=2)
        root.columnconfigure(0, weight=1)
        
        expression = tk.Entry(root)
        expression_repr = tk.Label(root, font=("Arial", 20), anchor="se")
        expression_repr.grid(row=0, column=0, sticky="news")
        self._expression = expression
        self._display = expression_repr
        
        keypad = tk.Frame(root)
        keypad.grid(row=1, column=0, sticky="news")
        buttons: dict[str, tk.Button] = {}
        
        for i in range(5):
            keypad.rowconfigure(i, weight=1)
        for i in range(4):
            keypad.columnconfigure(i, weight=1)
            
        button_icon = (("(", ")", "C", "/"),
                       ("7", "8", "9", "*"),
                       ("4", "5", "6", "-"),
                       ("1", "2", "3", "+"),
                       (".", "0", "\b", "="))
        
        for x, row in enumerate(button_icon):
            for y, icon in enumerate(row):
                button = tk.Button(keypad, 
                                   text=icon, 
                                   command=lambda key=icon: self.press(key))
                button.grid(row=x, column=y, sticky="news")
                buttons[icon] = button
        
        buttons["C"].configure(command=self.clear)
        buttons["*"].configure(text="\u00D7")
        buttons["/"].configure(text="\u00F7")
        buttons["\b"].configure(text="\u232B", command=self.backspace)
        buttons["="].configure(command=callback)
        
        self._root = root
       
    def _repr(self) -> None:
        display_txt = (self._expression.get()
                       .replace("*", "\u00D7")
                       .replace("/", "\u00F7"))
        self._display.config(text=display_txt) 
       
    def run(self):
        self._root.mainloop()
        
    def press(self, char: str) -> None:
        self._expression.insert(tk.END, char)
        self._repr()
        
    def clear(self) -> None:
        self._expression.delete(0, tk.END)
        self._repr()
        
    def backspace(self) -> None:
        last = len(self._expression.get()) - 1
        self._expression.delete(last)
        self._repr()
    
    def fetch(self) -> str:
        return self._expression.get()
    
    def display(self, result) -> None:
        self.clear()
        self._expression.insert(0, f"{result:g}")
        self._repr()
        
        
if __name__ == "__main__":
    app = Controller()