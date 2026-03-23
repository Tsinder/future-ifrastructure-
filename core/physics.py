import numpy as np


def lorentz_force(I, L, B):
    return I * L * B


def acceleration(F, m):
    return F / m


def kinetic_energy(m, v):
    return 0.5 * m * v**2


def capacitor_energy(C, V):
    return 0.5 * C * V**2


def power_loss(I, R):
    return I**2 * R
