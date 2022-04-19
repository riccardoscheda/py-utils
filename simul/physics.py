#!/usr/bin/env python3
# -*- coding: utf-8 -*

from vpython import vector

def phi(q: vector, p: vector, omega: float = 1.5) -> tuple[vector]:
    """
    The vectorial field which generates the evolution in the pase space
    Parameters:
    ---------------------------------
    q : the generalized coordinate, float
    p : the generalized momenta, float
    omega : frequency, float

    Return the derivative of the potential with respect to q.
    """

    ##################HARMONIC OSCILLATOR
    #    return p , -(q-2)*omega**2

    ################# DOUBLE WELL POTENTIAL
    a = 1.7
    b = 0.7

    return p, -q


def simplettic(q: vector, p: vector, dt: float, gamma: float=0, omega: float=0.5) -> tuple[vector, vector]:
    """
    Simplettic integration method to obtain the evolution of the system
    Parameters:
    ------------------------------------------
    q : the generalized coordinate, float
    dt : the evolution time step, float
    eps : constant which scale the intensity of the white noise csi
    gamma : damping constant (?)

    Returns the evolution of the coordinates q and p

    """

    p1, q1 = phi(q, p)

    # evolution of the coordinates q and p
    evoq = q + phi(q, p + dt * q1)[0] * dt
    evop = p - gamma * p * dt + q1 * dt

    return evoq, evop