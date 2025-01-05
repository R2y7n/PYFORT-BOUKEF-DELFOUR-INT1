# PYFORT-BOUKEF-DELFOUR-INT1

## General Presentation

### Project Title
- Fort Boyard Game Project

## Contributors

- __Anaïs Delfour__

- __Rayane Boukef__

## Description

The Fort Boyard Game Project is a Python-based simulation inspired by the 
famous TV show "Fort Boyard." This interactive game allows players to engage in various challenges—logical, chance-based, and mathematical—to unlock the
treasure room and win the game. The project showcases teamwork, strategy, and entertainment.


## Key Features



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

- Python 3.8 or later

- Required libraries:

  - ```random```

  - ```json```

#### Setup

__1. Clone the repository or download the project files.__

__2. Ensure the project structure includes the following:__

- ```project/ |-- main.py |-- utility_functions.py |-- math_challenges.py |-- logical_challenges.py |-- final_challenge.py |-- chance_challenges.py |-- battleship_game.py |-- pere_fouras_challenge.py |-- data/ |-- TRClues.json |-- output/ |-- history.txt```

__3. Install necessary dependencies (if any).__

__4. Run the game using the following command:__

- ```python main.py```

# Technical Documentation

## Game Algorithm

1. __Initialization__: Create a team of players and initialize the game environment.
2. __Challenge Selection__: Randomly select a challenge from the available list.
3. __Challenge Execution__: Execute the selected challenge and evaluate player performance.
4. __Key Collection__: Players attempt to collect 3 keys within 5 challenges.
5. __Treasure Room Access__: Use clues to guess the treasure room’s code word.
6. __Win Condition__: Players win by guessing the correct code word.

## Functions

- __read_file(file_path)__: Reads and returns the content of a file.
  - Parameters: `file_path` (str) - Path to the file.

- __get_max_verse_length(verses)__: Returns the length of the longest verse.
  - Parameters: `verses` (list) - List of verse strings.

- __print_justified(text, n)__: Prints text justified to `n` characters per line.
  - Parameters: `text` (str), `n` (int).

- __prefix_sum(numbers)__: Computes the prefix sum of a list of integers.
  - Parameters: `numbers` (list) - List of integers.

## Input and Error Management

### Input Validation

- Players must input valid names and roles.
- Numbers must be within specified ranges.

### Error Handling

- Handles `FileNotFoundError` when data files are missing.
- Ensures input values are correctly formatted (e.g., integers, non-empty strings).

### Known Bugs

- None currently identified.

## Logbook

### Project Chronology

- __Week 1__: Conceptualization and initial project setup.
- __Week 2__: Development of logical and mathematical challenges.
- __Week 3__: Implementation of treasure room functionality.
- __Week 4__: Final testing, debugging, and documentation.

### Task Distribution

- __Anaïs Delfour__:
  - Developed chance and logical (nim and tictactoe) challenges.
  - Developed main and utility functions
  - Designed père fouras and the treasure room algorithm.

- __Rayane Boukef__:
  - Developed math and battleship functions.
  - Developed main
  - Implemented file handling for game history.

## Testing and Validation

### Test Strategies

- __Unit Tests__: Test individual functions (e.g., `get_max_verse_length`, `prefix_sum`).
- __Integration Tests__: Ensure seamless execution of challenges and game flow.

### Test Cases and Results

- __Case 1__: Validate game initialization with 3 players. Result: __Passed__.
- __Case 2__: Execute a dice roll challenge. Result: __Passed__.
- __Case 3__: Solve a prime number challenge. Result: __Passed__.

### Screenshots

Include screenshots showing:
![Screenshot 2025-01-05 114959.png](Screen%20for%20readme%2FScreenshot%202025-01-05%20114959.png)
![Screenshot 2025-01-05 115059.png](Screen%20for%20readme%2FScreenshot%202025-01-05%20115059.png)
![Screenshot 2025-01-05 115128.png](Screen%20for%20readme%2FScreenshot%202025-01-05%20115128.png)
![Screenshot 2025-01-05 115257.png](Screen%20for%20readme%2FScreenshot%202025-01-05%20115257.png)
![Screenshot 2025-01-05 115308.png](Screen%20for%20readme%2FScreenshot%202025-01-05%20115308.png)
![Screenshot 2025-01-05 115321.png](Screen%20for%20readme%2FScreenshot%202025-01-05%20115321.png)
