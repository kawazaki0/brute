import unittest
from rotate_game import RotateGame

class MoveTest(unittest.TestCase):
  def test_completed(self):
    state = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    game = RotateGame(state)
    self.assertTrue(game.completed())

  def test_first_move(self):
    state = [[2,5,3],
             [1,4,6],
             [7,8,9]]
    game = RotateGame(state)
    game.move(0)
    self.assertTrue(game.completed())

  def test_second_move(self):
    state = [[1,3,6],
             [4,2,5],
             [7,8,9]]
    game = RotateGame(state)
    game.move(1)
    self.assertTrue(game.completed())

  def test_third_move(self):
    state = [[1,2,3],
             [5,8,6],
             [4,7,9]]
    game = RotateGame(state)
    game.move(2)
    self.assertTrue(game.completed())

  def test_fourth_move(self):
    state = [[1,2,3],
             [4,6,9],
             [7,5,8]]
    game = RotateGame(state)
    game.move(3)
    self.assertTrue(game.completed())

  def test_sequence(self):
    state = [[1,2,3],
             [4,5,9],
             [7,8,6]]
    sequence = (2, 3, 1, 2, 2, 2, 1, 1, 1)

    game = RotateGame(state)
    for step in sequence:
        self.assertFalse(game.completed())
        game.move(step)
    self.assertTrue(game.completed())


class GameTest(unittest.TestCase):
  def test_clone(self):
    state = [[1,2,3], [4,5,6], [7,8,9]]
    game = RotateGame(state)

    game2 = game.clone()

    self.assertEqual(game, game2)
    game.move(1)
    self.assertNotEqual(game, game2)
    game2.move(1)
    self.assertEqual(game, game2)


if __name__ == '__main__':
    unittest.main()
