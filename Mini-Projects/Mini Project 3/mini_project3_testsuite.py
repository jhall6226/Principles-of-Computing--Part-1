# Test Suite for Mini Project 3

import mini_project3_vf as mp3
import poc_ttt_provided as provided
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
def mc_update_scores_test():    
    print "Commencing mc_update_scores function test..."
    mc_update_scores_tests = [([[0,0,0],[0,0,0],[0,0,0]], provided.TTTBoard(3, reverse=False, board=[[2,2,2],[3,3,1],[1,1,1]]), provided.PLAYERX,[[1.5,1.5,1.5],[-1,-1,0],[0,0,0]]),
                            ([[0,0,0],[0,0,0],[0,0,0]], provided.TTTBoard(3, reverse=False, board=[[2,3,1],[1,3,2],[2,3,1]]), provided.PLAYERX,[[-1.5,1,0],[0,1,-1.5],[-1.5,1,0]]),
    ]
    
    mc_update_scores_ts = pst.TestSuite()
    
    for test in mc_update_scores_tests:
        mp3.mc_update_scores(test[0],test[1],test[2])
        computed = test[0]
        expected = test[3]
        mc_update_scores_ts.run_test(computed,expected)
        
    mc_update_scores_ts.report_results()
    print 

# get_best_move function test
def get_best_move_test():
    print "Commencing get_best_move function test..."
    get_best_move_tests = [(provided.TTTBoard(3, reverse=False, board=[[2,2,1],[1,3,1],[1,3,1]]), [[20,20,15],[3,-15,-9],[3,-15,-5]],[(0,2)]),
                        (provided.TTTBoard(3, reverse=False, board=[[2,3,1],[1,3,1],[2,1,1]]), [[30,-20,0],[40,-20,-5],[30,-50,10]], [(1,0)]),
                        (provided.TTTBoard(3, reverse=False, board=[[2,1,2],[1,3,1],[2,3,1]]), [[30,40,0],[40,-20,-5],[30,-50,10]], [(1,0),(0,1)]),
    ]
    
    get_best_move_ts = pst.TestSuite()
    
    for test in get_best_move_tests:
        computed_move = mp3.get_best_move(test[0],test[1])
        returned_a_best_move = False
        if computed_move in test[2]:
            returned_a_best_move = True
            
        get_best_move_ts.run_test(returned_a_best_move,True)
        
    get_best_move_ts.report_results()
    print 

# mc_move function test






# Run tests
mc_update_scores_test()
get_best_move_test()