import random
import numpy as np
from matplotlib import pyplot as plt
from is_intact import is_intact


def rotate(polymer, coord, direction):

    N = len(polymer)
    
    i,j = coord[0], coord[1]
    
    # definerer om rotasjonen skal skje for verdiene over eller under mrot. 

    lower_vals = False

    mrot = polymer[i, j]

    if mrot <= int(N/2):                            # for mrot i midten vil den rotere monomerer med lavere nummer.
        lower_vals = True

    if lower_vals:                                  # lokaliserer monomerer som skal roteres
        vectors = np.argwhere(np.logical_and(polymer > 0, polymer < mrot))           
    else:
        vectors = np.argwhere(polymer > mrot)

    if direction:                                   # lager rotasjonsmatrise, bytter om på x- og y-akse for å passe iterering gjennom 2D-array
        rot_matrix =  np.matrix('0, -1; 1, 0')
    else:
        rot_matrix = np.matrix('0, 1; -1, 0')


    for vector in vectors:
        i , j = vector[0], vector[1]
 
        val = polymer[i,j]
        polymer[i, j] = 0
        rel_coord = (vector - coord)
        rot_rel_coord = np.dot(rot_matrix, rel_coord)
        new_coord = rot_rel_coord + coord
        new_i, new_j = new_coord[0,0], new_coord[0,1]
        polymer[new_i, new_j] = val
        
    return polymer



