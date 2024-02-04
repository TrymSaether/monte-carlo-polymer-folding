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

p0, p1, e1, e2 = test_metropolis()


def strip_polymer(polymer):
    polymer = polymer[~np.all(polymer == 0, axis=1)]
    polymer = polymer[:, ~np.all(polymer == 0, axis=0)]
    nx, ny = np.shape(polymer)
    polymer = np.ma.masked_where(polymer == 0, polymer)
    return polymer, (nx, ny)

p0, (nx1, ny1) = strip_polymer(p0)
p1, (nx2, ny2) = strip_polymer(p0)
cmap = cm.get_cmap("plasma").copy()
cmap.set_bad(color="white")

fig = plt.figure()
(ax1, ax2) = fig.subplots(1, 2)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("Polymer 0")
ax1.grid(True, linewidth=0.2)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("Polymer 1")
ax2.grid(True, linewidth=0.2)

def set_polymer_text(ax, nx, ny):
    for i in range(nx):
        for j in range(ny):
            c = p1[i, j]
            if c != 0:
                ax.text(
                    j + 0.5,
                    i + 0.5,
                    str(int(c)),
                    va="center",
                    ha="center",
                    fontsize=8,
                    color="white",
                )
    


set_polymer_text(ax1, nx1, ny1)
set_polymer_text(ax2, nx2, ny2)
im1 = ax1.pcolormesh(p0, cmap=cmap, edgecolors="k", linewidth=0.2)
im2 = ax2.pcolormesh(p1, cmap=cmap, edgecolors="k", linewidth=0.2)
cbar = fig.colorbar(im1, ax=ax2, location="right")
cbar.set_label("monomer")
plt.show()


"""
Plot the image.
"""


test_metropolis()
#test_expectedvalue_and_standard_deviation()

#test_valid_rotations()
