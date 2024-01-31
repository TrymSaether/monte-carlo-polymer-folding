import time
import numpy as np
from intact_Nina import surroundings
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

vMatrix = v_Matrix(10)


def polEnergy(polymer, vMatrix):


    vectors = np.argwhere(polymer > 0)
    N = len(polymer)
    b = 0
    E = np.zeros((N,N), dtype=int, order='F') 
    
    for monomer in vectors:
        surroundings_arr = surroundings(polymer, monomer)
        y, x = monomer[0], monomer[1]
        val = polymer[y,x]
        vals = []
        vals.append(val)
        
        
        
        if val == 1:
            elements = [2]
        elif val == N:
            elements = [N-1]
        else:
            elements = [val-1, val+1]

        if not all(elem in surroundings_arr for elem in elements): # sjekker naboer
            b = 0
        else:
            b = 1

        for j in range(len(polymer)):
            E[:,j] = 1/2 * vMatrix[:,j] * b
    
    return E

N = 20
polymer, c, t = rotate_test(N, 100)
vMatrix = v_Matrix(N)

E = polEnergy(polymer, vMatrix)
print(E)