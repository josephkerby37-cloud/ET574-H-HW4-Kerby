# ET574-H-HW4-Kerby
ET574 Homework 4 - Dice Game Simulator

# ET574 Homework 4 - Dice Game Simulator

## Project Description

This project is a two-dice game simulator developed using Python.
It uses object-oriented programming and the unittest module.

## Files

- main.py: Contains the Die class, DiceGame class, and main menu.
- test_dicegame.py: Contains unit tests for the dice game.
- README.md: Contains project information and AI usage documentation.

## How to Run the Program

Open the terminal and enter:

    python main.py

## How to Run the Tests

Enter:

    python -m unittest -v test_dicegame

## Game Rules

The game uses two six-sided dice.

- Total of 7 or 11: Win
- Total of 2, 3, or 12: Lose
- Total of 4, 5, 6, 8, 9, or 10: Roll Again

## AI Usage Documentation

AI Tool: ChatGPT by OpenAI.

Purpose:
AI was used to help understand the assignment instructions,
explain Python classes, develop the game structure, and suggest
additional unit test scenarios.

Representative Prompts:
1. Help me create a Python dice game using object-oriented programming.
2. Explain how to use the unittest module in Python.
3. Suggest additional test cases for a two-dice game.
4. Help me understand how to test random dice rolls.

Evaluation and Modifications:
The AI suggestions were reviewed against the assignment requirements.
The code was organized into the required Die and DiceGame classes.
Additional tests were included to check custom dice, winning rounds,
losing rounds, invalid totals, and invalid die sizes.

The student should review the code, understand each method,
and verify the results by running the program and tests.

## Test Case Modifications

The original assignment includes three starter test categories:
1. Die roll boundaries.
2. Outcome evaluation.
3. Play round result structure.

Additional tests were created:

1. Custom die sides:
   Checks whether a die with ten sides can roll a value within its range.

2. Winning round:
   Uses controlled dice values of 4 and 3 to verify a total of 7.

3. Losing round:
   Uses controlled dice values of 1 and 1 to verify a total of 2.

4. Invalid total:
   Checks whether totals outside the possible range raise an error.

5. Invalid die size:
   Checks whether a die with zero sides raises an error.

## Reflection on AI Use

1. AI helped explain the assignment requirements, Python classes,
   and how to organize the game.

2. AI suggested testing custom dice, predictable winning and losing
   rounds, and invalid inputs. These scenarios were adopted.

3. Additional tests were added to check more situations beyond
   the original starter tests.

4. The tests should be verified by running the unittest command
   and checking that all tests pass. The program should also be
   tested manually through the console menu.

5. I learned that unit testing helps identify errors and verify
   that individual parts of a program work correctly. I also
   learned that AI suggestions must be reviewed and tested.

## Author

Name: KERBY JOSEPH

Course: ET574

Assignment: Homework 4 - Dice Game Simulator