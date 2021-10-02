# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:41:57 2021

@author: vedhs
"""
import Game
import UI
import LogMoves


#Init
ui = UI.UI()
game = Game.Game()
logger = LogMoves.LogMoves()

#Creating grid on the canvas
ui.createGrid()

#On tile click
def tileClicked(x,y):
    res = game.select(x, y)
    ui.setStatus(res)
    if res=="Tile selected":
        ui.drawXO(x, y, "X")
        logger.log(game.isX, game.isO, x, y)
    
ui.tileClicked = tileClicked


#Mainloop on the end
ui.mainloop()