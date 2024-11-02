import pygame

class SokobanPuzzle:
    
    def __init__(self, grid ):
        self.grid = grid
        self.player_pos = self.find_player()
        self.moves = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        

    def isGoal(self):
        for row in self.grid : 
            for cell in row:
                if cell == 'B':
                  return False ; 
    
        return True ; 
    
    def isDeadBlock(self) : 
        return (self.isCornerDeadBlock() or self.is_line_deadlock())
    

    def isCornerDeadBlock(self):

        
        
        for row in range(len(self.grid)) :  
            for cell in range(len(self.grid[row])): 
                if self.grid[row][cell] == 'B':
                    if self.grid[row +1][cell] == 'O' or self.grid[row -1][cell] == 'O' : 
                      if self.grid[row][cell+1] == 'O' or self.grid[row][cell-1] == 'O' :
                        return True 
        
        return False 
    
    def is_line_deadlock(self):
        
        horizontal = [(0, -1), (0, 1)]  
        vertical = [(-1, 0), (1, 0)]    

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 'B':  
                    
                    if self.is_deadlock_line(row, col, horizontal):
                        return True
                    
                    if self.is_deadlock_line(row, col, vertical):
                        return True
        return False

    def is_deadlock_line(self, row, col, direction_pair):
        
        for d_row, d_col in direction_pair:
            side_wall = True
            current_row, current_col = row, col

            
            while 0 <= current_row < len(self.grid) and 0 <= current_col < len(self.grid[0]):
                next_row, next_col = current_row + d_row, current_col + d_col

                
                if 0 <= next_row < len(self.grid) and 0 <= next_col < len(self.grid[0]):
                    if self.grid[next_row][next_col] != 'O':  
                        side_wall = False
                        break
                else:
                    break  

                
                current_row += d_row
                current_col += d_col

            
            if side_wall:
                return True

        return False

                        






    def successorFunction(self):
        successors = []
        moves = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        
        for move, (ver, hor) in self.moves.items():
            new_row, new_col = self.player_pos[0] + ver, self.player_pos[1] + hor
            
            
            if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]):
                pos = self.grid[new_row][new_col]
                
                
                if pos == ' ' or pos == 'S':
                    new_grid = [row[:] for row in self.grid]
                    new_grid[self.player_pos[0]][self.player_pos[1]] = ' ' if self.grid[self.player_pos[0]][self.player_pos[1]] == 'R' else 'S'
                    new_grid[new_row][new_col] = 'R' if pos == ' ' else '.'
                    
                    successor = SokobanPuzzle(new_grid)
                    successor.player_pos = (new_row, new_col)
                    successors.append((move, successor))
                    
                elif pos == 'B' or pos == '*':
                    
                    box_row, box_col = new_row + ver, new_col + hor
                    if 0 <= box_row < len(self.grid) and 0 <= box_col < len(self.grid[box_row]):
                        box_pos = self.grid[box_row][box_col]
                        if box_pos == ' ' or box_pos == 'S':
                            new_grid = [row[:] for row in self.grid]
                            new_grid[self.player_pos[0]][self.player_pos[1]] = ' ' if self.grid[self.player_pos[0]][self.player_pos[1]] == 'R' else 'S'
                            new_grid[new_row][new_col] = 'R' if pos == 'B' else '.'
                            new_grid[box_row][box_col] = 'B' if box_pos == ' ' else '*'
                            
                            successor = SokobanPuzzle(new_grid)
                            successor.player_pos = (new_row, new_col)
                            successors.append((move, successor))
        
        return successors


    def find_player(self):
        """Find the initial position of the player on the board."""
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 'R' or self.grid[row][col] == '.':
                    return (row, col)
        return None

    def move(self, direction):
        successors = []  
        
        
        if direction == pygame.K_UP:
            if self.board[self.row - 1][self.column] == "v":
               successors.add(("up"  , ))
            elif self.board[self.row -1][self.column] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        
        elif direction == pygame.K_DOWN:
            if self.board[self.row + 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row += 1  
                self.board[self.row][self.column] = "p"
            elif self.board[self.row +1][self.column] == "b" : 
                self.board = self.boxes[0].move(direction=direction)        
                return self.move(direction)

        
        elif direction == pygame.K_RIGHT:
            if self.board[self.row][self.column + 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column += 1  
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column +1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        
        elif direction == pygame.K_LEFT:
            if self.board[self.row][self.column - 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column -= 1  
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column -1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)
            
        return self.board
    
