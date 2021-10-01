# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:36:59 2021

@author: vedhs
"""
class Game:
    #For saving which player has which tile of the game
    isX = [[False]*3]*3
    isO = [[False]*3]*3
    
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
        
    