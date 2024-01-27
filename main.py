import random
import numpy as np
import matplotlib.pyplot as plt
from rotate import rotate
from is_intact import is_intact, intactPolymer
from grafikk import plot

N = 15                                                  # antall monomerer
def create_initial_polymer(N):

    grid = np.zeros((N,N), dtype=int, order='F')        # to-dimansjonalt grid uten polymer
    grid[int(N/2)] = np.arange(1, N+1)                  # legger inn horisontalt polymer
    return grid

def rotate_test(N, Ns):
    i = 1
    temp_polymer = create_initial_polymer(N)
    for i in range(1, Ns):
        monomer = polymer[random.randint(1, N)]
        rot = random.randint(0, 1)
        rot_polymer = rotate(polymer,monomer,bool(rot))
        # if is_intact(rot_polymer, N):
        if intactPolymer(rot_polymer, N):
            i += 1
            temp_polymer = rot_polymer
    return polymer, i

polymer0 = create_initial_polymer(N)
plot(polymer0, N)
print(polymer0)
polymer = rotate(polymer0, (int(N/2), int(N/2)), 1)
plot(polymer, N)
print(is_intact(polymer, N))


