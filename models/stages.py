class Stage:
    def __init__(self, name, B, L, discharge_factor):
        self.name = name
        self.B = B
        self.L = L
        self.discharge_factor = discharge_factor


def get_default_stages():
    return [
        Stage("coil", B=0.6, L=0.15, discharge_factor=0.6),
        Stage("induction", B=1.0, L=0.2, discharge_factor=0.7),
        Stage("pulse", B=2.5, L=0.1, discharge_factor=0.5),
    ]
