import random
import numpy as np
import matplotlib.pyplot as plt
from rotate import rotate, rotate_test
from is_intact import is_intact
from grafikk import plot

N = 15                                                  # antall monomerer
def create_initial_polymer(N):

    grid = np.zeros((N,N), dtype=int, order='F')        # to-dimansjonalt grid uten polymer
    grid[int(N/2)] = np.arange(1, N+1)                  # legger inn horisontalt polymer
    return grid

polymer0 = create_initial_polymer(N)
plot(polymer0, N)
print(polymer0)
polymer = rotate(polymer0, (int(N/2), int(N/2)), 1)
plot(polymer, N)

print(is_intact(polymer, N))


