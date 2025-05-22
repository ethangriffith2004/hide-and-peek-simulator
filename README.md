# Hide-and-Peek Simulator

A Python script to simulate the Hide-and-Peek minigame in [*Wii Party*](https://en.wikipedia.org/wiki/Wii_Party) and find which strategy is best for the hiding team. Personal project.

## Table of Contents
- [Background](#background)
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Results](#results)
- [Takeaways](#takeaways)
- [Improvements & Extensions](#improvements--extensions)
- [Download & Setup](#download--setup)
- [Contributing](#contributing)
- [License](#license)

## Background

Growing up, I played *Wii Party* with my family religiously. One of the minigames within it, **Hide-and-Peek**, has continued to stick with me. It is a very simple hide-and-seek game.

The mechanics of the game are:
- Three players (hiders) choose between seven spots; more than 1 player can hide in the same spot.
- The remaining player (seeker) can search five of the seven spots; repeated searches are not allowed.
- If the seeker finds all three players within five searches, they win. If they don't, the hiders win.

However:
- Only six of the seven spots are legit.
- One of the spots is a "joke spot", and any hiders who choose it are immediately visible, but the seeker still has to look there to count them as found.

I always thought the "joke spot" was just that: a joke. Though, I eventually came across claims that **intentionally using it could improve the hiders' odds of winning**. I saw nothing to truly back this up, however, so I wanted to find out for myself.

## Project Overview

This project simulates the minigame. The simulation models the game mechanics and calculates the hiders' win probabilities after a set number of trials using two distinct strategies:
- **Strategy A**
  - The three hiders each choose randomly between the six legit spots.
  - The seeker ignores the joke spot.
  - The seeker has five searches to find the three players among six spots.
- **Strategy B**
  - One hider intentionally chooses the joke spot, while the other two each choose randomly between the six legit spots.
  - The seeker searches the joke spot first, finding that hider immediately.
  - The seeker has four searches to find the remaining two players among six spots.

## Technologies Used
- Python 3.x
- Standard libraries

## Results

After running at least 10,000 trials for each strategy, the simulation begins to reliably reveal that **Strategy B** (deliberately choosing the joke spot) increases the hiders' chances of winning by approximately **13.5%**! This gives support to the online claim.

If you would like to test this yourself, keep reading!

## Takeaways

This project:
- Gave me a hands-on way to **explore probability and game theory**, concepts I always found a bit abstract.
- **Strengthened my Python fundamentals**, especially regarding loops, randomness, and writing readable code.
- Emphasized how **intuition can be misleading**, and that what seems like a "wrong" choice can actually provide an advantage.

## Improvements & Extensions

- Simulate more strategies (e.g. two hiders choose joke spot).
- Add a visual or graphical output for results.
- Implement a GUI to allow users to adjust simulation settings without directly modifying the source code.

## Download & Setup

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)

### How to Run
1. Download the simulation code: [`hide_and_peek_simulator.py`](hide_and_peek_simulator.py).
2. Configure the simulation parameters in `main()`.
3. Run the script.

> Running a large number of trials may take a few seconds to complete depending on your system.

### Examples

To run 10,000 trial games of both strategies (and see the estimated probabilities for each), set the parameters in `main()` like this:

```python
runTrials = True
nTrials = 10000
runExamples = False
# nExamples doesn't matter
```

To run 3 example games for each strategy (and see specific results for each), set the parameters in `main()` like this:

```python
runTrials = False
# nTrials doesn't matter
runExamples = True
nExamples = 3
```

## Contributing

- Fork the repo and submit a pull request with any improvements!
- Suggestions or bug reports welcome via email or GitHub issues.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code, provided you include proper credit and retain the license notice.

> © 2025 Ethan Griffith
