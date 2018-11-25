import unittest
from brute import brute

from rotate_game import RotateGame


from unittest.mock import MagicMock
# >>> thing = ProductionClass()
# >>> thing.method = MagicMock(return_value=3)
# >>> thing.method(3, 4, 5, key='value')
# 3
# >>> thing.method.assert_called_with(3, 4, 5, key='value')


class BruteTest(unittest.TestCase):

  def test_rotate_game0(self):
    res = brute(RotateGame, state=[[1,2,3], [4,5,6], [7,8,9]])
    self.assertEqual((), res)

  def test_rotate_game2(self):
    res = brute(RotateGame, state=[[3, 8, 6], [2, 4, 9], [1, 5, 7]])
    self.assertEqual((0, 3, 1, 2, 0), res)


if __name__ == '__main__':
    unittest.main()
