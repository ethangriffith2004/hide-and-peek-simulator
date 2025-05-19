'''
Copyright (c) 2025 Ethan Griffith
Licensed under the MIT License. See LICENSE file in the project root for details.
'''

import random

'''
simulation of the wii party minigame "hide-and-peek".
- 3 hiders, 1 seeker. seven spots: 6 legit, 1 joke.
- seeker can look in 5 of the 7 spots to find all 3 hiders. if all are found within 5 searches, seeker wins. if not, hiders win.

two strategies being tested:
- strategy A: all hiders randomly choose among the 6 legit spots (repeats allowed).
- strategy B: one hider deliberately hides in the joke spot; other two randomly choose among the 6 legit spots (repeats allowed).
'''

def main() :

    # ----------------------------------------
    runTrials = False
    nTrials = 10000
    # ----------------------------------------
    runExamples = False
    nExamples = 3
    # ----------------------------------------

    # run trials
    if runTrials :
        print()
        runTrialGames(nTrials)

    # run examples
    if runExamples :
        print()
        runExampleGames("A", nExamples)
        runExampleGames("B", nExamples)

    # if neither are enabled
    if (not runTrials) and (not runExamples) :
        print()
        print("Both set to false; enable something!")
        print()

def runStrategyA(trials : int, returnDetails : bool) -> float :
    '''
    simulate games where all three hiders choose randomly among the 6 legit spots.
    the seeker has 5 searches among those 6 legit spots.
    returns the proportion of games won by the hiders.
    '''
    legitSpots = [0, 1, 2, 3, 4, 5] # legit hiding spots, joke spot 6 unused here
    hiderWins = 0
    details = []

    for i in range(trials) :
        # hiders choose spots randomly (with replacement)
        hiderSpots = []
        for j in range(3) :
            hiderSpots.append(random.choice(legitSpots))

        # seeker chooses 5 unique spots to search among the legit spots
        searchSpots = set()
        while len(searchSpots) < 5 :
            searchSpots.add(random.choice(legitSpots))

        # determine if all hiders have been found
        allFound = True
        for spot in hiderSpots :
            if spot not in searchSpots :
                allFound = False
                break

        # if any hider is not found, the hiders win
        if not allFound :
            hiderWins += 1

        # return individual game details if enabled
        if returnDetails :
            if not allFound :
                winner = "Hiders"
            else :
                winner = "Seeker"
            details.append((hiderSpots, list(searchSpots), winner))

    # return the right thing depending on settings.
    if returnDetails :
        return details
    else :
        return hiderWins / trials

def runStrategyB(trials : int, returnDetails : bool) -> float :
    '''
    simulate games where one hider chooses the joke spot (6) and the other two choose among the 6 legit spots.
    the seeker must still use one search on the joke spot, leaving 4 searches among the 6 legit spots.
    returns the proportion of games won by the hiders.
    '''
    legitSpots = [0, 1, 2, 3, 4, 5] # legit hiding spots
    jokeSpot = 6 # joke spot
    hiderWins = 0
    details = []

    for i in range(trials) :
        # place one hider in the joke spot
        hiderSpots = [jokeSpot]

        # other two hiders choose among legit spots
        for j in range(2) :
            hiderSpots.append(random.choice(legitSpots))

        # seeker search set starts with the joke spot
        searchSpots = {jokeSpot}

        # seeker then chooses 4 unique spots to search among the legit spots
        while len(searchSpots) < 5 :
            searchSpots.add(random.choice(legitSpots))

        # determine if all hiders have been found
        allFound = True
        for spot in hiderSpots :
            if spot not in searchSpots :
                allFound = False
                break

        # if any hider is not found, the hiders win
        if not allFound :
            hiderWins += 1

        # return individual game details if enabled
        if returnDetails :
            if not allFound :
                winner = "Hiders"
            else :
                winner = "Seeker"
            details.append((hiderSpots, list(searchSpots), winner))

    # return the right thing depending on settings.
    if returnDetails :
        return details
    else :
        return hiderWins / trials

def runTrialGames(numTrials : int) :
    '''
    run and display the trial games.
    '''
    hiderWinRateA = runStrategyA(numTrials, False)
    hiderWinRateB = runStrategyB(numTrials, False)
    advantage = abs(hiderWinRateA - hiderWinRateB)
    equal = False
    if hiderWinRateA > hiderWinRateB :
        betterStrat = "Strategy A"
    elif hiderWinRateA == hiderWinRateB :
        equal = True
    else :
        betterStrat = "Strategy B"
    print(f"--- Simulation results ---")
    print(f"{numTrials} trials run for both strategies")
    print()
    print(f"Strategy A hider win percentage: {hiderWinRateA * 100:.2f}%")
    print(f"Strategy B hider win percentage: {hiderWinRateB * 100:.2f}%")
    print()
    if not equal : 
        print(f"Using {betterStrat}, the hiders were {advantage * 100:.2f}% more likely to win this round!")
    else :
        print(f"Strategies A and B gave the hiders equal chances to win this round!")
    print()

def runExampleGames(strategy : str, nExamples : int) :
    '''
    run and display the example games.
    '''
    print(f"-- {nExamples} example games for Strategy {strategy} --")
    if strategy == "A" :
        games = runStrategyA(nExamples, True)
    else :
        games = runStrategyB(nExamples, True)
    for i in range(len(games)) :
        hiderSpots, searchSpots, winner = games[i]
        print(f"Game {i + 1}:")
        print(f"  Hider spots: {hiderSpots}")
        print(f"  Search spots: {searchSpots}")
        print(f"  Winner: {winner}")
        print()

if __name__ == "__main__" :
    main()
