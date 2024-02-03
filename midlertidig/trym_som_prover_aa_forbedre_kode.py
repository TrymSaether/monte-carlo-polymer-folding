import numpy as np
N = 10

dt = np.dtype([('id', np.int32), ('position', np.int64, (2,))])
init_polymer = lambda N: np.array(np.arange(N), dtype = dt)
p0 = init_polymer(N)
print(p0)

def polymer_energy_trym(polymer, V):
    return 0

init_polymer = lambda N: np.array([[i+1, 0] for i in range(N)])

rotate= lambda polymer, xy, state: np.append(polymer,  polymer[xy[0]:,np.array(xy)[1]:] @ np.array([[0, 1 - 2*state],[2*state-1, 0]]), axis=0)
rotate= lambda polymer, xy, state: polymer[polymer > xy, :] @ np.array([[0, 1 - 2*state],[2*state-1, 0]])

