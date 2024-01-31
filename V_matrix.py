import time
import numpy as np
from intact_Nina import surroundings_chatgpt
from main import rotate_test, create_initial_polymer
from rotate import rotate
from grafikk import plot


def v_Matrix(N):
    grid = np.zeros((N,N), dtype=int, order='F')
    for i in range(N):
        for j in range(N):
            if i == j:
                grid[i,j] = 0
            elif i == j + 1:
                grid[i,j+1] = 0
            elif i + 1 == j:
                grid[i + 1, j] = 0
            else:
                grid[i,j] = -1
    return grid


def polEnergy(polymer, vMatrix):


    vectors = np.argwhere(polymer > 0)
    N = len(polymer)
    E = 0

    for monomer in vectors:
        surroundings_arr = surroundings_chatgpt(polymer, monomer)
        y, x = monomer[0], monomer[1]
        val = polymer[y,x]

        for i in range(N):
            m = val
            n = i+1

            if n in surroundings_arr:
                print(val, n)
                b = 1
                E += 1/2 * vMatrix[m-1,i]
            else:
                b = 0

            # E += 1/2 * vMatrix[m-1,i] * b
    
    return E

N = 20
Ns = 100
polymer, c, t = rotate_test(N, Ns)
vMatrix = v_Matrix(N)
print(vMatrix)
print(polymer)
E = polEnergy(polymer, vMatrix)
print(E)