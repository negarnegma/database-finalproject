from tkinter import *
def print():
    top=Tk()
    t = [(1,"2","3","4","5"),("sahar","sara","saeedeh","dd","ee"),("!@","%^","&*","@#","@$"),("A","B","C","D","E")]

    for x in range(4):
        for y in range(5):
            w = Text(top, width=15, height=2)
            w.grid(row=x,column=y)
            w.insert(END, t[x][y])

    top.state("zoomed")
    top.mainloop()
if __name__ == "__main__":
    print()