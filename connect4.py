# CS 111 FINAL PROJECT: CONNECT FOUR
# Orignal code from Breakout Lab by Aaron Bauer
# Modified and adapted for "Connect Four" Final Project by Issa Mohamed and Markus Gunadi 
import tkinter as tk
from tkinter import XView
from tkinter.constants import TRUE
from connect4_pgl import GWindow, GOval, GRect, GTimer
import random
from dataclasses import dataclass
player_moves = [] 
bot_moves = []
open_spots = []
box_dict = {}
num_box = 0
is_game_active = [True]
gw = GWindow(600, 700)
for row in range(6):
    for column in range(7):
        num_box += 1
        rect = GRect(column * 50 +100, row * 50 + 100, 50, 50)
        # rect.setColor('White')
        # rect.setFilled(False)
        box_dict[rect] = num_box
        gw.add(rect)
        open_spots.append(rect)


#Player Functions
def click_action(e):
    if is_game_active[0] == True:
        gobj = gw.getElementAt(e.getX(), e.getY())
        if gobj: 
            if gobj.getColor() != "#FF0000":
                gobj_x_value = gobj.getX()
                gobj_y_value = gobj.getY()
                lowest_spot = gobj
                for spot in open_spots:
                    current_spot_x_value = spot.getX()
                    current_spot_y_value = spot.getY()
                    if current_spot_x_value == lowest_spot.getX():
                        if current_spot_y_value > lowest_spot.getY():
                            lowest_spot = spot
                gobj = lowest_spot
                gobj.setFilled(True)
                gobj.setColor("#FF0000")
                player_moves.append(gobj)
                open_spots.remove(gobj)
                print("Turn", len(player_moves))
                print("player has", 21 - len(player_moves), "pieces left.")
                if check_connect4(player_moves) == True:
                    is_game_active[0]= False
                    endgame("Player", "")
                elif 21 - len(player_moves) < 0: 
                    is_game_active[0] = False
                    endgame("", "Bot")
                else:
                    bot_action(gobj)
                
            else:
                print("This Spot Has Already Been Selected. Please Choose Another Spot.")
        else:
            print("Click Inside The Board!")

#Computer Functions
def check_connect4(list_of_moves):
    if len(list_of_moves) < 4:
        return False
    else:
        for piece in list_of_moves:
            # 3 to the left 
            piece_y_val = piece.getY()
            piece_x_val = piece.getX()
            piece_color = piece.getColor()
            left_one_x_val = piece_x_val - 50
            left_two_x_val = piece_x_val - 100
            left_three_x_val = piece_x_val - 150
            left_one_obj = gw.getElementAt(left_one_x_val,piece_y_val)
            left_two_obj = gw.getElementAt(left_two_x_val,piece_y_val)
            left_three_obj = gw.getElementAt(left_three_x_val,piece_y_val)
            if (left_one_obj and left_two_obj and left_three_obj):
                if ( (left_one_obj.getColor() == piece_color) and (left_two_obj.getColor() == piece_color) and (left_three_obj.getColor() == piece_color)):
                            print("won left c4")
                            return True
             # 3 to the right
            right_one_x_val = piece_x_val + 50
            right_two_x_val = piece_x_val + 100
            right_three_x_val = piece_x_val + 150
            right_one_obj = gw.getElementAt(right_one_x_val,piece_y_val)
            right_two_obj = gw.getElementAt(right_two_x_val,piece_y_val)
            right_three_obj = gw.getElementAt(right_three_x_val,piece_y_val)
            if (right_one_obj and right_two_obj and right_three_obj):
                if ( (right_one_obj.getColor() == piece_color) and (right_two_obj.getColor() == piece_color) and (right_three_obj.getColor() == piece_color)):
                            print("won right c4")
                            return True
                 # 3 above
            above_one_y_val = piece_y_val - 50
            above_two_y_val = piece_y_val - 100
            above_three_y_val = piece_y_val - 150
            above_one_obj = gw.getElementAt(piece_x_val,above_one_y_val)
            above_two_obj = gw.getElementAt(piece_x_val,above_two_y_val)
            above_three_obj = gw.getElementAt(piece_x_val,above_three_y_val)
            if (above_one_obj and above_two_obj and above_three_obj):
                if ( (above_one_obj.getColor() == piece_color) and (above_two_obj.getColor() == piece_color) and (above_three_obj.getColor() == piece_color)):
                            print("won above c4")
                            return True
                 
            # 3 below
            below_one_y_val = piece_y_val + 50
            below_two_y_val = piece_y_val + 100
            below_three_y_val = piece_y_val + 150
            below_one_obj = gw.getElementAt(piece_x_val,below_one_y_val)
            below_two_obj = gw.getElementAt(piece_x_val,below_two_y_val)
            below_three_obj = gw.getElementAt(piece_x_val,below_three_y_val)
            if (below_one_obj and below_two_obj and below_three_obj):
                if ( (below_one_obj.getColor() == piece_color) and (below_two_obj.getColor() == piece_color) and (below_three_obj.getColor() == piece_color)):
                            print("won below c4")
                            return True
            # 3 right diagonal down
            right_diag_one_obj = gw.getElementAt(right_one_x_val, below_one_y_val)
            right_diag_two_obj = gw.getElementAt(right_two_x_val, below_two_y_val)
            right_diag_three_obj = gw.getElementAt(right_three_x_val, below_three_y_val)
            if (right_diag_one_obj and right_diag_two_obj and right_diag_three_obj):
                if ( (right_diag_one_obj.getColor() == piece_color) and (right_diag_two_obj.getColor() == piece_color) and (right_diag_three_obj.getColor() == piece_color)):
                            print("won right diag c4")
                            return True
             # 3 left diagonal down
            left_diag_one_obj = gw.getElementAt(left_one_x_val, below_one_y_val)
            left_diag_two_obj = gw.getElementAt(left_two_x_val, below_two_y_val)
            left_diag_three_obj = gw.getElementAt(left_three_x_val, below_three_y_val)
            if (left_diag_one_obj and left_diag_two_obj and left_diag_three_obj):
                if ( (left_diag_one_obj.getColor() == piece_color) and (left_diag_two_obj.getColor() == piece_color) and (left_diag_three_obj.getColor() == piece_color)):
                            print( "won left diag c4")
                            return True
    return False

def endgame(who_won, who_ran_out):
    print("Game Over.")
    if who_won == "Player":
        print('You Win!')
    elif who_won == "Bot":
        print( 'You Lose. Better Luck Next Time.')
    else:
        if who_ran_out == "Player":
            print("Player Has Run Out of Pieces.")
        elif who_ran_out == "Bot":
            print("Bot Has Run Out of Pieces.")


    
def bot_action(last_move):
    gobj = random.choice(open_spots)
    lowest_spot = gobj
    for spot in open_spots:
        current_spot_x_value = spot.getX()
        current_spot_y_value = spot.getY()
        if current_spot_x_value == lowest_spot.getX():
            if current_spot_y_value > lowest_spot.getY():
                lowest_spot = spot
    gobj = lowest_spot
    gobj.setFilled(True)
    gobj.setColor("#0000ff")
    bot_moves.append(gobj)
    open_spots.remove(gobj)
    print("bot has", 21 - len(bot_moves) , "pieces left.")
    if check_connect4(bot_moves) == True:
        is_game_active[0]= False
        endgame("Bot","")
    if 21 - len(bot_moves) < 0: 
        is_game_active[0] = False
        endgame("", "Player")

    
    return None
         
gw.addEventListener("click", click_action)