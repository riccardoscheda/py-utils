import numpy as np
from vpython import box, sphere, vector, color, rate, scene
from physics import simplettic

def build_box(side, thk, s2, s3):
    wallR = box(pos=vector(side, 0, 0), size=vector(thk, s2, s3), color=color.red)
    wallL = box(pos=vector(-side, 0, 0), size=vector(thk, s2, s3), color=color.red)
    wallB = box(pos=vector(0, -side, 0), size=vector(s3, thk, s3), color=color.blue)
    wallT = box(pos=vector(0,  side, 0), size=vector(s3, thk, s3), color=color.blue)
    wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color=color.gray(0.7))


def main():

    side = 4.0
    thk = 0.3
    s2 = 2 * side - thk
    s3 = 2 * side + thk
    N = 1

    build_box(side, thk, s2, s3)

    balls = []
    for i in range(N):
        ball = sphere(color=color.green, radius=0.2, make_trail=False)
        ball.mass = 1.
        ball.v = vector(*np.random.uniform(-5, 5, size=3))
       # ball.v = vector(*np.zeros(3))
        balls.append(ball)

    # Change side according to the thickness of the box and radius of the ball
    side = side - thk * 0.5 - ball.radius
    #ball.pos.x=3
    dt = 0.05 # Time step
    while True:

        rate(200) # Halt computation for 1/200s (it's the frequency of the animation)

        for ball in balls:

            ball.pos, ball.v = simplettic(ball.pos, ball.v, dt, gamma=0.05)

            # Wall hitting check
            if not (side > ball.pos.x > -side):
                ball.v.x = -ball.v.x
            if not (side > ball.pos.y > -side):
                ball.v.y = -ball.v.y
            if not (side > ball.pos.z > -side):
                ball.v.z = -ball.v.z

if __name__ == '__main__':
    main()
