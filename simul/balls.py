
import numpy as np
from vpython import vector, sphere

# this can be a dataclass, but for now it's ok
class Balls(object):

    def __init__(self, N: int, mass: float = 1.):
        """Create N balls and apply the update rule to them

        Parameters
        ----------
        N : int
            Number of balls to draw
        mass : float, optional
            mass of each ball, by default 1.

        TODO:
        I would like to vectorize the operations with numpy, but maybe there's no way
        """
        self.N = N
        self.mass = mass

        rnd = np.random.uniform

        # Defining all the positions and velocities
        self.pos = np.asarray([vector(rnd(), rnd(), rnd()) for _ in range(N)])
        self.v = np.asarray([vector(rnd(), rnd(), rnd()) for _ in range(N)])
        self.p = self.v * self.mass


    def __repr__(self) -> str:
        return f'Balls: N={self.N}, mass={self.mass}'


    def update_pos(self, dt):
        self.pos = self.pos + self.v * dt


if __name__ == '__main__':
    balls = Balls(N=100)
    print(balls)
    balls.update_pos(dt=0.3)