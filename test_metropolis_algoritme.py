import numpy as np
from metropolis_algoritme import metropolis
from V_matrix import polEnergy, v_Matrix
from main import create_initial_polymer
from matplotlib import pyplot as plt

def test_metropolis():
    # Test case 2
    N = 30
    polymer = create_initial_polymer(N)
    V = v_Matrix(N)
    T = 1
    beta = 0.5
    Ns = 40
    E_test = metropolis(polymer, V, Ns, T, beta)
    plt.plot(E_test, 'o', label = 'Energier 1')
    plt.legend()
    plt.show()
    print(E_test)
    expected_output = np.zeros(Ns, dtype=int)
    expected_output[0] = polEnergy(polymer, V)
    assert np.array_equal(metropolis(polymer, V, Ns, T, beta), expected_output)
    assert np.array_equal(metropolis(polymer, V, Ns, T, beta), expected_output)
    # Add more test cases if needed

test_metropolis()