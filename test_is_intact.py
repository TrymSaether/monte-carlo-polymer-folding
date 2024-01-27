import numpy as np
from is_intact import is_intact

def test_is_intact():
    # Test case 1: Polymer is intact
    polymer1 = np.array([1, 2, 3, 4, 5])
    assert is_intact(polymer1, 5) == True

    # Test case 2: Polymer has incorrect length
    polymer2 = np.array([1, 2, 3, 4])
    assert is_intact(polymer2, 5) == False

    # Test case 3: Polymer has duplicate monomers
    polymer3 = np.array([1, 2, 3, 3, 4])
    assert is_intact(polymer3, 5) == False

    # Test case 4: Polymer has incorrect neighbors
    polymer4 = np.array([1, 2, 4, 5, 6])
    assert is_intact(polymer4, 5) == True

    # Test case 5: Polymer is intact with negative monomer values
    polymer5 = np.array([-2, -1, 0, 1, 2])
    assert is_intact(polymer5, 5) == True

    # Test case 6: Empty polymer
    polymer6 = np.array([])
    assert is_intact(polymer6, 0) == True

    # Test case 7: Polymer with single monomer
    polymer7 = np.array([1])
    assert is_intact(polymer7, 1) == True

    # Test case 8: Polymer with two monomers
    polymer8 = np.array([1, 2])
    assert is_intact(polymer8, 2) == True

    # Test case 9: Polymer with two duplicate monomers
    polymer9 = np.array([1, 1])
    assert is_intact(polymer9, 2) == False

    print("All test cases pass")

test_is_intact()