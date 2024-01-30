import random
import time
import numpy as np
from rotate import rotate
from is_intact import is_intact
from grafikk import plot
                                          # antall monomerer
def create_initial_polymer(N):

    grid = np.zeros((N,N), dtype=int, order='F')        # to-dimansjonalt grid uten polymer
    grid[int(N/2)] = np.arange(1, N+1)                  # legger inn horisontalt polymer
    return grid


def intactPolymer(polymer, N):
    counter = 0
    pol_arr = []
    length = False
    val = False
    pol_len = len(polymer)
    neighbour_1 = False
    neighbour_2 = False
    neighbour_3 = False
    start = time.time()
    try:
        for i in range(pol_len):
            for j in range(pol_len):
                if polymer[i,j] != 0:
                    counter += 1
                    
                    pol_arr.append(polymer[i,j])

                    if polymer[i,j] == 1:
                        if (polymer[i - 1,j] == 2 or polymer[i + 1,j] == 2 or 
                        polymer[i,j - 1] == 2 or polymer[i,j + 1] == 2):
                            neighbour_1 = True

                    elif polymer[i,j] == N:
                            if (polymer[i - 1,j] == N-1 or polymer[i + 1,j] == N-1 or 
                            polymer[i,j - 1] == N-1 or polymer[i,j + 1] == N-1):
                                neighbour_2 = True
                    
                    else:
                        if (polymer[i,j] == 1 + polymer[i - 1,j] or polymer[i,j] == 1 + polymer[i + 1,j] or 
                        polymer[i,j] == 1 + polymer[i,j - 1] or polymer[i,j] == 1 + polymer[i,j + 1]) and (polymer[i,j] == -1 + polymer[i - 1,j] or polymer[i,j] == -1 + polymer[i + 1,j] or 
                        polymer[i,j] == -1 + polymer[i,j - 1] or polymer[i,j] == -1 + polymer[i,j + 1]):
                            neighbour_3 = True
                
        if counter == N:
            length = True

        
        delete_arr = set(pol_arr)
        if len(delete_arr) == len(pol_arr):
            val = True
                

        if (length and val and neighbour_1 and neighbour_2 and neighbour_3):
            print(f'Time used for a simple for-loop:  {time.time()-start:.2e} seconds')
            return True
            
        else:
            print(f'Time used for a simple for-loop:  {time.time()-start:.2e} seconds')
            return False 
            
            
        
    except IndexError:
        return False
    


def rotate_test(N, Ns):
    c = 1
    temp_polymer = create_initial_polymer(N)
    for i in range(1, Ns):
        monomer = np.argwhere(temp_polymer > 0)
        coord = monomer[np.random.randint(0, N)]
        rot = random.randint(0, 1)
        old_polymer, rot_polymer = rotate(temp_polymer,coord,rot)
        
        if intactPolymer(rot_polymer, N):
            c += 1
            temp_polymer = rot_polymer
        else:
            temp_polymer = old_polymer
    plot(temp_polymer, N)
    return temp_polymer, c

polymer, c = rotate_test(100, 21)
#plot(polymer, 100)
print(c)

