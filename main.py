from Node import Node
from SokobanPuzzle import SokobanPuzzle
game_map = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'R', ' ', ' ', 'O'],
    ['O', 'S', 'B', ' ', 'O'],
    ['O', 'O', 'O', 'O', 'O']
]
init = Node(SokobanPuzzle(game_map))
print(len(init.getStates()))