import time
import random
from polymer_utillties import create_initial_polymer, v_Matrix, polEnergy, rotate, is_intact, metropolis
import numpy as np
from matplotlib import pyplot as plt


def rotate_test(N, Ns):
    """
    Utfører en Monte Carlo-simulering av polymerfolding ved å rotere polymeren.

    Parametere:
    N (int): Antall monomerer i polymeren.
    Ns (int): Antall Monte Carlo-steg som skal utføres.

    Returnerer:
    tuple: En tuple bestående av den resulterende polymeren, antall vellykkede rotasjoner og total tid brukt.

    """
    start = time.time()
    c = 1
    temp_polymer = create_initial_polymer(N)
    for i in range(1, Ns):
        monomer = np.argwhere(temp_polymer > 0)
        coord = monomer[np.random.randint(0, N)]
        rot = random.randint(0, 1)
        old_polymer, rot_polymer = rotate(temp_polymer,coord,rot)
        
        if is_intact(rot_polymer, N):
            c += 1
            temp_polymer = rot_polymer
        else:
            temp_polymer = old_polymer
    slutt = time.time()
    total_time = slutt-start
    return temp_polymer, c, total_time


def test_metropolis():
    # Test case 2
    N = 30
    polymer = create_initial_polymer(N)
    V = v_Matrix(N)
    T = 1
    beta = 0.5
    Ns = 40
    E_test = metropolis(polymer, V, Ns, T, beta)
    plt.plot(E_test, 'ro', label=f'Energi - polymer (N = {N})')
    plt.grid()
    plt.legend()
    plt.show()
    print(E_test)
    expected_output = np.zeros(Ns, dtype=int)
    expected_output[0] = polEnergy(polymer, V)
    # assert np.array_equal(metropolis(polymer, V, Ns, T, beta), expected_output)
    # assert np.array_equal(metropolis(polymer, V, Ns, T, beta), expected_output)
    # Add more test cases if needed


