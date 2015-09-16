"""
Basic test suite module that allows the user to create test suites for a specific function and store input/ expected output values for that function
"""

def function_test(function, test_case):
	"""
	Tests whether the supplied function passes the given input/output case.
	Accepts a tuple with two values: (input_line, expected_output_line)
	"""
	input_line, expected_output_line = test_case
	
	if function(input_line) == expected_output_line:
		result = 'PASSED'
	else:
		result = 'FAILED'
		
	return result
 
			
class FunctionTestSuite():
	def __init__(self,function,tests=[]):
		self.tests = tests
		self.function = function		
	
	def run_tests(self):
		"""
		Runs all the test in the test suite for the merge function.
		"""
		
		failures = 0
				
		for index,test in enumerate(self.tests):
			result = function_test(self.function,test)
			print 'Test',str(index+1)+':',str(test[0]),'--->',str(test[1]),'-',result
			if result == 'FAILED':
				failures += 1			
			
		print 'Ran', str(len(self.tests)), 'tests.', str(failures), 'failures.'
			
	def add_test(self, test):
		"""
		Adds a test to the test suite.
		"""
		self.tests.append(test)