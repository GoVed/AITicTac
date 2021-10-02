# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:19:37 2021

@author: vedhs
"""
import tkinter as tk

class UI:
    #init Variables
    win = None
    w = None
    h = None
    canvas = None
    trainBtn = None
    easyBtn = None
    hardBtn = None
    status = None
    
    #Constructor
    def __init__(self,w=500,h=500,bg="black"):
        #Setting up the window
        self.win = tk.Tk()
        self.win.title('AI Tic Tac Toe')
        
        
        #Setting the width and the height of the canvas
        self.w = w
        self.h = h
        
        #Setting up the canvas
        self.canvas = tk.Canvas(self.win,bg=bg,width = self.w,height = self.h)
        self.canvas.bind("<Button-1>", self.canvasClick)
        self.canvas.grid(row = 0, column = 0,columnspan = 2)
        
        #Setting the status text
        self.status = tk.Label(self.win,text="Select the mode to play/train")
        self.status.grid(row = 1, column = 0,columnspan = 2)
        
        #Setting up the buttons
        self.trainBtn = tk.Button(self.win,text = "Train model")
        self.easyBtn = tk.Button(self.win,text = "Play easy")
        self.hardBtn = tk.Button(self.win,text = "Play hard")
        self.trainBtn.grid(row = 2, column = 0,columnspan = 2)
        self.easyBtn.grid(row = 3, column = 0)
        self.hardBtn.grid(row = 3, column = 1)
    
    #Create tic tac toe grid on the canvas (4 lines)
    def createGrid(self):
        self.canvas.create_line(self.w/3,0,self.w/3,self.h,fill="white")
        self.canvas.create_line(2*self.w/3,0,2*self.w/3,self.h,fill="white")
        self.canvas.create_line(0,self.h/3,self.w,self.h/3,fill="white")
        self.canvas.create_line(0,2*self.h/3,self.w,2*self.h/3,fill="white")
        
    #Function to draw Xs and Os
    def drawXO(self,x,y,sym):
        x*=self.w/3
        y*=self.h/3
        x+=self.w/6
        y+=self.h/6        
        self.canvas.create_text(x,y,fill="white",font = "Times 40  bold",text = sym )
    
    #Handles canvas clicks
    def canvasClick(self,event):
        self.status.config(text="Clicked at "+ str(int(event.y/self.h*3)) +","+str(int(event.x/self.w*3)))
        self.tileClicked(int(event.y/self.h*3),int(event.x/self.w*3))
        
       
    def setStatus(self,txt):
        self.status.config(text=txt)
        
    #To be overriden in Run file
    def tileClicked(x,y):
        pass
    
    #Run the mainloop
    def mainloop(self):
        self.win.mainloop()
             

