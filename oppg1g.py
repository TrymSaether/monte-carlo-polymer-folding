from main import rotate_test
import numpy as np

polymer_15_4, c, t = rotate_test(15, 4) 
polymer_15_1000, c, t = rotate_test(15, 1000)

np.savez("Polymer_15_4", polymer_15_4)
np.savez("Polymer_15_1000", polymer_15_1000)

