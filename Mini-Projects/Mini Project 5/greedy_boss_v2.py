# Principles of Computing, Part 1
# Week 5 Practice Activity (Greedy Boss Problem)
# Jordan Hall
# 10/04/2015

INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment): #plot_type input removed while testing
	salary = 
	current_day = 1
	day_increment = 1
	bribe_cost = INITIAL_BRIBE_COST
	
	total_earned = 0
	current_cash = 0
	
	days_vs_earnings = [(0, 0)]
	
	while day <= days_in_simulation:
		if current_cash >= bribe_cost:
			while current_cash >= bribe_cost:
				salary += 100
				current_cash -= bribe_cost
				bribe_cost += bribe_cost_increment
			
			days_vs_earnings.append((day, total_earned))
		
		day_increment = (bribe_cost - current_cash)/salary
		day += day_increment
		total_earned += day_increment*salary
		current_cash += day_increment*salary
	
	return days_vs_earnings