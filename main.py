from brute import brute_async as brute
from rotate_game import RotateGame


if __name__ == '__main__':
    curr = [[1, 2, 3],
            [4, 5, 9],
            [7, 8, 6]]
    res = brute(RotateGame, curr, pool_size=2)
    print(res)
