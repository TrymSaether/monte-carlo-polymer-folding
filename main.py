import random
import time
import numpy as np
from rotate import rotate
from intact_Nina import is_intact
from intact_Alisa import intactPolymer
from grafikk import plot
                                          # antall monomerer
def create_initial_polymer(N):

    grid = np.zeros((N,N), dtype=int, order='F')        # to-dimansjonalt grid uten polymer
    grid[int(N/2)] = np.arange(1, N+1)                  # legger inn horisontalt polymer
    return grid

    


def rotate_test(N, Ns):
    start = time.time()
    c = 1
    temp_polymer = create_initial_polymer(N)
    for i in range(1, Ns):
        monomer = np.argwhere(temp_polymer > 0)
        coord = monomer[np.random.randint(0, N)]
        rot = random.randint(0, 1)
        old_polymer, rot_polymer = rotate(temp_polymer,coord,rot)
        
        if is_intact(rot_polymer, N):
            c += 1
            temp_polymer = rot_polymer
        else:
            temp_polymer = old_polymer
    slutt = time.time()
    total_time = slutt-start
    return temp_polymer, c, total_time

polymer, c, time = rotate_test(1000, 33)
print(time)

N, Ns = 1000, 50
polymer, c = rotate_test(N, Ns)
plot(polymer, N)

