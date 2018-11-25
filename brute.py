import functools
import itertools
import time

from copy import deepcopy
from multiprocessing import Pool


def _brute_length(game_cls, start_state, l):
    # print("start", l)
    prev_time = time.time()
    for sequence in itertools.product(range(4), repeat=l):
        game = game_cls(start_state)
        game = game.clone()
        for step in sequence:
            game.move(step)
        if game.completed():
            # print ("yeah", sequence, time.time() - prev_time)
            return sequence
    # print("done", l, time.time() - prev_time)

def brute(game_cls, state, max_length=10, pool_size=3):
    do_f = functools.partial(_brute_length, game_cls, state)
    with Pool(pool_size) as p:
        res = p.map(do_f, range(max_length))

    res_without_none = [r for r in res if r is not None]

    if not res_without_none:
        return None
    else:
        shortest_len = min(map(len, res_without_none))
        shortest_sequence = [r for r in res_without_none if len(r) == shortest_len][0]
        return shortest_sequence


