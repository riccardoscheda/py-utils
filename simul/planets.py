#!/usr/bin/env python3
# -*- coding: utf-8 -*

from vpython import sphere, vector, color, rate

from physics import gravity


def main():

    G = .1

    # Create a "sun", a firm object.
    sun = sphere(pos=vector(0, 0, 0), radius=1., mass=100, color=color.yellow)

    # Create the planet in the solar system
    planet = sphere(pos=vector(0, 6., 0),
                    radius=0.2,
                    mass=1,
                    color=color.blue,
                    make_trail=True, retain=300)
    planet.v = vector(1., 0., 0.)

    # Animation loops
    dt = 0.05
    while True:
        rate(200)  # Halt computation for 1/200s (it's the frequency of the animation)

        g = gravity(planet, sun, G) / planet.mass

        # Update position and velocity of the planet
        planet.pos = planet.pos + planet.v * dt + g / 2 * dt ** 2
        planet.v = planet.v + g * dt


if __name__ == '__main__':
    main()
