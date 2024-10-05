'''
1. Gambler
    a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
    he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
    times he/she wins and the number of bets he/she makes. Run the experiment N
    times, averages the results, and prints them out.
    b. I/P -> $Stake, $Goal and Number of times
    c. Logic -> Play till the gambler is broke or has won
    d. O/P -> Print Number of Wins and Percentage of Win and Loss
'''
import random
def gambler_game(stake,goal,trials):
    wins = 0
    total_bets = 0
    
    # Run the experiment N times
    for _ in range(trials):
        cash = stake
        bets = 0
        
        # Play until the gambler is broke or reaches the goal
        while cash > 0 and cash < goal:
            bets += 1
            total_bets += 1
            
            # Simulate the bet (50% chance to win or lose)
            if random.random() < 0.5:
                cash += 1  # Win $1
            else:
                cash -= 1  # Lose $1
        
        # If the gambler reached the goal, increment the win counter
        if cash == goal:
            wins += 1
    
    # Calculate percentage of wins and losses
    win_percentage = (wins / trials) * 100
    loss_percentage = 100 - win_percentage
    
    print(f"wins:{wins}, total_bets:{total_bets}, " 
          f"\nwin_percentage:{win_percentage}, loss_percentage:{loss_percentage}")

gambler_game(100,500,5)