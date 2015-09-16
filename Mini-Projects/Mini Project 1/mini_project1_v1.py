"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    # If the line is length 1, then we cannot merge it. Return the line.
    if len(line) == 1:
        return line
    
    else:
        new_line = []
        anchor = 0
        
        # anchor is the index that we are currently testing
        # against the remaining numbers in the line to the
        # right to see if we can merge with it.
    
        # Loop through anchors until we reach the last index in the line
        while anchor < len(line) - 1:
            
            # If all remaining values past the anchor are zero,
            # add the anchor to new_line and break the loop
            if sum(line[anchor+1:]) == 0:
                new_line.append(line[anchor])
                break
            
            # If anchor is equal to zero, shift it over 1
            elif line[anchor] == 0:
                anchor += 1
                
            else:
                # reach is the index we are currently testing
                # against anchor.
                
                # Scan to the right of anchor in the line until 
                # you hit a non-zero number or the end of the line.
                # If this number equals the anchor, merge them, add to new_line, 
                # and set anchor to be the index after reach. If not, add the 
                # anchor to new_line and set anchor to be equal to the next 
                # non-zero number (reach). Once a value is found, break the loop.
                for reach in range(anchor+1,len(line)):
                    if not reach == len(line) - 1 and line[reach] == 0:
                        pass
                    elif line[anchor] == line[reach]:
                        new_line.append(line[anchor]*2)
                        anchor = reach + 1
                        break
                    else:
                        new_line.append(line[anchor])                        
                        anchor = reach
                        break
            # If anchor is the last index in the line,
            # add its value to new_line
            if anchor == len(line) - 1:
                    new_line.append(line[anchor])
        
        # Add zeros to the end of new_line after all values
        # have been merged to retain the size of the input line
        new_line += [0]*(len(line)-len(new_line))                        

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