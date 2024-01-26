"""
This module contains the definition of the Polymer class, which represents a polymer object.
It also includes functions for plotting the polymer grid and printing the grid.

Classes:
- Polymer: Represents a polymer object.

Functions:
- main: The main function of the module.
"""
import numpy as np
import matplotlib.pyplot as plt


class Polymer:
    """
    Represents a polymer object.

    Parameters:
    - n (int): The size of the grid.

    Attributes:
    - n (int): The size of the grid.
    - grid (numpy.ndarray): The grid representing the polymer.
    - m (numpy.ndarray): An array of integers from 1 to n.
    - fig (matplotlib.figure.Figure): The figure object for plotting.
    - ax (matplotlib.axes.Axes): The axes object for plotting.
    """

    def __init__(self, n):
        """
        Initialize a Polymer object.

        Args:
            n (int): The size of the grid.
        """
        self.n = n
        self.grid = np.zeros((n, n), dtype=int)
        self.m = np.arange(1, n + 1, dtype=int)
        self.grid[int(n / 2)] = self.m
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_aspect("equal")
        self.ax.set_xlim(1, n)
        self.ax.set_ylim(1, n)
        self.ax.set_xticks(np.arange(1, n + 1, 1))
        self.ax.set_yticks(np.arange(1, n + 1, 1))
        self.ax.grid(True)
        self.plot_mesh()
        self.plot_im()
    def __len__(self):
        """
        Return length of polymer.

        Returns:
            int: The length of the polymer.
        """
        return self.n

    def __getitem__(self, i):
        """
        Return monomer i.

        Args:
            i (int): The index of the monomer.

        Returns:
            numpy.ndarray: The monomer at the given index.
        """
        return self.grid[i]

    def __setitem__(self, i, value):
        """
        Set the value at the given index in the grid.

        Args:
            i (int): The index of the grid element to set.
            value: The value to set at the given index.
        """
        self.grid[i] = value

    def __str__(self):
        """
        Return string representation of the grid.

        Returns:
            str: The string representation of the grid.
        """
        return str(self.grid)

    def plot_mesh(self):
        """
        Plot the mesh using pcolormesh.

        This method plots the mesh using the pcolormesh function from matplotlib.
        The mesh is visualized with a colormap, black edges, and a transparency of 0.5.

        Parameters:
        None

        Returns:
        None
        """
        self.ax.pcolormesh(
            self.grid, cmap="viridis", edgecolor="black", linewidth=2, alpha=0.5
        )
        plt.show()

    def plot_im(self):
        """
        Plot the image.

        This method plots the image of the polymer grid using matplotlib.
        It uses the 'viridis' colormap for color mapping and 'nearest' interpolation for pixel display.
        The image is displayed with the origin at the lower left corner and the extent set to [0, self.n, 0, self.n].
        """

        self.ax.imshow(
            self.grid,
            cmap="viridis",
            interpolation="nearest",
            origin="lower",
            extent=[0, self.n, 0, self.n],
        )
        plt.show()

    def print(self):
        """
        Print the grid.
        """
        print(self.grid)


def main():
    """
    Main function
    """
    polymer = Polymer(10)
    polymer.plot_mesh()

    polymer.plot_im()
    print(polymer)
    polymer.print()


main()
