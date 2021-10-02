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
            if  self.isX[x][y] or  self.isO[x][y]:
                return "Tile already selected"
            self.turn = not self.turn
            if not self.turn:                
                self.isX[x][y] = True            
                return "x"
            else:
                self.isO[x][y] = True            
                return "o"            
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
        
        #Check all filled / draw match
        if np.array_equal(np.bitwise_or(self.isX,self.isO),np.full((3,3),True)):
            return 'd'
        
        return '-'
    
    def playRandom(self):
        empty = []
        for i in range(3):
            for j in range(3):
                if not self.isX[i,j] and not self.isO[i,j]:
                    empty.append([i,j])
                    
        rand = random.randint(0,len(empty)-1)
        self.select(empty[rand][0],empty[rand][1])
        return empty[rand][0],empty[rand][1]
    
    def playPriority(self,priority):
        for i in range(9):            
            if self.select(priority[0,i], priority[1,i])=='o':
                return priority[0,i], priority[1,i]
        return -1,-1
            
        
        
    
        
    