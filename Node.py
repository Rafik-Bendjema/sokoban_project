import pygame
import SokobanPuzzle
import queue

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
        open_set = queue.Queue()
        closed_set = set()  # Use a set for faster lookup

        if self.state.isGoal():
            return self 
        
        open_set.put(self)  # Enqueue initial node

        while not open_set.empty(): 
            current = open_set.get()
            closed_set.add(current.state)  # Mark state as visited

            for (action, successor) in current.state.successorFunction():
                child = Node(successor, current, action)
                
                if child.state.isGoal():
                    return child
                
                if successor not in closed_set:
                    open_set.put(child)
        
        return None
