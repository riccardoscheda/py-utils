#!/usr/bin/env python3
# -*- coding: utf-8 -*

import numpy as np
from vpython import box, sphere, vector, color, rate, scene
from physics import simplettic


def build_box(side, thk, s2, s3):
    wallR = box(pos=vector(side, 0, 0), size=vector(thk, s2, s3), color=color.red)
    wallL = box(pos=vector(-side, 0, 0), size=vector(thk, s2, s3), color=color.red)
    wallB = box(pos=vector(0, -side, 0), size=vector(s3, thk, s3), color=color.blue)
    wallT = box(pos=vector(0,  side, 0), size=vector(s3, thk, s3), color=color.blue)
    wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color=color.gray(0.7))


def check_wall_hit(ball: sphere, side: float):
    # Wall hitting check
    if not (side > ball.pos.x > -side):
        ball.v.x = -ball.v.x
    if not (side > ball.pos.y > -side):
        ball.v.y = -ball.v.y
    if not (side > ball.pos.z > -side):
        ball.v.z = -ball.v.z


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
