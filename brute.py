import functools
import itertools
import time

from copy import deepcopy
from multiprocessing import Pool

goal = [[1,2,3],
        [4,5,6],
        [7,8,9]]

curr = [[1,2,3],
        [4,8,5],
        [7,9,6]]

curr = [[4,1,3],
        [5,6,9],
        [7,2,8]]

curr = [[1,2,3],
        [4,5,9],
        [7,8,6]]

class Game():

    def __init__(self, init_state):
        self.ops = {0: lambda: self._op(0, 0),
                    1: lambda: self._op(1, 0),
                    2: lambda: self._op(0, 1),
                    3: lambda: self._op(1, 1)}
        self._state = init_state
        self._goal_state = [[1,2,3], [4,5,6], [7,8,9]]

    def __str__(self):
        return '\n'.join([str(line) for line in self._state])

    def __eq__(self, other):
        return self._state == other._state

    def _op(self, x_offset, y_offset):
        self._state[0+y_offset][0+x_offset], \
        self._state[0+y_offset][1+x_offset], \
        self._state[1+y_offset][1+x_offset], \
        self._state[1+y_offset][0+x_offset]\
        = self._state[1+y_offset][0+x_offset], \
        self._state[0+y_offset][0+x_offset], \
        self._state[0+y_offset][1+x_offset], \
        self._state[1+y_offset][1+x_offset]

        return self._state

    @staticmethod
    def mycopy(lst):
        return list(map(list, lst))

    def clone(self):
        return Game(list(map(list, self._state)))

    def completed(self):
        return self._goal_state == self._state

    def move(self, move):
        self.ops[move]()


def do(start_state, l):
    print("start", l)
    prev_time = time.time()
    for sequence in itertools.product(range(4), repeat=l):
        game = Game(start_state)
        game = game.clone()
        for i, step in enumerate(sequence):
            game.move(step)
            if game.completed():
                print (l, "yeah", sequence[:i+1], time.time() - prev_time)
                return sequence[:i+1]
    print("done", l, time.time() - prev_time)

def brute(state):
    do_f = functools.partial(do, state)
    with Pool(3) as p:
        return p.map(do_f, range(10))

if __name__ == '__main__':

    res = brute(curr)

    res_without_none = [r for r in res if r is not None]

    if not res_without_none:
        print("no answer")
    else:
        shortest_len = min(map(len, res_without_none))
        shortest_sequences = [r for r in res_without_none if len(r) == shortest_len]
        print ("best answer", set(shortest_sequences))
