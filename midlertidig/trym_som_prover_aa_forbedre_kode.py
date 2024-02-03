import numpy as np
N = 10

dt = np.dtype([('id', np.int32), ('position', np.int64, (2,))])
init_polymer = lambda N: np.array(np.arange(N), dtype = dt)
p0 = init_polymer(N)
print(p0)

def polymer_energy_trym(polymer, V):

    return 0

init_polymer = lambda N: np.array([[i+1, 0] for i in range(N)])

rotate_trym = lambda polymer, xy, state: polymer[xy:]@ np.array([[0, 2*state - 1], [2*state-1, 0]])


def expected_value(T, k_boltsmann, matrixV = func, create_initial_polymer = func1, rotate_test = func2, metropolis = func3):
    N = 30
    Ns_exclude, Ns = 1000, 3000
    V = matrixV(N, k = k_boltsmann)
    EXP = np.array([])
    STD = np.array([])
    for t in T:
        polymer = create_initial_polymer(N)
        polymer, _, _= rotate_test(N, Ns_exclude)
        _, E_temp = metropolis(polymer, V, Ns, t)
        EXP = np.append(EXP, np.mean(E_temp))
        STD = np.append(EXP, np.std(E_temp))
    # std_wtf = np.sqrt((T - exp_val)**2)
    return EXP, STD
