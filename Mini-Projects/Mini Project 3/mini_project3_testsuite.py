# Test Suite for Mini Project 3

import mini_project3_v1 as mp3
import poc_ttt_provided as provided
import jordan_test as jt
import poc_simpletest as pst

# mc_trial function tests
#mc_trial_tests = [(provided.TTTBoard(3, reverse=False, board=[[2,1,1],[1,3,1],[1,1,1]]), provided.PLAYERO),
#                  (provided.TTTBoard(3, reverse=False, board=[[2,3,1],[1,3,3],[1,2,1]]), provided.PLAYERX),
#                  (provided.TTTBoard(3, reverse=False), provided.PLAYERX),
#                  (provided.TTTBoard(3, reverse=True), provided.PLAYERO),
#]



#mc_trial_ptest = pst.TestSuite()

#for test in mc_trial_tests:
#    mp3.mc_trial(test[0],test[1],test[2])
#    mc_trial_ptest.run_test(test[0],test[3])
#    
#mc_trial_ptest.report_results()

# mc_update_scores function test
scores = [[0,0,0],[0,0,0],[0,0,0]]
mc_update_tests = [(scores, provided.TTTBoard(3, reverse=False, board=[[2,1,1],[1,3,1],[1,1,1]]), provided.PLAYERX),
                   (scores, provided.TTTBoard(3, reverse=False, board=[[2,3,1],[2,1,1],[3,1,1]]), provided.PLAYERX)
]



mc_update_ptest = pst.TestSuite()

for test in mc_update_tests:
    print test[1]
    print scores
    move = mp3.get_best_move(test[1], scores)
    print move
    mp3.mc_trial(test[1],test[2])
    mp3.mc_update_scores(test[0],test[1],test[2])
    print test[1]
    print scores

# get_best_move function test

# mc_move function test