#!/usr/bin/env python3
# -*- coding: utf-8 -*

import numpy as np
from vpython import sphere, vector, color, rate

from utils import build_box, check_wall_hit


def create_balls(N: int=1, r: float=.2) -> list[sphere]:

    balls = []
    for i in range(N):
        ball = sphere(color=color.green, radius=r, make_trail=False, pos=vector.random()*2)
        ball.mass = 1.
        ball.v = vector.random() * .1
        balls.append(ball)

    return balls


def main():

    side = 4.0
    thk = 0.3
    s2 = 2 * side - thk
    s3 = 2 * side + thk

    N = 50
    r = 0.2

    build_box(side, thk, s2, s3)
    balls = create_balls(N)

    # Change side according to the thickness of the box and radius of the ball
    side = side - thk * 0.5 - r

    # Animation loops
    dt = 0.05
    while True:

        rate(200) # Halt computation for 1/200s (it's the frequency of the animation)

        for i, ball in enumerate(balls):

            ball.pos = ball.pos + ball.v * dt
            ball.v = ball.v
            check_wall_hit(ball, side)

            # Check ball hitting
            for ball2 in balls:
                if not (ball is ball2):
                    dpos = ball.pos - ball2.pos
                    dpos_mag = dpos.mag
                    if dpos_mag <= r:

                        # source: https://introcs.cs.princeton.edu/java/assignments/collisions.html
                        dv = ball.v - ball2.v
                        J = 2 * dv.dot(dpos)
                        Jv = J * dpos / (dpos_mag * 2)

                        ball.v = ball.v + Jv

                    else:
                        pass



if __name__ == '__main__':
    main()
