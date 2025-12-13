'''
Copyright (c) 2025 Ethan Griffith
Licensed under the MIT License. See LICENSE file for details.
'''

import random

'''
simulation of the wii party minigame "hide-and-peek"
- 3 hiders, 1 seeker
- 7 spots: 6 legit, 1 joke
- seeker can look in 5 of the 7 spots to find all 3 hiders
- if all are found within 5 searches, seeker wins
- if not, hiders win

3 strategies being tested:
- strategy A: all hiders randomly choose among the 6 legit spots (repeats allowed)
- strategy B: one hider deliberately hides in the joke spot; other two randomly choose among the 6 legit spots (repeats allowed)
- strategy C: two hiders deliberately hide in the joke spot; remaining hider randomly chooses among the 6 legit spots
'''

def main() :

    # ---------------------
    # simulation parameters
    # ---------------------
    runTrials = True
    nTrials = 100000
    # ---------------------
    runExamples = True
    nExamples = 3
    # ---------------------

    # run trials
    if runTrials :
        print()
        runTrialGames(nTrials)

    # run examples
    if runExamples :
        print()
        runExampleGames("A", nExamples)
        runExampleGames("B", nExamples)
        runExampleGames("C", nExamples)

    # if neither are enabled
    if (not runTrials) and (not runExamples) :
        print()
        print("Both set to false; enable something!")
        print()

def runStrategyA(trials : int, returnDetails : bool) :

    '''
    simulate games where all three hiders choose randomly among the 6 legit spots (0-5)
    the seeker has 5 searches among those 6 legit spots.
    '''

    legitSpots = [0, 1, 2, 3, 4, 5] # legit hiding spots, joke spot (6) unused here
    hiderWins = 0
    details = []

    for i in range(trials) :
        # hiders choose spots randomly (with replacement)
        hiderSpots = []
        for j in range(3) :
            hiderSpots.append(random.choice(legitSpots))

        # seeker chooses 5 unique spots to search among the legit spots
        # use a set for faster lookup time
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

        # set up returning individual game details, if enabled
        if returnDetails :
            if not allFound :
                winner = "Hiders"
            else :
                winner = "Seeker"
            details.append((hiderSpots, list(searchSpots), winner))

    # return the right thing
    if returnDetails :
        return details
    else :
        return hiderWins / trials

def runStrategyB(trials : int, returnDetails : bool) :

    '''
    simulate games where one hider chooses the joke spot (6) and the other two choose among the 6 legit spots (0-5).
    the seeker must still use one search on the joke spot, leaving 4 searches among the 6 legit spots.
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

        # all other logic is the same
        allFound = True
        for spot in hiderSpots :
            if spot not in searchSpots :
                allFound = False
                break

        if not allFound :
            hiderWins += 1

        if returnDetails :
            if not allFound :
                winner = "Hiders"
            else :
                winner = "Seeker"
            details.append((hiderSpots, list(searchSpots), winner))

    if returnDetails :
        return details
    else :
        return hiderWins / trials

def runStrategyC(trials : int, returnDetails : bool) :

    '''
    simulate games where two hiders choose the joke spot (6) and the remaining hider chooses among the 6 legit spots (0-5).
    the seeker must still use one search on the joke spot, leaving 4 searches among the 6 legit spots.
    '''

    legitSpots = [0, 1, 2, 3, 4, 5] # legit hiding spots
    jokeSpot = 6 # joke spot
    hiderWins = 0
    details = []

    for i in range(trials) :
        # place two hiders in the joke spot
        hiderSpots = [jokeSpot, jokeSpot]

        # remaining hider chooses among legit spots
        hiderSpots.append(random.choice(legitSpots))

        # seeker search set starts with the joke spot
        searchSpots = {jokeSpot}

        # seeker then chooses 4 unique spots to search among the legit spots
        while len(searchSpots) < 5 :
            searchSpots.add(random.choice(legitSpots))

        # all other logic is the same
        allFound = True
        for spot in hiderSpots :
            if spot not in searchSpots :
                allFound = False
                break

        if not allFound :
            hiderWins += 1

        if returnDetails :
            if not allFound :
                winner = "Hiders"
            else :
                winner = "Seeker"
            details.append((hiderSpots, list(searchSpots), winner))

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
    hiderWinRateC = runStrategyC(numTrials, False)
    
    print(f"--- Simulation results ---")
    print(f"{numTrials} trials run for all strategies")
    print()
    print(f"Strategy A hider win percentage: {hiderWinRateA * 100:.2f}%")
    print(f"Strategy B hider win percentage: {hiderWinRateB * 100:.2f}%")
    print(f"Strategy C hider win percentage: {hiderWinRateC * 100:.2f}%")
    print()
    
    # determine best strategy
    bestStrat = "Strategy A"
    bestRate = hiderWinRateA
    if hiderWinRateB > bestRate :
        bestStrat = "Strategy B"
        bestRate = hiderWinRateB
    if hiderWinRateC > bestRate :
        bestStrat = "Strategy C"
        bestRate = hiderWinRateC
    
    print(f"Best strategy: {bestStrat} with {bestRate * 100:.2f}% hider win rate")
    print()

def runExampleGames(strategy : str, nExamples : int) :

    '''
    run and display the example games.
    '''
    
    print(f"-- {nExamples} example games for Strategy {strategy} --")
    if strategy == "A" :
        games = runStrategyA(nExamples, True)
    elif strategy == "B" :
        games = runStrategyB(nExamples, True)
    else :
        games = runStrategyC(nExamples, True)
    
    for i in range(len(games)) :
        hiderSpots, searchSpots, winner = games[i]
        print(f"Game {i + 1}:")
        print(f"  Hider spots: {hiderSpots}")
        print(f"  Search spots: {searchSpots}")
        print(f"  Winner: {winner}")
        print()

if __name__ == "__main__" :
    main()