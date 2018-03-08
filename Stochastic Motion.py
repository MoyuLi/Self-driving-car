#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:19:34 2018

@author: moyuli
"""
#
# Write a function called stochastic_value that 
# returns two grids. The first grid, value, should 
# contain the computed value of each cell as shown 
# in the video. The second grid, policy, should 
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True
    while change:
        change = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if goal[0]==i and goal[1]==j:
                    if value[i][j]!=0:
                        value[i][j] = 0
                        policy[i][j] = '*'
                        change = True
                    
                elif grid[i][j]==0:
                    for a in range(len(delta)):
                        i_success = i + delta[a][0]
                        j_success = j + delta[a][1]
                        i_left = i + delta[(a+1)%4][0]
                        j_left = j + delta[(a+1)%4][1]
                        i_right = i + delta[(a-1)%4][0]
                        j_right = j + delta[(a-1)%4][1]
                        if i_success<0 or i_success>=len(grid) or j_success<0 or j_success>=len(grid[0]):
                            value_success = collision_cost
                        elif grid[i_success][j_success] == 1:
                            value_success = collision_cost
                        else:
                            value_success = value[i_success][j_success]
                        if i_left<0 or i_left>=len(grid) or j_left<0 or j_left>=len(grid[0]):
                            value_left = collision_cost
                        elif grid[i_left][j_left] == 1:
                            value_left = collision_cost
                        else:
                            value_left = value[i_left][j_left]   
                        if i_right<0 or i_right>=len(grid) or j_right<0 or j_right>=len(grid[0]):
                            value_right = collision_cost
                        elif grid[i_right][j_right] == 1:
                            value_right = collision_cost
                        else:
                            value_right = value[i_right][j_right]    
                        v2 = success_prob*value_success + failure_prob*(value_left+value_right)+cost_step
                        if v2 < value[i][j]:
                            value[i][j] = v2
                            policy[i][j] = delta_name[a]
                            change = True
                        

    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0])-1] # Goal is in top right corner
cost_step = 1
collision_cost = 1000
success_prob = 0.5

value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
for row in value:
    print (row)
for row in policy:
    print (row)

# Expected outputs:
#
#[471.9397246855924, 274.85364957758316, 161.5599867065471, 0],
#[334.05159958720344, 230.9574434590965, 183.69314862430264, 176.69517762501977], 
#[398.3517867450282, 277.5898270101976, 246.09263437756917, 335.3944132514738], 
#[700.1758933725141, 1000, 1000, 668.697206625737]


#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
