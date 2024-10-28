import pygame

class Box:
  def __init__(self,board , position):
     self.row, self.column = position
     self.board = board

  def move(self, direction):

        # Move UP
        if direction == pygame.K_UP:
            if self.board[self.row - 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row -= 1  # Update the player's row position
                self.board[self.row][self.column] = "b"

        # Move DOWN
        elif direction == pygame.K_DOWN:
            if self.board[self.row + 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row += 1  # Update the player's row position
                self.board[self.row][self.column] = "b"

        # Move RIGHT
        elif direction == pygame.K_RIGHT:
            if self.board[self.row][self.column + 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column += 1  # Update the player's column position
                self.board[self.row][self.column] = "b"

        # Move LEFT
        elif direction == pygame.K_LEFT:
            if self.board[self.row][self.column - 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column -= 1  # Update the player's column position
                self.board[self.row][self.column] = "b"

         
  
        return self.board  