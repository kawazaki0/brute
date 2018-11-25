from unittest import TestCase
from unittest.mock import MagicMock

from brute import brute_async, brute_sync
from rotate_game import RotateGame


class BruteTest(TestCase):

    def test_async_simple(self):
        res = brute_async(RotateGame, init_state=[[1,2,3], [4,5,6], [7,8,9]])
        self.assertEqual((), res)

    def test_async_complex(self):
        res = brute_async(RotateGame, init_state=[[3, 8, 6], [2, 4, 9], [1, 5, 7]])
        self.assertEqual((0, 3, 1, 2, 0), res)

    def test_sync_simple(self):
        res = brute_sync(RotateGame, init_state=[[1,2,3], [4,5,6], [7,8,9]])
        self.assertEqual((), res)

    def test_sync_complex(self):
        res = brute_sync(RotateGame, init_state=[[3, 8, 6], [2, 4, 9], [1, 5, 7]])
        self.assertEqual((0, 3, 1, 2, 0), res)


if __name__ == '__main__':
        unittest.main()
