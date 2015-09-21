# Test Suite for Mini Project 4
# Principles of Computing, Part 1
# Jordan Hall
# 09/20/2015

import poc_simpletest as pst
import mini_project4_v1 as mp4

# score function test
def score_test():    
    print "Commencing score function test..."
    tests = [((1, 1, 2, 2, 4), 4),
             ((2, 3, 3, 5, 5), 10),
             ((1, 1, 1, 1, 6), 6),
    ]
    
    score_ts = pst.TestSuite()
    
    for test in tests:
        computed = mp4.score(test[0])
        expected = test[1]
        score_ts.run_test(computed, expected)
        
    score_ts.report_results()
    print 

# expected_value function ttest
def expected_value_test():
    print "Commencing expected_value function test..."
    tests = [((6,), 6, 1, 7.0),
             ((1,), 6, 1, 22./6),
             ((6, 6), 6, 1, 13.0),
    ]
    
    exp_value_ts = pst.TestSuite()
    
    for test in tests:
        computed = mp4.expected_value(test[0], test[1], test[2])
        expected = test[3]
        exp_value_ts.run_test(computed, expected)
        
    exp_value_ts.report_results()
    print   

# get_all_holds function test
def gen_all_holds_test():
    print "Commencing get_all_holds function test..."
    tests = [((1, 2), set([(), (1,), (2,), (1, 2)])),
             ((1, 1), set([(), (1,), (1, 1)])),
             ((1, 2, 2), set([(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)])),
    ]
    
    all_holds_ts = pst.TestSuite()
    
    for test in tests:
        computed = mp4.gen_all_holds(test[0])
        expected = test[1]
        all_holds_ts.run_test(computed, expected)
        
    all_holds_ts.report_results()
    print   

# strategy function test
def strategy_test():
    print "Commencing strategy function test..."
    tests = [((6, 6, 4, 3, 2), 6, (mp4.expected_value((6, 6), 6, 3), (6, 6))),
    ]
    
    strategy_ts = pst.TestSuite()
    
    for test in tests:
        computed = mp4.strategy(test[0], test[1])
        expected = test[2]
        strategy_ts.run_test(computed, expected)
        
    strategy_ts.report_results()
    print   

# Run the test functions
score_test()
expected_value_test()
gen_all_holds_test()
strategy_test()