# Name: KERBY JOSEPH
# QCC ID: 24767298
# Course: ET574 - Homework 4
# Assignment: Dice Game Simulator

import random


class Die:
    """Represents a single die."""

    def __init__(self, max_side=6):
        if not isinstance(max_side, int) or max_side < 1:
            raise ValueError("The number of sides must be a positive integer.")

        self.max_side = max_side

    def roll(self):
        """Roll the die and return a random number."""
        return random.randint(1, self.max_side)


class DiceGame:
    """Manages the two-dice game."""

    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def evaluate_roll(self, total):
        """Determine the result based on the dice total."""

        if total < 2 or total > 12:
            raise ValueError("Total must be between 2 and 12.")

        if total == 7 or total == 11:
            return "Win"

        elif total == 2 or total == 3 or total == 12:
            return "Lose"

        else:
            return "Roll Again"

    def play_round(self):
        """Roll both dice and return the results."""

        first_roll = self.die1.roll()
        second_roll = self.die2.roll()

        total = first_roll + second_roll
        result = self.evaluate_roll(total)

        return {
            "die1": first_roll,
            "die2": second_roll,
            "total": total,
            "result": result
        }


def main():
    """Display the game menu."""

    game = DiceGame()

    while True:
        print("\n===== DICE GAME SIMULATOR =====")
        print("1. Play a round")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            result = game.play_round()

            print("\nYou rolled:")
            print("Die 1:", result["die1"])
            print("Die 2:", result["die2"])
            print("Total:", result["total"])
            print("Game Result:", result["result"])

        elif choice == "2":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()