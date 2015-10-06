# Principles of Computing, Part 1
# Week 5 Practice Activity (Greedy Boss Problem)
# Jordan Hall
# 10/04/2015

def greedy_boss(days_in_simulation, bribe_cost_increment): #plot_type input removed while testing
	salary = 100
	day = 1
	bribe_cost = 1000
	
	total_earned = 0
	current_cash = 0
	
	days_vs_earnings = [(0, 0)]
	
	while day <= days_in_simulation:
		total_earned += salary
		current_cash += salary
		
		if current_cash >= bribe_cost:
			while current_cash >= bribe_cost:
				salary += 100
				current_cash -= bribe_cost
				bribe_cost += bribe_cost_increment
			
			days_vs_earnings.append((day, total_earned))
		
		day += 1
	
	return days_vs_earnings