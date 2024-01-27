import numpy as np
from matplotlib import pyplot as plt

def plot(polymer, N):
        """
        Plot the image.

        This method plots the image of the polymer grid using matplotlib.
        It uses the 'viridis' colormap for color mapping and 'nearest' interpolation
        for pixel display.
        The image is displayed with the origin at the lower left corner and
        the extent set to [0, N, 0, N].
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_aspect("equal")
        ax.set_xlim(0, N)
        ax.set_ylim(0, N)
        ax.set_xticks(np.arange(0, N + 1, np.floor(N / 10)))
        ax.set_yticks(np.arange(0, N + 1, np.floor(N / 10)))
        ax.set_xticklabels(np.arange(0, N + 1, np.floor(N / 10)))
        ax.set_yticklabels(np.arange(0, N + 1, np.floor(N / 10)))
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Polymer")
        if N < 50:
            ax.grid(True,linewidth=0.2)
        else:
            ax.grid(False)

        im = ax.pcolormesh(
            polymer,
            cmap="plasma",
            edgecolors="grey",
            linewidth=0.5,
            antialiased=True,
        )
        cbar = fig.colorbar(im, ticks=np.arange(1, N + 1, np.floor(N / 10)), boundaries=np.arange(1, N + 1, 1))
        cbar.set_label("monomer")
        plt.show()

