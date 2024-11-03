import pygame
import SokobanPuzzle
import queue
import heapq
import time
import itertools  


class Node:
   
    def __init__(self, state: SokobanPuzzle.SokobanPuzzle, parent=None, action=None, g=0):
        self.state = state  
        self.parent = parent  
        self.action = action  
        self.path = []
        self.g = g                             # Path cost to reach this node
        self.f = 0                             # Fitness value for A* (g + h)
        self.setF() 

    def getPath(self):
        solution = self.getSolution()
        if solution is None:
            print("Solution is None")
            return []

        current = solution
        while current.parent is not None: 
            self.path.insert(0, current.action)  
            current = current.parent

        return self.path 
    
    def setF(self):
        # Set f to a value based on heuristic h2 for A*
        self.f = self.g + self.heuristic_h2()

    def heuristic_h1(self):
        # Heuristic h1: number of boxes not in target spaces
        boxes = self.state.find_boxes()
        targets = set(self.state.find_storages())
        nb_left_blocks = sum(1 for box in boxes if box not in targets)
        return nb_left_blocks

    def heuristic_h2(self):
        # Heuristic h2: enhanced heuristic with Manhattan distance estimation
        boxes = self.state.find_boxes()
        targets = self.state.find_storages()

        # h1 part: 2 * number of boxes not yet in targets
        h1_value = 2 * self.heuristic_h1()

        # Add Manhattan distances from each box to its closest target
        total_distance = 0
        for box in boxes:
            min_distance = min(abs(box[0] - target[0]) + abs(box[1] - target[1]) for target in targets)
            total_distance += min_distance

        return h1_value + total_distance

    def getStates(self):
        states = []
        start_time = time.time()
        solution = self.AStar()
        print("--- %s seconds ---" % (time.time() - start_time))

        if solution is None:
            print("Solution is None")
            return []

        current = solution
        while current.parent is not None: 
            states.insert(0, current.state.grid)  
            current = current.parent 
        
        return states
        


    def getSolution(self):
        open_set = [self]  
        closed_set = []  

        while open_set:
            current = open_set.pop(0)  
            
            if current.state.isGoal():
                return current  

            closed_set.append(current.state.grid)  

            for action, successor in current.state.successorFunction():
                child = Node(successor, current, action)

                
                if child.state.isGoal():
                    return child

                
                if successor.grid not in closed_set and all(
                    node.state.grid != successor.grid for node in open_set):
                        if successor.isDeadBlock():
                            open_set.append(child)
        
        return None  
    
    def AStar(self):
        open_set = {}  # Dictionary to store nodes with their states as keys
        closed_set = set()  # Set to track visited states

        # Initialize the open set with the start node
        open_set[tuple(map(tuple, self.state.grid))] = self  

        while open_set:
            # Select the node with the lowest f value in open_set
            current = min(open_set.values(), key=lambda node: node.f)
            del open_set[tuple(map(tuple, current.state.grid))]  

            if current.state.isGoal():
                return current

            # Mark current state as visited
            closed_set.add(tuple(map(tuple, current.state.grid)))

            # Expand successors
            for action, successor in current.state.successorFunction():
                child = Node(successor, current, action, g=current.g + 1)
                child.setF()

                # If this state is already visited, skip it
                if tuple(map(tuple, child.state.grid)) in closed_set:
                    continue

                # If the state is already in open_set, replace it if this path is better
                child_key = tuple(map(tuple, child.state.grid))
                if child_key in open_set:
                    if child.f < open_set[child_key].f:
                        open_set[child_key] = child  # Replace with the better path
                else:
                    # Add new child state to open_set
                    open_set[child_key] = child

        # Return None if no solution found
        return None




        
        
