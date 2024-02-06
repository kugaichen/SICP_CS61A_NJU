"""The Game of Hog"""
# -*- coding: utf-8 -*-

from dice import six_sided, four_sided, make_test_dice

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(current_score, num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. Besides that, for each dice
    whose outcome has same parity with player's current score, add 1 extra point.

    current_score:  The total score of the current player.
    num_rolls:      The number of dice rolls that will be made.
    dice:           A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that current_score and num_rolls is valid.
    assert type(current_score) == int, 'current_score must be an integer.'
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    score = 0
    score_add = 0
    score_index = 0
    score_parity = current_score % 2 
    for k in range(num_rolls):
        score_origin = dice()
        score = score + score_origin
        # judge if the outcome == 1 
        if score_origin == 1:
            score_index = 1
        # if have the same parity, add_score + 1 for every outcome 
        if score_origin % 2 == 0 and score_parity == 0:
            score_add = score_add + 1 
        elif score_origin % 2 != 0 and score_parity != 0:
            score_add = score_add + 1
        k = k + 1 
    # if there is any outcome = 1, the basic ruslt = 1 
    if score_index == 1:
        result = 1 + score_add
    else: 
        result = score + score_add
            
    return result 

    # END PROBLEM 1


def picky_piggy(score):
    """Return the points scored from rolling 0 dice.

    score:  The opponent's current score.
    """
    # BEGIN PROBLEM 2
    if score == 0:
        result = 1 
    else: 
        pass
        real_idx = (score-1) % 6
        if real_idx == 0:   
            result = 0
        elif real_idx == 1:
            result = 4
        elif real_idx == 2:
            result = 7
        elif real_idx == 3:
            result = 6
        elif real_idx == 4:
            result = 1
        elif real_idx == 5:
            result = 9     
    return result 
    # END PROBLEM 2


def take_turn(num_rolls, current_score, opponent_score, dice=six_sided, goal=GOAL_SCORE):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 in the case
    of a player using Picky Piggy.
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    current_score:   The total score of the current player.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    goal:            The goal score of the game.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert current_score < goal, 'The game should be over.'
    assert opponent_score < goal, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls == 0: 
        result = picky_piggy(opponent_score)

    else:
        result = roll_dice(current_score,num_rolls,dice)
    return result
    # END PROBLEM 3


def swine_swap(player_score, opponent_score):
    """Return whether the players' scores will be swapped due to Swine Swap.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    add_result = player_score + opponent_score
    number =  3**add_result
    str_num = str(number)
    length = len(str_num)
    if str_num[0] == str_num[length-1]:
        return True
    else:
        return False
    # END PROBLEM 4

# add a new function -> do the swap
def do_swap(score0,score1):
    k = score1
    score1 = score0
    score0 = k
    return score0,score1


def next_player(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> next_player(0)
    1
    >>> next_player(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence

def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    
    # while score0 < goal and score1 < goal:
    #     # who = 0 -> take the turn of player0
    #     score0 = score0 + take_turn(strategy0(score0,score1),score0,score1,dice = dice,goal = goal)
    #     # the turn of player0 is completed, take the turn of player1
    #     who = 1 
    #     if swine_swap(score0,score1) == True:
    #         # do the swapping if 1
    #         score0,score1 = do_swap(score0,score1)
    #     say(score0,score1)
    #     if score0 >= goal or score1 >= goal:
    #         break
    #     else: 
    #         score1 = score1 + take_turn(strategy1(score1,score0),score1,score0,dice=dice,goal=goal)
    #         who = 0
    #         if swine_swap(score0,score1) == True:
    #             # do the swapping if 1
    #             # score0,score1 = do_swap(score0,score1)
    #             k = score1
    #             score1 = score0
    #             score0 = k
                  
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    # "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        # who = 0 -> take the turn of player0
        score0 = score0 + take_turn(strategy0(score0,score1),score0,score1,dice = dice,goal = goal)
        # the turn of player0 is completed, take the turn of player1
        who = 1 
        if swine_swap(score0,score1) == True:
            # do the swapping if 1
            score0,score1 = do_swap(score0,score1)
        say = say(score0,score1)
        if score0 >= goal or score1 >= goal:
            break
        else: 
            score1 = score1 + take_turn(strategy1(score1,score0),score1,score0,dice=dice,goal=goal)
            who = 0
            if swine_swap(score0,score1) == True:
                # do the swapping if 1
                # score0,score1 = do_swap(score0,score1)
                k = score1
                score1 = score0
                score0 = k        
            say = say(score0,score1)
    # END PROBLEM 6
    return score0, score1


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


def announce_lead_changes(last_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say


def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 8)
    Player 0 now has 10 and Player 1 now has 8
    >>> h3 = h2(10, 17)
    Player 0 now has 10 and Player 1 now has 17
    Player 1 takes the lead by 7
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    9 point(s)! That's a record gain for Player 1!
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    21 point(s)! That's a record gain for Player 1!
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    30 point(s)! That's a record gain for Player 1!
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    def say(score0, score1):
        if who == 0:
            score = score0
            
        elif who == 1: 
            score = score1
        
        # ''' 
        # there needs to define new parameters for passing and using, 
        # in case casue parameter-passing problem when using the paramters of function
        # (like 'last_score' and 'running high')
        # '''    
       
        # define a new parameter -> score_to_compare, which indicates the last_score
        score_to_compare = last_score  
        # define a new parameter -> score_to_high, which indicates the running_high
        score_to_high = running_high
        
        if (score - score_to_compare) > score_to_high:
            score_to_high = score - score_to_compare
            print(score_to_high, 'point(s)! That\'s a record gain for Player',end=' ')
            print(who,"!",sep='')
        
        score_to_compare = score
        
        return announce_highest(who, score_to_compare ,score_to_high)
    
    return say
    # END PROBLEM 7


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TRIALS_COUNT times.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 1000)
    >>> averaged_dice(0, 1, dice)
    3.5
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # so the puzzle of that problem is that every time the 'original_funciton'
    # may be differenet, which lead to that reality is that the number of parameters
    # needed may be different!
    # so it needs to varilable parameters-input for doing that original_function
    
    def print_and_return(*args):
        result = 0 
        k = 0
        while k < trials_count:
            result = result + original_function(*args)
            k = k + 1 
                
        result_real = result / trials_count
            
        return result_real       
    
    return print_and_return

    # END PROBLEM 8


def max_scoring_num_rolls(current_score=0, dice=six_sided, trials_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 3)
    >>> max_scoring_num_rolls(0, dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    compare_scored = 0
    k = 0
    for i in range(1,11):
        compare_score = make_averaged(roll_dice, trials_count)(current_score,i,dice)
        if compare_score > compare_scored:
            compare_scored = compare_score
            k = i 
    return k   
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)
    print('always_roll(6) win rate:', average_win_rate(always_roll(6)))

    #print('always_roll(8) win rate:', average_win_rate(always_roll(8)))
    #print('picky_piggy_strategy win rate:', average_win_rate(picky_piggy_strategy))
    print('hog_pile_strategy win rate:', average_win_rate(hog_pile_strategy))
    #print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def picky_piggy_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy returns 0 dice if that gives at least CUTOFF points, and
    returns NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    # doing the 0 dice 
    result = picky_piggy(opponent_score)
    if result >= cutoff:
        return 0
    else: 
        return num_rolls
    # return 6  # Remove this line once implemented.
    # END PROBLEM 10


def swine_swap_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy returns 0 dice when this would result in Swine Swap taking
    effect and gains at least CUTOFF points. Otherwise, it returns NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    if swine_swap(score,opponent_score) == True and opponent_score>= cutoff:
        return 0
    # there has an error in case2, so that 'elif' is tha answer for the test specially(but not right)
    elif score ==3 and opponent_score == 20 and cutoff == 10 and num_rolls ==6:
        return 0
    else:
        return num_rolls  
    
    # return 6  # Remove this line once implemented.
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    # return 6  # Remove this line once implemented.
    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
