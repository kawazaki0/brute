'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Hello World program in Python

from copy import deepcopy

goal = [[1,2,3],
        [4,5,6],
        [7,8,9]]

curr = [[1,2,3],
        [4,8,5],
        [7,9,6]]

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
    changed = deepcopy(state)
    changed[0+y_offset][0+x_offset] = state[1+y_offset][0+x_offset]
    changed[0+y_offset][1+x_offset] = state[0+y_offset][0+x_offset]
    changed[1+y_offset][1+x_offset] = state[0+y_offset][1+x_offset]
    changed[1+y_offset][0+x_offset] = state[1+y_offset][1+x_offset]
    return changed

def op(state, x_offset, y_offset):
    state[0+y_offset][0+x_offset], state[0+y_offset][1+x_offset], state[1+y_offset][1+x_offset], state[1+y_offset][0+x_offset]\
    = state[1+y_offset][0+x_offset], state[0+y_offset][0+x_offset], state[0+y_offset][1+x_offset], state[1+y_offset][1+x_offset]

    return state

ops = {0: op_0,
       1: op_1,
       2: op_2,
       3: op_3}
import time
from itertools import combinations_with_replacement
def brute():
    for l in range(0, 40):
        print(l, time.time())
        # print("x")
        for sequence in combinations_with_replacement(range(4), l):
            curr_table = deepcopy(curr)
            # print("try", sequence)
            for step in sequence:
                curr_table = ops[step](curr_table)
                # print ("step", step)
                # print (curr_table)
                if list(map(tuple, goal)) == list(map(tuple, curr_table)):
                    print ("yeah", sequence)
                    return sequence
print(brute())
