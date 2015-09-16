# Homework 3, Question 8

list_of_outcomes = [x+y for y in range(1,7) for x in range(1,7)]
unique_outcomes = set(list_of_outcomes)
outcome_counts = {}
for outcome in unique_outcomes:
	outcome_counts[outcome] = 0

for value in list_of_outcomes:
	for outcome in unique_outcomes:
		if value == outcome:
			outcome_counts[outcome] += 1
			break

outcome_probabilities = {}
odd_probability = 0
for outcome in unique_outcomes:
	outcome_probabilities[outcome] = float(outcome_counts[outcome])/float(len(list_of_outcomes))
	if not outcome % 2 == 0:
		odd_probability += outcome_probabilities[outcome]

print odd_probability