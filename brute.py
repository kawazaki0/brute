import functools
import itertools
import time

from copy import deepcopy
from multiprocessing import Pool
import multiprocessing


def _brute_length(game_cls, start_state, l):
    # print(" " * (l) + "*", l)
    prev_time = time.time()
    for sequence in itertools.product(range(4), repeat=l):
        game = game_cls(start_state)
        game = game.clone()
        for step in sequence:
            game.move(step)
        if game.completed():
            # print("yeah", sequence, time.time() - prev_time)
            return sequence
    # print("done", l, time.time() - prev_time)
    # print(" "*(l) + "*")


def brute_sync(game_cls, init_state, max_length=15):
    do_f = functools.partial(_brute_length, game_cls, init_state)
    for l in range(max_length):
        r = do_f(l)
        if r is not None:
            return r
    return None


def brute_async(game_cls, init_state, max_length=15, pool_size=3):
    do_f = functools.partial(_brute_length, game_cls, init_state)
    processes = []
    with Pool(processes=pool_size) as pool:         # start 4 worker processes
        for l in range(max_length):
            processes.append(pool.apply_async(do_f, (l,)))

        for i, p in enumerate(processes):
            r = p.get()
            # print("*" * i)
            if r is not None:
                return r
    return None
