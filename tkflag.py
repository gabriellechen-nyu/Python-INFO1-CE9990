"""
tkflag.py

Gabrielle Chen
Homework 3
June 29, 2017
"""

import tkinter

rowHeight = 75
height = 10 * rowHeight
width = int(height * 16/10)

root = tkinter.Tk()
root.title("Flag of Sweden")
root.geometry(str(width) + "x" + str(height))

canvas = tkinter.Canvas(root, highlightthickness = 0, background = "#FFCE00")

y = 0
while y < height:
    x = 0
    while x < width:
        if (x < width * 5/16 or x > width * 7/16) and (y < 4 * rowHeight or y > 6 * rowHeight):
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = "#00559B")
        x += 1
    y += 1

canvas.pack(expand = tkinter.YES, fill = "both")

root.mainloop()
