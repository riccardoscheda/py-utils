#!/usr/bin/env python3
# -*- coding: utf-8 -*

from vpython import vector
from potentials import Potential


def Integrator(object):

    def __init__ (self, name):
        self._name = name

    @staticmethod
    def integrate(p: vector, q: vector, V: Potential, dt: float, *args, **kwargs):
        raise NotImplementedError


def Simplettic(Integrator):

    def __init__ (self):
        super(Simplettic, self).__init__('Simplettic')

    @staticmethod
    def integrate(p: vector, q: vector, V: Potential, dt: float, gamma: vector=vector(0, 0, 0)):

        _, q1 = V.phi(q, p)

        # evolution of the coordinates q and p
        evoq = q + V.phi(q, p + dt * q1)[0] * dt
        # TODO: Unfortunately, gamma can't be a vector since the product
        # between vectors is not implemented
        evop = p - gamma * p * dt + q1 * dt

        return evoq, evop