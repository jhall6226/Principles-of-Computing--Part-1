# Principles of Computing, Part 1
# Mini Project 1, Version 3
# Jordan Hall
# 9/7/2015

def merge(line):
	"""
    Merges a single row or column in 2048.
    """
	
	# Create new line object to store the merged line
	new_line = []
	
	# Add all non-zero elements to the new line
	for elem in line:
		if not elem == 0:
			new_line.append(elem)
	
	# Merge adjacent elements that are equal, set the left equal to the sum and the right equal to zero (ensures each element is only merged once)
	for index in range(len(new_line)-1):
		if new_line[index] == new_line[index+1]:
			new_line[index]	*= 2
			new_line[index + 1] = 0
	
	# Remove the zeroes added to the new line in the merge process
	for index in range(len(new_line)):
		if index < len(new_line) and new_line[index] == 0:
			new_line.pop(index)
			
	# Append zeroes to the end of the merged line until it is the same length as the original line
	new_line += [0]*(len(line)-len(new_line))
	
	# Return the merged line
	return new_line
	

def merge_test(test):
	"""
	Tests whether the merge function passes the given input/output case.
	Accepts a tuple with two values: (input_line, expected_output_line)
	"""
	input_line, expected_output_line = test
	
	if merge(input_line) == expected_output_line:
		result = 'PASSED'
	else:
		result = 'FAILED'
		
	return result

			
class MergeTestSuite():
	def __init__(self,input_tests):
		self.tests = input_tests
	
	def run_tests(self):
		"""
		Runs all the test in the test suite for the merge function.
		"""
		for index,test in enumerate(self.tests):
			print 'Test',str(index+1)+':',str(test[0]),'--->',str(test[1]),'-',merge_test(test)
			
	def add_test(self, test):
		"""
		Adds a test to the test suite.
		"""
		self.tests.append(test)
		
	
tests = [
		([2, 0, 2, 4], [4, 4, 0, 0]),
		([0, 0, 2, 2], [4, 0, 0, 0]),
		([2, 2, 0, 0], [4, 0, 0, 0]),
		([2, 2, 2, 2, 2], [4, 4, 2, 0, 0]),
		([8, 16, 16, 8], [8, 32, 8, 0]),
]

import mini_project1_testsuite

mini_project1_testsuite.run_testsuite(merge)

import jordan_test

mp1_jordan_testsuite = jordan_test.FunctionTestSuite(merge,tests)
mp1_jordan_testsuite.run_tests()