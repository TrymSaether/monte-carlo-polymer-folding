import time
import numpy as np
from intact_Nina import surroundings
from main import rotate_test, create_initial_polymer
from rotate import rotate
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

print(vMatrix(10))


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

        for i in range(N):    
            for j in range(N):
                E[i,j] = 1/2 * vMatrix[i,j] * b
    
    return E


#poly0 = create_initial_polymer(10)
#pol, poly0 = rotate(poly0, (5,5), 1)
#pol, poly0 = rotate(poly0, (4,5), 1)
#print(poly0)


#E = polEnergy(poly0, vMatrix)
 
#print(E)
