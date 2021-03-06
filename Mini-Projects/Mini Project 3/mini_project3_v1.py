# Mini Project 3, Tic Tac Toe Monte Carlo Player
# Principles of Computing, Part 1
# Jordan Hall
# 9/13/2015
"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#mport poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000      # Number of trials to run
SCORE_CURRENT = 3.0 # Score for squares played by the current player
SCORE_OTHER = 4.0   # Score for squares played by the other player
    
def mc_trial(board, player):
    """
    Runs a Monte Carlo trial based on the current player and state of the board.
    """

    winner = None
    cur_player = player
    
    # Run trial
    while winner == None:
        # Determine which squares are still empty
        empty_squares = board.get_empty_squares()
        
        # Randomly select one of the empty squares to be the player's next move
        random_move = empty_squares[random.randrange(len(empty_squares))]
        row, col = random_move
        board.move(row, col, cur_player)

        # Update state
        winner = board.check_win()
        cur_player = provided.switch_player(cur_player)
        
    
def mc_update_scores(scores, board, player):
    """
    Updates global scores from an iteration of a Monte Carlo trial.
    """
    winner = board.check_win()
    opp_player = provided.switch_player(player)
    
    if winner == player:
        for r_idx in range(board.get_dim()):
             for c_idx in range(board.get_dim()):
                 if board.square(r_idx,c_idx) == player:
                     scores[r_idx][c_idx] += SCORE_CURRENT
                 elif board.square(r_idx,c_idx) == opp_player:
                     scores[r_idx][c_idx] -= SCORE_OTHER
    elif winner == opp_player:
        for r_idx in range(board.get_dim()):
             for c_idx in range(board.get_dim()):
                 if board.square(r_idx,c_idx) == player:
                     scores[r_idx][c_idx] -= SCORE_CURRENT
                 elif board.square(r_idx,c_idx) == opp_player:
                     scores[r_idx][c_idx] += SCORE_OTHER
    
def get_best_move(board, scores):
    """
    Returns a move on the board (a row, column tuple) of a random move from the moves with the best score from the mc trials.
    """ 
    # Determine which squares are still empty
    empty_squares = board.get_empty_squares()
    
    # Determine the best score
    best_score = max([scores[r_idx][c_idx] for r_idx, c_idx in empty_squares])
    
    # Collect a list of moves that have the best score
    best_moves = []
    for r_idx, c_idx in empty_squares:
            if scores[r_idx][c_idx] == best_score:
                best_moves.append((r_idx, c_idx))
    
    # Return a random move from the list of best moves
    return best_moves[random.randrange(len(best_moves))]
    
def mc_move(board, player, trials):
    """
    Runs a Monte Carlo Simulation for the provided number of trials to figure out the best move for player on the current Tic Tac Toe board.
    """
    scores = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for dummy_trial in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board,player)
        mc_update_scores(scores,trial_board,player)
        
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
