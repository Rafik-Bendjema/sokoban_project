import pygame
import SokobanPuzzle
import time
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
            self.path.insert(0, current.action)  
            current = current.parent

        return self.path 
    


    def getStates(self):
        states = []
        start_time = time.time()
        solution = self.getSolution()
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
                    if not successor.isDeadBlock(): 
                        open_set.append(child)
        
        return None  

        
        
