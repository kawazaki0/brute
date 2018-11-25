from game import Game


class RotateGame(Game):

    def __init__(self, init_state=None):
        super().__init__(init_state)
        self._ops = {0: lambda: self._op(0, 0),
                     1: lambda: self._op(1, 0),
                     2: lambda: self._op(0, 1),
                     3: lambda: self._op(1, 1)}
        self._goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        if init_state is None:
            self._state = list(map(list, self._goal_state))

    def __str__(self):
        return '\n'.join([str(line) for line in self._state])

    def _op(self, x_offset, y_offset):
        self._state[0 + y_offset][0 + x_offset], \
            self._state[0 + y_offset][1 + x_offset], \
            self._state[1 + y_offset][1 + x_offset], \
            self._state[1 + y_offset][0 + x_offset]\
            = self._state[1 + y_offset][0 + x_offset], \
            self._state[0 + y_offset][0 + x_offset], \
            self._state[0 + y_offset][1 + x_offset], \
            self._state[1 + y_offset][1 + x_offset]

        return self._state

    def ops(self):
        return self._ops

    def clone(self):
        return self.__class__(list(map(list, self._state)))

    def completed(self):
        return self._goal_state == self._state

    def move(self, move):
        self.ops()[move]()
