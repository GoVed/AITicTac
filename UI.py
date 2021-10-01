# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:19:37 2021

@author: vedhs
"""
import tkinter as tk

win = tk.Tk()
win.title('AI Tic Tac Toe')
win.geometry('700x700')

w=500
h=500
canvas = tk.Canvas(win,bg="black",width = w,height = h)
canvas.pack()

def createGrid(canvas):
    canvas.create_line(w/3,0,w/3,h,fill="white")
    canvas.create_line(2*w/3,0,2*w/3,h,fill="white")
    canvas.create_line(0,h/3,w,h/3,fill="white")
    canvas.create_line(0,2*h/3,w,2*h/3,fill="white")
createGrid(canvas)

win.mainloop()