import numpy as np

def create_initial_polymer(N):

    grid = np.zeros((N,N), dtype=int, order='F')        # to-dimansjonalt grid uten polymer
    grid[int(N/2)] = np.arange(1, N+1)                  # legger inn horisontalt polymer
    return grid


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

def is_intact(polymer, N):

    if len(polymer) != N:
        intact = False
    elif len(np.unique(polymer)) != N:
        intact = False

    intact = True
    vectors = np.argwhere(polymer > 0)
    for i in range(1, N): 
        monomer = vectors[i]
        surroundings_arr = surroundings(polymer, monomer)
        y, x = monomer[0], monomer[1]
        val = polymer[y,x]
        
        if val == 1:
            elements = 2
            intact = np.all(np.isin(elements, surroundings_arr))
            print(intact)
        elif val == N:
            elements = N-1
            intact = np.all(np.isin(elements, surroundings_arr))
        else:
            elements = np.array([val-1, val+1])
            intact = np.all(np.isin(elements, surroundings_arr))
    return intact
