

# returned mostly bad moves: [(1, 2), (2, 2), (1, 2), (0, 2), (2, 2)]

import mini_project3_v1 as mp3
import poc_ttt_provided as provided


board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]])

print board
print

moves = []
for dummy_var in range(100):
    moves.append(mp3.mc_move(board, provided.PLAYERX, 1000))
    
    
set_of_moves = set(moves)
count_of_moves = {}

for move in set_of_moves:
    count_of_moves[move] = 0

for move in moves:
    count_of_moves[move] += 1
    
print count_of_moves
    