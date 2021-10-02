# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:36:59 2021

@author: vedhs
"""
import random

class Game:
    #For saving which player has which tile of the game
    isX = [[False]*3 for _ in range(3)]
    isO = [[False]*3 for _ in range(3)]
    turn = False
    
    def __init__(self):
        self.turn = bool(random.randint(0, 1))
    
    def getCurrent(self,style='XO'):
        #Different styles for returning status
        styles={'XO':{'x':'X','o':'O'},'+-':{'x':'+','o':'-'}}
        
        #Empty status var to fill in later
        out=[['']*3]*3
        
        #Looping through all the position in tic tac toe
        for i in range(3):
            for j in range(3):
                if self.isX[i][j]:
                    out[i][j]=styles[style]['x']
                if self.isO[i][j]:
                    out[i][j]=styles[style]['o']
                    
        return out
    
    def select(self,x,y):
        if self.turn:
            if  self.isX[x][y] or  self.isO[x][y]:
                return "Tile already selected"
            self.isX[x][y] = True            
            return "Tile selected"
        return "Not your turn"
        
    