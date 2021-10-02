# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:36:59 2021

@author: vedhs
"""
import random
import numpy as np

class Game:
    #For saving which player has which tile of the game
    isX = np.full((3,3),False)
    isO = np.full((3,3),False)
    turn = False
    
    def __init__(self):
        self.turn = bool(random.randint(0, 1))
        
    def reset(self):
        self.isX = np.full((3,3),False)
        self.isO = np.full((3,3),False)
    
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
        if self.checkWin()=='-':
            if self.turn:
                if  self.isX[x][y] or  self.isO[x][y]:
                    return "Tile already selected"
                self.isX[x][y] = True            
                return "Tile selected"
            return "Not your turn"
        return "Game over"
    
    def checkWin(self):
        #Check horizontal and verticle
        for i in range(3):
            
            if np.array_equal(self.isX[i,:],np.full((3),True)):
                return 'x'
            if np.array_equal(self.isO[i,:],np.full((3),True)):
                return 'o'
            if np.array_equal(self.isX[:,i],np.full((3),True)):
                return 'x'
            if np.array_equal(self.isO[:,i],np.full((3),True)):
                return 'o'
            
        #Check diagonal
        if np.array_equal(self.isX.diagonal(),np.full((3),True)):
            return 'x'
        if np.array_equal(self.isO.diagonal(),np.full((3),True)):
            return 'o'
        if np.array_equal(np.fliplr(self.isX).diagonal(),np.full((3),True)):
            return 'x'
        if np.array_equal(np.fliplr(self.isO).diagonal(),np.full((3),True)):
            return 'x'
        
        return '-'
        
        
        
    
        
    