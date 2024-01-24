# Matplotlib inline

import assets.polymer as p
import numpy as np
import matplotlib.pyplot as plt

# initialize polymer
p1 = p.Polymer(100, 100, 1)

# plot polymer
fig = p1.plotPolymer2D()
