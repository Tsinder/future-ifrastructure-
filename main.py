from core.physics import capacitor_energy
from metrics.metrics import efficiency, esi
from models.system import HybridSystem
from simulation.run import simulate
from visualization.plots import plot_all

params = {
    "mass": 0.1,
    "resistance": 0.5,
    "capacitance": 0.02,
    "voltage": 120,
    "dt": 1e-4,
    "t_max": 0.02,
}

system = HybridSystem()

time, velocity, current, loss, power = simulate(system, params)

E_input = capacitor_energy(params["capacitance"], params["voltage"])

eta = efficiency(params["mass"], velocity[-1], E_input)
esi_value = esi(power)

print("Efficiency:", eta)
print("ESI:", esi_value)

plot_all(time, velocity, current, loss, "Hybrid")
