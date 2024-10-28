import pygame
from box import Box
from typing import List
from time import sleep


class Player:
    def __init__(self, board, position , boxes : List[Box]):
        self.row, self.column = position
        self.board = board
        self.boxes = boxes

    def play(self , moves) : 
        for move in moves : 
            self.move(move)
            sleep(1)
            

    def move(self, direction):

        # Move UP
        if direction == "UP":
            if self.board[self.row - 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row -= 1  # Update the player's row position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row -1][self.column] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        # Move DOWN
        elif direction == "DOWN":
            if self.board[self.row + 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row += 1  # Update the player's row position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row +1][self.column] == "b" : 
                self.board = self.boxes[0].move(direction=direction)        
                return self.move(direction)

                print("heloo")

        # Move RIGHT
        elif direction == "RIGHT":
            if self.board[self.row][self.column + 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column += 1  # Update the player's column position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column +1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        # Move LEFT
        elif direction == "LEFT":
            if self.board[self.row][self.column - 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column -= 1  # Update the player's column position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column -1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)
            

        return self.board
