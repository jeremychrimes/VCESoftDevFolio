"""
Jeremy Chrimes 2018
Date Created: 2018/05/24
Date Modified: 2018/05/24
Version 0.1

This program is the class that stores client information
"""

import tkinter


class MainApplication(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MainApplication, self).__init__()
        self.parent = parent
        numberButtons = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.buttons = list()
        for i in range(len(numberButtons)):
            for j in range(len(numberButtons[i])):
                self.buttons.append(tkinter.Button(self, text=numberButtons[i][j]))
                pos = int(len(self.buttons) - 1)
                self.buttons[pos].grid(row=i, column=j)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("XOSales - Add Client")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
