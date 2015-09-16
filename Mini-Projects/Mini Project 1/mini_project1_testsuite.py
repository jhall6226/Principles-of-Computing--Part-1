"""
Test Suite for Merge Function for POC Mini-Project 1 (2048 Merge)
"""

import poc_simpletest

def run_testsuite(merge_function):
	"""
	Runs the Test Suite on the supplied Merge Function
	"""
	
	testsuite = poc_simpletest.TestSuite()
	
	tests = [
		([2, 0, 2, 4], [4, 4, 0, 0]),
		([0, 0, 2, 2], [4, 0, 0, 0]),
		([2, 2, 0, 0], [4, 0, 0, 0]),
		([2, 2, 2, 2, 2], [4, 4, 2, 0, 0]),
		([8, 16, 16, 8], [8, 32, 8, 0]),
	]
	
	for index, test in enumerate(tests):
		testsuite.run_test(merge_function(test[0]), test[1], 'Test #' + str(index) + ':')
		
	testsuite.report_results()
	
	