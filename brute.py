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

# curr = [[1,2,3],
#         [4,5,9],
#         [7,8,6]]

class Game():

    def __init__(self, init_state):
        self.ops = {0: self.op_0,
                    1: self.op_1,
                    2: self.op_2,
                    3: self.op_3}
        self.state = self.mycopy(init_state)
        self.goal_state = [[1,2,3], [4,5,6], [7,8,9]]

    def __str__(self):
        return '\n'.join([str(line) for line in self.state])

    def op_0(self):
        return self._op(0, 0)
    def op_1(self):
        return self._op(1, 0)
    def op_2(self):
        return self._op(1, 1)
    def op_3(self):
        return self._op(1, 1)

    def _op(self, x_offset, y_offset):
        self.state[0+y_offset][0+x_offset], self.state[0+y_offset][1+x_offset], self.state[1+y_offset][1+x_offset], self.state[1+y_offset][0+x_offset]\
        = self.state[1+y_offset][0+x_offset], self.state[0+y_offset][0+x_offset], self.state[0+y_offset][1+x_offset], self.state[1+y_offset][1+x_offset]

        return self.state

    @staticmethod
    def mycopy(lst):
        return list(map(list, lst))

    def completed(self):
        return self.goal_state == self.state

    def move(self, move):
        self.ops[move]()


a = [[1,2],]
b = Game.mycopy(a)
b[0][0] = 4
assert a != b


def test():

    def pprint_game(g):
        print(g)
        print ("---")

    g = Game([[1,2,3],
             [4,5,9],
             [7,8,6]])

    s = (0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2)

    for ss in s:
        pprint_game(g)
        print(ss)
        g.move(ss)

    pprint_game(g)

    if not g.completed():
        raise Exception()


test()

def do(start_state, l):
    print("start", l)
    prev_time = time.time()
    for sequence in itertools.product(range(4), repeat=l):
        game = Game(start_state)
        for i, step in enumerate(sequence):
            game.move(step)
            if game.completed():
                print (l, "yeah", sequence[:i+1], time.time() - prev_time)
                return sequence[:i+1]
    print("done", l, time.time() - prev_time)

def brute(curr):
    do_f = functools.partial(do, curr)
    with Pool(3) as p:
        return p.map(do_f, range(10))

res = brute(curr)

res_without_none = [r for r in res if r is not None]

if not res_without_none:
    print("no answer")
else:
    shortest_len = min(map(len, res_without_none))
    shortest_sequences = [r for r in res_without_none if len(r) == shortest_len]
    print ("best answer", set(shortest_sequences))
