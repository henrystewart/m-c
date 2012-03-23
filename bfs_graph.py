'''
Created on Jan 11, 2012

@author: Henry I. Stewart
 
Performs breath first search algorithm on a graph!

'''

from collections import deque


'''
Nodes are objects that contain
    1. state
    2. back pointers to other nodes
'''
class Node:
    def _init_(self, state, bck_ptr):
        self.state = state
        self.bck_ptr = bck_ptr
 
'''
BFS requires:
- a start state
- a goal state
- an equals operator 
- a way to find neighbors in the graph (gen_children)
'''
def breadth_first_search_graph(start_state, goal, equals, gen_children):
    #frontier = new queue
    frontier = deque([])
    
    #pack start state into a node
    x = Node()
    x.state = start_state
    #print "printing " + str(x)
    #add node to frontier
    frontier.append(x)
    
    #explored = new set /n add start_state to explored
    explored = []
    explored.append(start_state)

    #while frontier is not empty:
    while frontier != 0:
        #get current node from the frontier
        try:
            current_node = frontier.popleft()
        except IndexError:
            print "failure"
            break
        #get current_state from current_node
        current_state = current_node.state
        
        #if current state is the goal:
        
        if equals(current_state,goal):
            #solution = backchain(current_node, equals)
            return "solution"
        print "Goal:" + str(goal)
        print "Current_state: " + str(current_state)
        
        #child = gen_children(start_state)
        #print current_state
        #print "Children: " + str(gen_children(current_state))
        #for child in current_state: // don't know if this line is right, but we'll leave for now
        child = gen_children(current_state)
        #print child
        #print "Explored: " + str(explored)
        for x in child:
            if not(x in explored):
                y = Node()
                explored.append(x)
                y.state = x
                y.bck_ptr = current_node
                frontier.append(y)
        #print "Frontier"   
    return "failure"


def backchain(current_node,equals):
    stack = [current_node]
    parent_node = current_node.bck_ptr
    while not(equals(parent_node,stack)):
        parent_node = current_node.bck_ptr
        stack.append(parent_node)
    
def print_frontier(f):
    for x in f:
        print x.state