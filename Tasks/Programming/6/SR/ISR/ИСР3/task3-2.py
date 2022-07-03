from tkinter import *
from tkinter.ttk import *

class Solver:
    def __init__(self):
        self.root = Tk()
        
        padx, pady = 8, 8
        font = ('Tahoma', 12)
        
        Label(text='Решение СЛАУ методом Крамера', font='Tahoma 14') \
            .grid(row=0, column=0, columnspan=5, sticky=W, padx=padx, pady=pady)
        
        self.n1 = Entry(width=10, font=font)
        self.n1.grid(row=1, column=0, padx=padx, pady=pady)
        
        Label(text='+', font=font).grid(row=1, column=1, padx=padx, pady=pady)
        
        self.n2 = Entry(width=10, font=font)
        self.n2.grid(row=1, column=2, padx=padx, pady=pady)
        
        Label(text='=', font=font).grid(row=1, column=3, padx=padx, pady=pady)
        
        self.n3 = Entry(width=10, font=font)
        self.n3.grid(row=1, column=4, padx=padx, pady=pady)
        
        self.n4 = Entry(width=10, font=font)
        self.n4.grid(row=2, column=0, padx=padx, pady=pady)
        
        Label(text='+', font=font).grid(row=2, column=1, padx=padx, pady=pady)
        
        self.n5 = Entry(width=10, font=font)
        self.n5.grid(row=2, column=2, padx=padx, pady=pady)
        
        Label(text='=', font=font).grid(row=2, column=3, padx=padx, pady=pady)
        
        self.n6 = Entry(width=10, font=font)
        self.n6.grid(row=2, column=4, padx=padx, pady=pady)
        
        self.button = Button(text='Решить', width=20, command=self.solve)
        self.button.grid(row=3, column=0, columnspan=5, padx=padx, pady=pady)
        
        self.result = Label(font=('Tahoma', 14))
        self.result.grid(row=4, column=0, columnspan=5, padx=padx, pady=pady)
        
        self.root.mainloop()
        
        
    def solve(self):
        n1 = float(self.n1.get())
        n2 = float(self.n2.get())
        n3 = float(self.n3.get())
        n4 = float(self.n4.get())
        n5 = float(self.n5.get())
        n6 = float(self.n6.get())
        x1 = n3 * n5 - n2 * n6
        x2 = n1 * n5 - n2 * n4
        x = x1 / x2
        y1 = n1 * n6 - n3 * n4
        y2 = n1 * n5 - n2 * n4
        y = y1 / y2
        result = f'x = {x}, y = {y}'
        self.result.config(text=result)
        
        
if __name__ == '__main__':
    Solver()