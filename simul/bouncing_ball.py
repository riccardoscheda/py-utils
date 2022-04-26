#!/usr/bin/env python3
# -*- coding: utf-8 -*

import numpy as np
from vpython import box, sphere, vector, color, rate, scene

from physics import simplettic
from utils import build_box, check_wall_hit


def create_balls(N: int=1) -> list:

    balls = []
    for i in range(N):
        ball = sphere(color=color.green, radius=0.2, make_trail=False)
        ball.mass = 1.
        ball.v = vector(*np.random.uniform(-5, 5, size=3))
        balls.append(ball)

    return balls

def main():

    side = 4.0
    thk = 0.3
    s2 = 2 * side - thk
    s3 = 2 * side + thk
    N = 1

    build_box(side, thk, s2, s3)
    balls = create_balls(N)

    # Change side according to the thickness of the box and radius of the ball
    side = side - thk * 0.5 - ball.radius

    # Animation loops
    dt = 0.05
    while True:

        rate(200) # Halt computation for 1/200s (it's the frequency of the animation)

        for ball in balls:

            ball.pos, ball.v = simplettic(ball.pos, ball.v, dt, gamma=0.05)
            check_wall_hit(ball, side)


if __name__ == '__main__':
    main()
