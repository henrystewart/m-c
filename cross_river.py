'''
Created on Jan 11, 2012

author: Henry I. Stewart
@ Attempts to solve the missionaries & cannibals problem

sources for help/ideas:
http://docs.python.org/tutorial/
http://www.learn4good.com/games/puzzle/boat.htm

The advice from Professor Devin Balkcom allowed me to get
the correct legal moves for each turn. 
Help debugging received from Devin Balkom 1/17/2012

Program starts with 3 missionaries, 3 cannibals, and 1 boat on one side.
The start state 

 xxx | MMM
 xxx | CCC
   x | B
   
represented by [3,3,1]

The next legal move given in the solution is illustrated as:
 xxx | MMM
 xCC | Cxx
   B | x
   
represented by [3,1,-1]

The state is shown by how many missionaries, cannibals, and boats are on the starting side.

The final state is: [0,0,-1]
 
'''
from bfs import breadth_first_search_graph
import itertools

start_state = [3,3,1]
goal = [0,0,-1]

def equals_goal(x,y):
    return x == y

'''All possible actions for movement of (missionaries, cannibals)'''
actions = [(0,1),(0,2),(1,0),(2,0),(1,1)]

''' Idea for this function taken from conversation with Devin Balkcom on 1/17/2012'''
def possible_moves(param_state):
    possible_actions = []
    for action in actions:
        m,c,b = param_state 
        m -= action[0]*b 
        c -= action[1]*b
        b *= -1
        new_action = [m,c,b]
        possible_actions.append(new_action)
    return possible_actions

def is_legal_move(list):
    legal_move = []
    for x in list:
        if (x[0] >-1 and x[1] >-1):
            if( x[0] == 3 ):
                legal_move.append(x)
            elif( x[0] == x[1] ):
                legal_move.append(x)
            elif( x[0] == 0 ):
                legal_move.append(x)
    return legal_move


def generate_legal_moves(x):
    list = possible_moves(x)
    list = is_legal_move(list)
    return list

breadth_first_search_graph(start_state,goal, equals_goal,generate_legal_moves)

t = (0,0,1)
l = [3,4]

'''
x,y=l
x+=1
print y
l = [x,y]
print l
'''






