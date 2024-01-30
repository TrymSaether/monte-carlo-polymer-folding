import numpy as np

def create_initial_polymer(N):

    grid = np.zeros((N,N), dtype=int, order='F')        # to-dimansjonalt grid uten polymer
    grid[int(N/2)] = np.arange(1, N+1)                  # legger inn horisontalt polymer
    return grid

# ikke så nice, men skrevet av meg:

def surroundings(polymer, monomer):  # definerer verdier over, under, til venstre og høyre
    
    surroundings = np.zeros(4)

    try: 
        up = monomer+np.array([-1, 0])
        y,x = up[0], up[1]
        up_val = polymer[y,x]
        surroundings[0] = up_val
    except:
        pass

    try:
        down = monomer + np.array([1, 0])
        y,x = down[0], down[1]
        down_val = polymer[y,x]
        surroundings[1] = down_val
    except IndexError:
        pass

    try:
        left = monomer + np.array([0, -1])
        y,x = left[0], left[1]
        left_val = polymer[y,x]
        surroundings[2] = left_val
    except IndexError:
        pass

    try:
        right = monomer + np.array([0, 1])
        y,x = right[0], right[1]
        right_val = polymer[y,x]
        surroundings[3] = right_val
    except IndexError:
        pass
  

    return surroundings
"""
# sykt nice men skrevet av ChatGPT:

def surroundings(polymer, monomer):
    y, x = monomer
    max_y, max_x = polymer.shape
    surrounding_values = []

    if y > 0:
        surrounding_values.append(polymer[y-1, x])  # Up
    if y < max_y - 1:
        surrounding_values.append(polymer[y+1, x])  # Down
    if x > 0:
        surrounding_values.append(polymer[y, x-1])  # Left
    if x < max_x - 1:
        surrounding_values.append(polymer[y, x+1])  # Right

    return surrounding_values

"""
def is_intact(polymer, N):

    vectors = np.argwhere(polymer > 0)
    
    for monomer in vectors:
        surroundings_arr = surroundings(polymer, monomer)
        y, x = monomer[0], monomer[1]
        val = polymer[y,x]
        vals = []
        vals.append(val)
        
        if len(set(vals)) != len(vals): #checking repeating vaalues
            return False
        
        if val == 1:
            elements = [2]
        elif val == N:
            elements = [N-1]
        else:
            elements = [val-1, val+1]

        if not all(elem in surroundings_arr for elem in elements): # sjekker naboer
            return False
        
    if len(vectors) != N: # sjekker antall tall
        return False
    
        
    return True
