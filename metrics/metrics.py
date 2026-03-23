import numpy as np

from core.physics import kinetic_energy


def efficiency(m, v_final, E_input):
    return kinetic_energy(m, v_final) / E_input


def esi(power_series):
    return 1 / np.std(power_series)
