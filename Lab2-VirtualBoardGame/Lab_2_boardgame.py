#!/usr/bin/env python
# coding: utf-8

# In[43]:


import random as rn
import numpy as np 

specialSpaces = np.arange(1, 99, 3)

num_players = input('How many players?')

num_players = int(num_players)

player_positions = [0] * num_players

someone_won = False

while someone_won == False:
    for player in range(0, num_players):
        print('Turn of player ' + str(player + 1))
        print('Current position: ' + str(player_positions[player]))
        dice_roll = rn.randint(1,6)
        print('Dice roll:' + str(dice_roll))
        player_positions[player] = player_positions[player] + dice_roll

        print('New position:'+ str(player_positions[player]))
        
        if player_positions[player] in specialSpaces:
            print('Special space! ')
            if player_positions[player] % 2:
                print('Back 5 spaces :(')
                player_positions[player] = player_positions[player] - 5
                print('New position:'+ str(player_positions[player]))
            else:
                print('Forward 5 spaces :) ')
                player_positions[player] = player_positions[player] + 5
                print('New position:'+ str(player_positions[player]))
            
        if player_positions[player] >= 100:
            someone_won = True
            print('We have a winner: player ' + str(player + 1))
            break   
            
print('Game complete.')
    

