import numpy as np

def is_intact(polymer, N):
    """
    Check if the polymer is intact.

    This method checks if the polymer is intact.
    - It has N monomers
    - Every monomer m has a unique int from 1 to N
    - Every monomer m is neigbour with m - 1 and m + 1, except m = 1 and m = N
    It returns True if the polymer is intact and False otherwise.
    """
    intact = True
    if len(polymer) != N:
        intact = False
    elif len(np.unique(polymer)) != N:
        intact = False
    elif np.any(np.diff(polymer) != 1) and np.any(np.diff(polymer) != -1):
        intact = False
    return intact

def intactPolymer(polymer, N):
    counter = 0
    pol_arr = []
    length = False
    val = False
    pol_len = len(polymer)
    neighbour_1 = False
    neighbour_2 = False
    neighbour_3 = False
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
            return True
        else:
            return False 
        
    except IndexError:
        return False
        
