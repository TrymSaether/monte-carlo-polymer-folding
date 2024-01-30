from main import rotate_test
import numpy as np
import matplotlib.pyplot as plt


N = np.arange(10, 500, 100)
Ns = np.arange(10, 50, 10)
percent = []
fig, ax = plt.subplots(figsize=(8, 5))

for i in N:
    for j in Ns:
        polymer, c, t = rotate_test(i, j)
        p = (c/j)*100
        percent.append(p)
ax.plot(N, percent, label=f'Ns = {Ns}')
ax.legend()
plt.show()

    