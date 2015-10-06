# Test Suite for Week 5 Practice Activity
# Principles of Computing, Part 1
# Jordan Hall
# 10/04/2015

import poc_simpletest_3 as pst
import greedy_boss_v2_1 as gb

# greedy_boss function test
def greedy_boss_test():    
    print("Commencing greedy_boss function test...")
    tests = [((10, 0), [(0, 0), (10, 1000)]),
             ((12, 0), [(0, 0), (10, 1000)]),
             ((15, 0), [(0, 0), (10, 1000), (15, 2000)]),
             ((16, 200), [(0, 0), (10, 1000), (16, 2200)]),
             ((20, 1000), [(0, 0), (10, 1000), (20, 3000)]),
             ((35, 100), [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]),
             ((35, 0), [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]),
    ]
    
    greedy_boss_ts = pst.TestSuite()
    
    for test in tests:
        computed = gb.greedy_boss(test[0][0], test[0][1])
        expected = test[1]
        greedy_boss_ts.run_test(computed, expected)
        
    greedy_boss_ts.report_results()
    print()

# Run the test functions
greedy_boss_test()

