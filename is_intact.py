import numpy as np

def is_intact(polymer, N):
    """
    Check if the polymer is intact.

    This method checks if the polymer is intact.
    - It has N monomers
    - Every monomer m has a unique int from 1 to N
    - Every monomer m is neigbour with m - 1 and m + 1, except m = 1 and m = N
    It returns True if the polymer is intact and False otherwise.
    """
    intact = True
    if len(polymer) != N:
        intact = False
    elif len(np.unique(polymer)) != N:
        intact = False
    elif np.any(np.diff(polymer) != 1) and np.any(np.diff(polymer) != -1):
        intact = False
    return intact

p0 = np.arange(1, )