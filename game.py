from copy import deepcopy


class Game():

    def __init__(self, init_state):
        self._state = init_state

    def __eq__(self, other):
        return self._state == other._state

    def clone(self):
        return self.__class__(deepcopy(self._state))

    def ops(self):
        return {0: lambda: self._state}

    def move(self, op):
        self.ops()[op]

    def completed(self):
        return False
