import numpy as np
N = 10

dt = np.dtype([('id', np.int32), ('position', np.int64, (2,))])
init_polymer = lambda N: np.array(np.arange(N), dtype = dt)
p0 = init_polymer(N)
print(p0)