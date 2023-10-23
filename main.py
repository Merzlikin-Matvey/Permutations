import numpy as np
from typing import Sequence, Union


class Permutation:
    def __init__(self, data: Union[Sequence[Sequence[Sequence]], Sequence[int]] = None, size: int = None):
        if data is None:
            if size is None:
                raise Exception("Not enough parameters")
            self.size = size
            self.first = np.array(range(1, size + 1))
            self.second = np.array(range(1, size + 1))
        else:
            if isinstance(data, Sequence) and isinstance(data[0], int):
                self.size = len(data)
                self.first = np.array(range(1, self.size + 1))
                self.second = np.array(data)
            else:
                self.size = len(data[0])
                self.first = np.array(data[0])
                self.second = np.array(data[1])

    def __str__(self):
        return ' '.join(list(map(str, self.first))) + '\n' + ' '.join(list(map(str, self.second))) + '\n'

    def __getitem__(self, item):
        return self.second[np.where(self.first == item)][0]

    def image(self, item):
        return self[item]

    def preimage(self, item):
        return self.first[np.where(self.second == item)][0]

    def inv(self, item):
        return self.preimage(item)

    def standard(self, up=True):
        if up:
            self.second = np.array([self[i] for i in range(1, self.size + 1)])
            self.first = np.array(range(1, self.size + 1))
        else:
            self.first = np.array([self.inv(i) for i in range(1, self.size + 1)])
            self.second = np.array(range(1, self.size + 1))



