from polymer_utillties import *
from test_functions import test_metropolis, rotate_test, test_valid_rotations, test_expectedvalue_and_standard_deviation


'''
# ------- TEST: ROTATE_TEST --------
polymer, c, t = rotate_test(1000, 33)
N, Ns = 500, 100
polymer, c, t = rotate_test(N, Ns)
polymer0 = create_initial_polymer(20)
plot(polymer0, N)
plot(polymer, N)
'''

'''
# -------- TEST: POLENERGY --------
N = 20
Ns = 100
polymer, c, t = rotate_test(N, Ns)
vMatrix = v_Matrix(N)
print(polymer)
E = polEnergy(polymer, vMatrix)
print(E)
'''
#test_metropolis()
test_expectedvalue_and_standard_deviation()

#test_valid_rotations()
