import random

# simulation of the wii party minigame "hide-and-peek".
# 3 hiders, 1 seeker. seven spots: 6 legit, 1 joke.
# seeker can look in 5 of the 7 spots to find all 3 hiders. if all are found within 5 searches, seeker wins. if not, hiders win.

# two strategies being tested:
# strategy A: all hiders randomly choose among the 6 legit spots (repeats allowed).
# strategy B: one hider deliberately hides in the joke spot; other two randomly choose among the 6 legit spots (repeats allowed).

def strategyA(trials: int) -> float :
    '''
    simulate games where all three hiders choose randomly among the 6 legit spots.
    the seeker has 5 searches among those 6 legit spots.
    returns the proportion of games won by the hiders.
    '''
    legitSpots = [0, 1, 2, 3, 4, 5] # legit hiding spots
    jokeSpot = 6 # joke spot (unused here, included for clarity's sake)
    hiderWins = 0

    for j in range(trials) :
        # hiders choose spots randomly (with replacement)
        hiderSpots = []
        for h in range(3) :
            chosen = random.choice(legitSpots)
            hiderSpots.append(chosen)

        # seeker chooses 5 unique spots to search among the legit spots
        searchSpots = set()
        while len(searchSpots) < 5 :
            picked = random.choice(legitSpots)
            searchSpots.add(picked)

        # determine if all hiders have been found
        allFound = True
        for spot in hiderSpots :
            if spot not in searchSpots :
                allFound = False
                break

        # if any hider is not found, the hiders win
        if not allFound :
            hiderWins += 1

    return hiderWins / trials

def strategyB(trials: int) -> float :
    '''
    simulate games where one hider chooses the joke spot (6) and the other two choose among the 6 legit spots.
    the seeker must still use one search on the joke spot, leaving 4 searches among the 6 legit spots.
    returns the proportion of games won by the hiders.
    '''
    legitSpots = [0, 1, 2, 3, 4, 5] # legit hiding spots
    jokeSpot = 6 # joke spot
    hiderWins = 0

    for j in range(trials) :
        # place one hider in the joke spot
        hiderSpots = [jokeSpot]

        # other two hiders choose among legit spots
        for h in range(2) :
            chosen = random.choice(legitSpots)
            hiderSpots.append(chosen)

        # seeker search set starts with the joke spot
        searchSpots = {jokeSpot}

        # seeker then chooses 4 unique spots to search among the legit spots
        while len(searchSpots) < 5 :
            picked = random.choice(legitSpots)
            searchSpots.add(picked)

        # determine if all hiders have been found
        allFound = True
        for spot in hiderSpots :
            if spot not in searchSpots :
                allFound = False
                break

        # if any hider is not found, the hiders win
        if not allFound :
            hiderWins += 1

    return hiderWins / trials

def simulateSingleGame(strategy: str) :
    '''
    simulate one game under a certain strategy and return details.
    the code here is the same as the other two functions.
    '''
    legitSpots = [0, 1, 2, 3, 4, 5]
    jokeSpot = 6
    if strategy == "A":
        hiderSpots = []
        for h in range(3) :
            chosen = random.choice(legitSpots)
            hiderSpots.append(chosen)
        searchSpots = set()
        while len(searchSpots) < 5 :
            picked = random.choice(legitSpots)
            searchSpots.add(picked)
    elif strategy == "B":
        hiderSpots = [jokeSpot]
        for h in range(2) :
            chosen = random.choice(legitSpots)
            hiderSpots.append(chosen)
        searchSpots = {jokeSpot}
        while len(searchSpots) < 5 :
            picked = random.choice(legitSpots)
            searchSpots.add(picked)
    else :
        return None, None, None
    allFound = True
    for spot in hiderSpots :
        if spot not in searchSpots :
            allFound = False
            break
    if not allFound :
        winner = "Hiders"
    else :
        winner = "Seeker"
    return hiderSpots, searchSpots, winner

def examples(strategy: str, nExamples: int) :
    print(f"-- {nExamples} example games for Strategy {strategy} --")
    for i in range(nExamples) :
        hiderSpots, searchSpots, winner = simulateSingleGame(strategy)
        print(f"Game {i + 1}:")
        print(f"  Hider spots: {hiderSpots}")
        print(f"  Search spots: {list(searchSpots)}")
        print(f"  Winner: {winner}\n")

def main() :
    # ----------------------------------------
    # set to true to run that number of trials
    runTrials = False
    numTrials = 10000
    # ----------------------------------------
    # set to true to display sample games
    showExamples = True
    nExamples = 3
    # ----------------------------------------

    # run trials
    if runTrials :
        hiderWinRateA = strategyA(numTrials)
        hiderWinRateB = strategyB(numTrials)
        advantage = abs(hiderWinRateA - hiderWinRateB)
        equal = False
        if hiderWinRateA > hiderWinRateB :
            betterStrat = "Strategy A"
        elif hiderWinRateA == hiderWinRateB:
            equal = True
        else :
            betterStrat = "Strategy B"
        print()
        print(f"--- Simulation results ---")
        print(f"{numTrials} trials run on both strategies")
        print()
        print(f"Strategy A hider win percentage: {hiderWinRateA * 100:.2f}%")
        print(f"Strategy B hider win percentage: {hiderWinRateB * 100:.2f}%")
        print()
        if not equal : 
            print(f"Using {betterStrat}, the hiders were {advantage * 100:.2f}% more likely to win this round!")
        else :
            print(f"Strategies A and B gave the hiders equal chances to win this round!")
        print()

    # show examples
    if showExamples :
        print()
        examples("A", nExamples)
        examples("B", nExamples)

    # if neither are enabled
    if (not runTrials) and (not showExamples) :
        print("Enable something...")
        print()

if __name__ == "__main__" :
    main()