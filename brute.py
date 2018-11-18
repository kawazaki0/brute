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

def op_0(state):
    return op(state, 0, 0)
def op_1(state):
    return op(state, 1, 0)
def op_2(state):
    return op(state, 1, 1)
def op_3(state):
    return op(state, 1, 1)


def op(state, x_offset, y_offset):
    state[0+y_offset][0+x_offset], state[0+y_offset][1+x_offset], state[1+y_offset][1+x_offset], state[1+y_offset][0+x_offset]\
    = state[1+y_offset][0+x_offset], state[0+y_offset][0+x_offset], state[0+y_offset][1+x_offset], state[1+y_offset][1+x_offset]

    return state

ops = {0: op_0,
       1: op_1,
       2: op_2,
       3: op_3}


def mycopy(lst):
    return list(map(list, lst))

a = [[1,2],]
b = mycopy(a)
b[0][0] = 4
assert a != b


def test():
    s = (0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2)

    def pprint(obj):
        for elem in obj:
            print(elem)
        print ("---")
    t = curr

    for ss in s:
        pprint(t)
        print(ss)
        t = mycopy(t)
        t = ops[ss](t)

    pprint(t)

    raise Exception()


# test()

def do(l):
    print("start", l)
    prev_time = time.time()
    for sequence in itertools.product(range(4), repeat=l):
        curr_table = mycopy(curr)
        for i, step in enumerate(sequence):
            curr_table = ops[step](curr_table)
            if goal == curr_table:
                print (l, "yeah", sequence[:i+1], time.time() - prev_time)
                return sequence[:i+1]
    print("done", l, time.time() - prev_time)

def brute():
    with Pool(3) as p:
        return p.map(do, range(14,15))

res = brute()

res_without_none = [r for r in res if r is not None]

if not res_without_none:
    print("no answer")
else:
    shortest_len = min(map(len, res_without_none))
    shortest_sequences = [r for r in res_without_none if len(r) == shortest_len]
    print ("best answer", set(shortest_sequences))
