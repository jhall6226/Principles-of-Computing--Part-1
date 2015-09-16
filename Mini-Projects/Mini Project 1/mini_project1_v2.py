# Principles of Computing, Part 1
# Mini Project 1, Version 2
# Jordan Hall
# 9/4/2015

def merge(line):
	"""
    Merges a single row or column in 2048.
    """
	
	new_line = [0]*len(line)
	
	merge_flag = False
	
	for index in range(len(line)):
		if merge_flag:
			merge_flag = False
		elif line[index] == 0:
			pass
		elif index == len(line) - 1:
			new_line[index] = line[index]
		elif line[index] == line[index + 1]:
			new_line[index] = line[index]*2
			new_line[index+1] = 0
			merge_flag = True
		else:
			new_line[index] = line[index]
	
	non_zeroes = []
	
	for index, element in enumerate(new_line):
		if not element == 0:
			non_zeroes.append(new_line.pop(index))
	
	new_line = non_zeroes + new_line
	
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

merge_test_suite = MergeTestSuite(tests)
merge_test_suite.run_tests()