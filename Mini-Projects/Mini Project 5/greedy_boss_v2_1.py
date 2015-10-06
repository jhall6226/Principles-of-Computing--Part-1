# Principles of Computing, Part 1
# Week 5 Practice Activity (Greedy Boss Problem)
# Jordan Hall
# 10/04/2015

import math

INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000

STANDARD = True
LOGLOG = False

def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
	salary = INITIAL_SALARY
	current_day = 1
	day_increment = 1
	bribe_cost = INITIAL_BRIBE_COST
	
	total_earned = 0
	current_cash = 0
	
	days_vs_earnings = [(0, 0)]
	
	while current_day <= days_in_simulation:
		total_earned += day_increment*salary
		current_cash += day_increment*salary
		
		while current_cash >= bribe_cost:
			salary += SALARY_INCREMENT
			current_cash -= bribe_cost
			bribe_cost += bribe_cost_increment
			
			days_vs_earnings.append((current_day, total_earned))
		
		day_increment = math.ceil((bribe_cost - current_cash)/salary)
		current_day += day_increment
	
	if not plot_type:
		days_vs_earnings = map(math.log, days_vs_earnings)
	
	return days_vs_earnings