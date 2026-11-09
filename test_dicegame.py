# Name: KERBY JOSEPH
# QCC ID: 24767298
# Course: ET574 - Homework 4
# Assignment: Dice Game Unit Tests

import unittest
from unittest.mock import patch

from main import Die, DiceGame


class TestDiceGame(unittest.TestCase):

    # STARTER TEST 1: Check die roll boundaries

    def test_die_roll_bounds(self):
        die = Die()

        for _ in range(100):
            result = die.roll()

            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 6)

    # STARTER TEST 2: Check outcome evaluation

    def test_outcome_evaluation(self):
        game = DiceGame()

        self.assertEqual(game.evaluate_roll(7), "Win")
        self.assertEqual(game.evaluate_roll(11), "Win")

        self.assertEqual(game.evaluate_roll(2), "Lose")
        self.assertEqual(game.evaluate_roll(3), "Lose")
        self.assertEqual(game.evaluate_roll(12), "Lose")

        self.assertEqual(game.evaluate_roll(4), "Roll Again")
        self.assertEqual(game.evaluate_roll(8), "Roll Again")
        self.assertEqual(game.evaluate_roll(10), "Roll Again")

    # STARTER TEST 3: Check play_round structure

    def test_play_round_structure(self):
        game = DiceGame()

        result = game.play_round()

        self.assertIn("die1", result)
        self.assertIn("die2", result)
        self.assertIn("total", result)
        self.assertIn("result", result)

        self.assertEqual(
            result["total"],
            result["die1"] + result["die2"]
        )

    # ADDITIONAL TEST 1: Test a custom-sided die

    def test_custom_die_sides(self):
        die = Die(10)

        with patch("main.random.randint", return_value=9):
            self.assertEqual(die.roll(), 9)

    # ADDITIONAL TEST 2: Test a winning round

    def test_winning_round(self):
        game = DiceGame()

        with patch.object(game.die1, "roll", return_value=4):
            with patch.object(game.die2, "roll", return_value=3):

                result = game.play_round()

        self.assertEqual(result["total"], 7)
        self.assertEqual(result["result"], "Win")

        # ADDITIONAL TEST 3: Test a losing round

    def test_losing_round(self):
        game = DiceGame()

        with patch.object(game.die1, "roll", return_value=1):
            with patch.object(game.die2, "roll", return_value=1):

                result = game.play_round()

        self.assertEqual(result["total"], 2)
        self.assertEqual(result["result"], "Lose")

    # ADDITIONAL TEST 4: Test invalid totals

    def test_invalid_total(self):
        game = DiceGame()

        with self.assertRaises(ValueError):
            game.evaluate_roll(1)

        with self.assertRaises(ValueError):
            game.evaluate_roll(13)

    # ADDITIONAL TEST 5: Test invalid die size

    def test_invalid_die_size(self):
        with self.assertRaises(ValueError):
            Die(0)


if __name__ == "__main__":
    unittest.main()
