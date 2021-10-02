# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:41:57 2021

@author: vedhs
"""
import Game
import UI

ui = UI.UI()
game = Game.Game()
ui.createGrid()

def tileClicked(x,y):
    res = game.select(x, y)
    ui.setStatus(res)
    if res=="Tile selected":
        ui.drawXO(x, y, "X")
    
ui.tileClicked = tileClicked

ui.mainloop()