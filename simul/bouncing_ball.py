from vpython import box, sphere, vector, color, rate, scene


def build_box(side, thk, s2, s3):
    wallR = box(pos=vector( side, 0, 0), size=vector(thk, s2, s3), color=color.red)
    wallL = box(pos=vector(-side, 0, 0), size=vector(thk, s2, s3), color=color.red)
    wallB = box(pos=vector(0, -side, 0), size=vector(s3, thk, s3), color=color.blue)
    wallT = box(pos=vector(0,  side, 0), size=vector(s3, thk, s3), color=color.blue)
    wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color=color.gray(0.7))


def main():

    scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
    To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
    On a two-button mouse, middle is left + right.
    To pan left/right and up/down, Shift-drag.
    Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

    side = 4.0
    thk = 0.3
    s2 = 2 * side - thk
    s3 = 2 * side + thk

    build_box(side, thk, s2, s3)

    # Ball creation with mass and momentum
    ball = sphere(color=color.green, radius=0.2, make_trail=False)
    ball.mass = 1.0
    ball.p = vector(-0.15, -0.23, +0.27)

    # Change side according to the thickness of the box
    side = side - thk * 0.5 - ball.radius

    dt = 0.3 # Time step
    while True:

        rate(200) # Halt computation for 1/200s (it's the frequency of the animation)

        # Equation
        ball.pos = ball.pos + (ball.p / ball.mass) * dt

        # Wall hitting check
        if not (side > ball.pos.x > -side):
            ball.p.x = -ball.p.x
        if not (side > ball.pos.y > -side):
            ball.p.y = -ball.p.y
        if not (side > ball.pos.z > -side):
            ball.p.z = -ball.p.z


if __name__ == '__main__':
    main()
