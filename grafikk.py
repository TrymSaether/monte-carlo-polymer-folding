import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colormaps as cm

def plot(polymer, N):
        """
        Plot the image.
        """
        polymer = polymer[~np.all(polymer == 0, axis=1)]
        polymer = polymer[:, ~np.all(polymer == 0, axis=0)]
        polymer = np.ma.masked_where(polymer == 0, polymer)
        cmap = cm.get_cmap("plasma").copy()
        cmap.set_bad(color='white')

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_aspect("equal")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Polymer")
        ax.grid(True,linewidth=0.2)
        im = ax.pcolormesh(
            polymer,
            cmap=cmap,
            linewidth=0.5,
            antialiased=True,
        )
        cbar = fig.colorbar(im, ticks=np.arange(1, N + 1, np.floor(N / 10)), boundaries=np.arange(1, N + 1, 1))
        cbar.set_label("monomer")
        plt.show()

