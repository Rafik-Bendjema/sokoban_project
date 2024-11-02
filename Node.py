import pygame
import SokobanPuzzle

class Node:
   
    def __init__(self, state: SokobanPuzzle.SokobanPuzzle, parent=None, action=None):
        self.state = state  
        self.parent = parent  
        self.action = action  
        self.path = []

    def getPath(self):
        solution = self.getSolution()
        if solution is None:
            print("Solution is None")
            return []

        current = solution
        while current.parent is not None: 
            self.path.insert(0, current.action)  # Add action to the path list
            current = current.parent

        return self.path 
    


    def getStates(self):
        states = []
        solution = self.getSolution()
        if solution is None:
            print("Solution is None")
            return []

        current = solution
        while current.parent is not None: 
            states.insert(0, current.state.grid)  # Add action to the path list
            current = current.parent 
        
        return states
        


    def getSolution(self):
        open_set = [self]  # Start with the initial node in the open set
        closed_set = []  # Use a set for visited nodes to speed up lookup

        while open_set:
            current = open_set.pop(0)  # Take the first element from open_set
            
            if current.state.isGoal():
                return current  # Return the node if it's the goal

            closed_set.append(current.state.grid)  # Mark current state as visited

            for action, successor in current.state.successorFunction():
                child = Node(successor, current, action)

                # Check if this child state is the goal
                if child.state.isGoal():
                    return child

                # Add child to open_set if not already in closed_set or open_set
                if successor.grid not in closed_set and all(
                    node.state.grid != successor.grid for node in open_set):
                    open_set.append(child)
        
        return None  # Return None if no solution is found

        
        
