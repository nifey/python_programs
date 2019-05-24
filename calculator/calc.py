from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.state = 0
        self.value = 0
        self.op = ''

        self.text_box = Entry(justify=RIGHT)
        self.text_box.grid(row=0, column=0, columnspan=4)
        self.text_box.insert(0, 0)

        self.b1 = Button(win, text='1',fg='black',bg='grey',command=lambda:self.number(1))
        self.b1.grid(row=1, column=0)

        self.b2 = Button(win, text='2',fg='black',bg='grey',command=lambda:self.number(2))
        self.b2.grid(row=1, column=1)

        self.b3 = Button(win, text='3',fg='black',bg='grey',command=lambda:self.number(3))
        self.b3.grid(row=1, column=2)

        self.plus = Button(win, text='+',fg='black',bg='grey',command=lambda:self.operator('+'))
        self.plus.grid(row=1, column=3)

        self.b4 = Button(win, text='4',fg='black',bg='grey',command=lambda:self.number(4))
        self.b4.grid(row=2, column=0)

        self.b5 = Button(win, text='5',fg='black',bg='grey',command=lambda:self.number(5))
        self.b5.grid(row=2, column=1)

        self.b6 = Button(win, text='6',fg='black',bg='grey',command=lambda:self.number(6))
        self.b6.grid(row=2, column=2)

        self.minus = Button(win, text='-',fg='black',bg='grey',command=lambda:self.operator('-'))
        self.minus.grid(row=2, column=3)

        self.b7 = Button(win, text='7',fg='black',bg='grey',command=lambda:self.number(7))
        self.b7.grid(row=3, column=0)

        self.b8 = Button(win, text='8',fg='black',bg='grey',command=lambda:self.number(8))
        self.b8.grid(row=3, column=1)

        self.b9 = Button(win, text='9',fg='black',bg='grey',command=lambda:self.number(9))
        self.b9.grid(row=3, column=2)

        self.multiply = Button(win, text='x',fg='black',bg='grey',command=lambda:self.operator('x'))
        self.multiply.grid(row=3, column=3)

        self.clear = Button(win, text='Clr',fg='black',bg='grey',command=self.clear)
        self.clear.grid(row=4, column=0)

        self.b0 = Button(win, text='0',fg='black',bg='grey',command=lambda:self.number(0))
        self.b0.grid(row=4, column=1)

        self.equal = Button(win, text='=',fg='black',bg='grey',command=self.calculate)
        self.equal.grid(row=4, column=2)

        self.division = Button(win, text='/',fg='black',bg='grey',command=lambda:self.operator('/'))
        self.division.grid(row=4, column=3)

    def clear(self):
        self.text_box.delete(0, END)
        self.text_box.insert(0, 0)
        self.state = 0
        self.value = 0
        self.op = ''

    def operator(self, op):
        if self.state == 0:
            self.value = self.get_value()
            self.op = op
            self.text_box.delete(0, END)
            self.text_box.insert(0, 0)
            self.state = 1
        elif self.state == 1:
            current_value = self.get_value()
            if self.op == '+':
                self.value = self.value + current_value
            elif self.op == '-':
                self.value = self.value - current_value
            elif self.op == 'x':
                self.value = self.value * current_value
            elif self.op == '/':
                self.value = self.value / current_value
            self.op = op
            self.text_box.delete(0, END)
            self.text_box.insert(0, 0)

    def calculate(self):
        if self.state == 1:
            current_value = self.get_value()
            if self.op == '+':
                self.value = self.value + current_value
            elif self.op == '-':
                self.value = self.value - current_value
            elif self.op == 'x':
                self.value = self.value * current_value
            elif self.op == '/':
                self.value = self.value / current_value
            self.op = ''
            self.text_box.delete(0, END)
            self.text_box.insert(0, self.value)
            self.state = 0

    def number(self, number):
        current_value = self.get_value()
        current_value = current_value * 10 + number
        self.text_box.delete(0, END)
        self.text_box.insert(0, current_value)

    def get_value(self):
        try:
            current_value = float(self.text_box.get())
        except:
            self.text_box.delete(0, END)
            current_value = 0
        return current_value

window = Tk()
my_window = MyWindow(window)
window.title('Calculator')
window.geometry('175x150')
window.mainloop()

