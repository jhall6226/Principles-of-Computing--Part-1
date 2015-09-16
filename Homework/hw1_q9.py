# Principles of Computing
# Homework 1
# Question 9

def appendsums(lst):
	"""
	Repeatedly append the sum of the current last three elements of lst to lst.
	"""
	for index in range(25):
		ele_sum = lst[-3] + lst[-2] + lst[-1]
		lst.append(ele_sum)
		
sum_three = [0, 1, 2]
appendsums(sum_three)
print(sum_three[10])

print(sum_three[20])