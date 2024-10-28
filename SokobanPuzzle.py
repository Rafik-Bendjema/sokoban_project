import pygame

class SokobanPuzzle:
    def __init__(self, grid ):
        self.grid = grid
        self.player_pos = self.find_player()
        

    def isGoal(self):
        for row in self.grid : 
            for cell in row:
                if cell == 'B':
                  return False ; 
    
        return True ; 

    def successorFunction(self):
        successors = []
        moves = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        
        for move, (ver, hor) in moves.items():
            new_row, new_col = self.player_pos[0] + ver, self.player_pos[1] + hor
            
            # Check if the new position is within the grid bounds
            if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]):
                pos = self.grid[new_row][new_col]
                
                # If the player can move to an empty or target space
                if pos == ' ' or pos == 'S':
                    new_grid = [row[:] for row in self.grid]
                    new_grid[self.player_pos[0]][self.player_pos[1]] = ' ' if self.grid[self.player_pos[0]][self.player_pos[1]] == 'R' else 'S'
                    new_grid[new_row][new_col] = 'R' if pos == ' ' else '.'
                    
                    successor = SokobanPuzzle(new_grid)
                    successor.player_pos = (new_row, new_col)
                    successors.append((move, successor))
                    
                elif pos == 'B' or pos == '*':
                    # Check if the box can be pushed to the next cell
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
        
        # Move UP
        if direction == pygame.K_UP:
            if self.board[self.row - 1][self.column] == "v":
               successors.add(("up"  , ))
            elif self.board[self.row -1][self.column] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        # Move DOWN
        elif direction == pygame.K_DOWN:
            if self.board[self.row + 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row += 1  # Update the player's row position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row +1][self.column] == "b" : 
                self.board = self.boxes[0].move(direction=direction)        
                return self.move(direction)

        # Move RIGHT
        elif direction == pygame.K_RIGHT:
            if self.board[self.row][self.column + 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column += 1  # Update the player's column position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column +1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        # Move LEFT
        elif direction == pygame.K_LEFT:
            if self.board[self.row][self.column - 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column -= 1  # Update the player's column position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column -1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)
            
        return self.board
    
