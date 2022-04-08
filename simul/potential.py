from vpython import vector


def Potential(object):

    def __init__ (self, name):
        self._name = name

    @staticmethod
    def phi(p: vector, q: vector, *args, **kwargs):
        raise NotImplementedError


def HarmonicOscillator(Potential):

    def __init__ (self):
        super(HarmonicOscillator, self).__init__('Harmonic Oscillator')

    @staticmethod
    def phi(p: vector, q: vector, omega: vector=vector(1.5, 1.5, 1.5)) -> tuple[vector]:

        omega_squared = vector(omega.x ** 2, omega.y ** 2, omega.z ** 2)

        return p, -(q - 2) * omega_squared