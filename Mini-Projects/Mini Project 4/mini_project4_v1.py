# Mini Project 4, Yahtzee Strategy Planner
# Principles of Computing, Part 1
# Jordan Hall
# 09/20/2015
"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    scores = [0 for dummy_idx in range(max(hand))]
    
    for elem in hand:
        scores[elem-1] += elem

    return max(scores)

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    # Create a list to use as the starting hand for each possible completed hand from the held_dice variable
    starting_hand = [elem for elem in held_dice]
    
    # Generate a list of all sequences possible with num_die_sides and num_free_dice
    all_free_sequences = gen_all_sequences(set([idx for idx in range(1,num_die_sides+1)]),num_free_dice)

    # Initialize variable to sum the total value of all sequences, to later calculate expected value
    total_value = 0
    
    # Construct each possible hand by combining the starting hand with each free sequence, add the hand's score to the total value
    for seq in all_free_sequences:
        temp_hand = tuple(sorted(starting_hand + [elem for elem in seq]))
        total_value += score(temp_hand)
        
    # Calculate expected value by dividing total value by the number of possible hands (since all have equal probability)
    exp_value = float(total_value)/float(len(all_free_sequences))
    
    return exp_value

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    # Create a set of unique hold hands by dice index so that duplicate values don't intefere
    hold_idx_set = set([()])
    for dummy_idx in range(len(hand)):
        temp_set = set()
        for partial_sequence in hold_idx_set:
            for idx in range(len(hand)):
                new_sequence = list(partial_sequence)
                if idx not in new_sequence:
                    new_sequence.append(idx)
                    temp_set.add(tuple(new_sequence))
        hold_idx_set.update(temp_set)
    
    # Convert the unique set of hold hand indexes to an actual set of hold hand values
    all_holds_set = set([()])
    for idx_hand in hold_idx_set:
        hold_hand = tuple(sorted([hand[idx_hand[idx]] for idx in range(len(idx_hand))]))
        all_holds_set.add(hold_hand)
        
    return all_holds_set


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    # Get the entire set of possible holds from the hand
    all_holds_set = gen_all_holds(hand)
    
    # Initialize variables to hold the maximum exp value and corresponding hold tuple
    max_exp_value = 0
    max_hold = ()
    
    # Loop through all possible holds and find the one with the highest expected value score
    for hold in all_holds_set:
        temp_exp_value = expected_value(hold, num_die_sides, len(hand)-len(hold))
        if temp_exp_value > max_exp_value:
            max_exp_value = temp_exp_value
            max_hold = hold
            
    return (max_exp_value, max_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    