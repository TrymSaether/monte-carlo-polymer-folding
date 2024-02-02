import random
import numpy as np
from V_matrix import polEnergy
from intact_Nina import is_intact
from rotate import rotate

# Konstanter


def metropolis(polymer, V, Ns, T, beta = 1):
    N = len(polymer)
    E_array = np.zeros(Ns, dtype=int)
    E = polEnergy(polymer, V)
    i = 1
    while i < Ns:
        monomer = np.argwhere(polymer > 0)
        coord = monomer[np.random.randint(0, N)]
        dir = random.randint(0, 1)
        polymer, rot_polymer = rotate(polymer,coord, dir)
        if is_intact(rot_polymer, N):
            i += 1
            E_new = polEnergy(polymer,V)
            if E_new < E:
                polymer = rot_polymer
                E = E_new
            elif np.random.random() < np.exp(-beta*(E_new - E)):
                polymer = rot_polymer
                E = E_new
            E_array[i] = E
    return E_array

            