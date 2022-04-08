
from dataclasses import dataclass, field

import numpy as np
from vpython import vector, sphere, color


@dataclass
class Balls(object):
    N: int
    mass: int = 1.

    def __post_init__(self):
        self.balls = [sphere(pos=(1, 1, 1),color=color.green, radius=0.2) for _ in range(self.N)]


if __name__ == '__main__':
    balls = Balls(N=100)
    print(balls)