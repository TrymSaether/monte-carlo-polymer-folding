import random
import numpy as np
from rotate import rotate
from is_intact import is_intact
from grafikk import plot
                                          # antall monomerer
def create_initial_polymer(N):

    grid = np.zeros((N,N), dtype=int, order='F')        # to-dimansjonalt grid uten polymer
    grid[int(N/2)] = np.arange(1, N+1)                  # legger inn horisontalt polymer
    return grid


def rotate_test(N, Ns):
    c = 1
    temp_polymer = create_initial_polymer(N)
    for i in range(1, Ns):
        monomer = np.argwhere(temp_polymer > 0)[np.random.randint(1, N)]
        rot = random.randint(0, 1)
        rot_polymer = rotate(temp_polymer,monomer,rot)
        if is_intact(rot_polymer, N):
            c += 1
            temp_polymer = rot_polymer
    plot(temp_polymer, N)
    return temp_polymer, c

polymer, i = rotate_test(100, 50)
plot(polymer, 100)
print(i)