#!/usr/bin/env python3
# -*- coding: utf-8 -*

from vpython import vector, box, color, sphere


def build_box(side: float, thk: float, s2: float, s3: float):
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


if __name__ == "__main__":
    pass