# PYFORT-BOUKEF-DELFOUR-INT1


## Introduction

Welcome to the __Fort Boyard Game Project__, a Python-based simulation inspired by the famous TV show __"Fort Boyard."__ This project offers an engaging and interactive experience where players face challenges of logic, chance, mathematics, and strategy to unlock the treasure room.

The game accommodates 1 to 3 players who work as a team to overcome various obstacles and ultimately claim the treasure. With multiple challenge types and dynamic gameplay, this project showcases the collaborative and competitive spirit of Fort Boyard.

## Features

### Player Team Management

 - Create and manage a team of up to 3 players.

 - Assign roles and track performance during the game.

### Variety of Challenges

- __Logical challenges__ (e.g., Nim Game, Tic-Tac-Toe).

- __Chance-based challenges__ (e.g., Shell Game, Dice Roll).

- __Mathematical challenges__ (e.g., solving equations, identifying prime numbers).

- __Treasure room final challenge.__

### Dynamic Gameplay

- Randomized challenge selection.

- Strategic decision-making and resource management.

### Game History

- Save detailed game progress and outcomes for future reference.

## Installation

### Prerequisites

- Python 3.12 or later

- Required libraries:

- ``` random```

- ```json```

#### Setup

__1. Clone the repository or download the project files.__

__2. Ensure the project structure includes the following:__
```
project/
|-- main.py
|-- utility_functions.py
|-- math_challenges.py
|-- logical_challenges.py
|-- final_challenge.py
|-- chance_challenges.py
|-- battleship_game.py
|-- pere_fouras_challenge.py
|-- data/
    |-- TRClues.json
|-- output/
    |-- history.txt 
```

__3. Install necessary dependencies (if any).__

__4. Run the game using the following command:__

```python main.py```

## How to Play

__1. Launch the game by running main.py.__

__2. Follow the on-screen prompts to:__

- Set the number of players.

- Assign names and roles to each player.

__3. Participate in a series of challenges:__

- Logical games like Nim, Tic-Tac-Toe, or Battleship.

- Chance-based games like Shell Game or Dice Roll.

- Mathematical problems or puzzles.

__4. Collect 3 keys within 5 attempts to gain access to the treasure room.__

__5. Use clues to guess the treasure room's code word and win the treasure.__

## Project Structure

### Core Files

- __main.py:__ Centralizes game actions and manages the main game loop.

  - __utility_functions.py:__ Provides utility functions for team composition, challenge selection, and game history recording.

  - __math_challenges.py:__ Implements various mathematical challenges, including solving equations and prime number identification.

  - __logical_challenges.py:__ Contains logic-based games like Nim and Tic-Tac-Toe.

  - __chance_challenges.py:__ Handles chance-based games like Shell Game and Dice Roll.

  - __final_challenge.py:__ Manages the final treasure room challenge, including guessing the code word.

  - __battleship_game.py:__ Implements the Battleship game.

  - __pere_fouras_challenge.py__: Placeholder for additional challenges (e.g., riddles).

### Supporting Files

-   __data/TRClues.json__: Contains the clues and code words for the treasure room.

  - __output/history.txt__: Logs game outcomes and player performance.

## __Game Rules__

### __General Rules__

-   Players must collect 3 keys to access the treasure room.

  - Each player can attempt a variety of challenges, with the outcomes affecting overall progress.

### Specific Challenges

1. __Logical Challenges:__

   - __Nim Game__: Players alternate removing sticks; the last to remove a stick loses.

     - __Tic-Tac-Toe__: Line up three symbols to win.

       - __Battleship__: Sink all opponent boats to win.

2. __Chance Challenges:__

   - __Shell Game__: Guess under which shell the key is hidden.

     - __Dice Roll__: Roll a 6 to win before the master does.

3. __Mathematical Challenges:__

   - __Solve linear equations, factorial problems, or identify prime numbers.__

4. __Treasure Room:__

   - __Use collected clues to guess the treasure room’s code word within 3 attempts.__

## Contributors

- __Anaïs Delfour__

- __Rayane Boukef__

### Future Improvements

- Add more diverse challenges (e.g., riddles, memory games).

- Enhance the game’s user interface with graphics.

- Allow online multiplayer mode.

- Include a scoring system to rank player performance.

#### Thank you for playing the Fort Boyard Game Project! Enjoy the adventure!

