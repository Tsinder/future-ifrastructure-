import numpy as np

from core.physics import acceleration, lorentz_force, power_loss


def simulate(system, params):
    m = params["mass"]
    R = params["resistance"]
    C = params["capacitance"]
    V = params["voltage"]

    dt = params["dt"]
    time = np.arange(0, params["t_max"], dt)

    v = 0
    velocity = []
    current = []
    loss = []
    power = []

    E_loss = 0

    for t in time:
        stage = system.get_stage(t)

        I = V / R
        F = lorentz_force(I, stage.L, stage.B)
        a = acceleration(F, m)

        v += a * dt

        P = power_loss(I, R)
        E_loss += P * dt

        V -= (stage.discharge_factor * I * dt) / C

        velocity.append(v)
        current.append(I)
        loss.append(E_loss)
        power.append(P)

    return time, velocity, current, loss, power
