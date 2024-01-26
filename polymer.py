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
    - n (int): The size of the grid and polymer.

    Attributes:
    - n (int): The size of the polymer.
    - polymer (numpy.ndarray): The grid representing the polymer.
    - m (numpy.ndarray): An array of integers from 1 to n.
    - fig (matplotlib.figure.Figure): The figure object for plotting.
    - ax (matplotlib.axes.Axes): The axes object for plotting.
    """

    def __init__(self, n, coord=(0, 0), direction=True):
        """
        Initialize a Polymer object.

        Args:
            n (int): The size of the polymer.
        """
        self.n = n
        self.polymer = np.zeros((n, n), dtype=int)
        self.monomer = np.arange(1, n + 1, dtype=int)
        self.polymer[int(n / 2)] = self.monomer
        self.x = np.arange(1, n + 1)
        self.y = np.arange(1, n + 1)
        self.coord = coord
        self.direction = direction
        self.rotate(coord, direction)
        self.polymer_size = np.count_nonzero(self.polymer)

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
        return self.polymer[i]

    def __setitem__(self, i, value):
        """
        Set the value at the given index in the polymer.

        Args:
            i (int): The index of the polymer element to set.
            value: The value to set at the given index.
        """
        self.polymer[i] = value

    def __str__(self):
        """
        Return string representation of the polymer.

        Returns:
            str: The string representation of the polymer.
        """
        return str(self.polymer)
    
    def rotate(self, coord, direction):
        """
        Rotates the polymer around a given coordinate.

        Args:
            coord (tuple): The coordinate around which the rotation will occur.
            direction (bool): The direction of rotation.
            - True for clockwise, False for counterclockwise.

        Returns:
            numpy.ndarray: The updated polymer polymer after rotation.
        """
        polymer = self.polymer
        n = self.n

        i, j = coord[0], coord[1]

        # definerer om rotasjonen skal skje for verdiene over eller under mrot.
        lower_vals = False

        mrot = polymer[i, j]
        if mrot <= int(
            n / 2
        ):  # for mrot i midten vil den rotere monomerer med lavere nummer.
            lower_vals = True

        if lower_vals:  # lokaliserer monomerer som skal roteres
            vectors = np.argwhere(np.logical_and(polymer > 0, polymer < mrot))
        else:
            vectors = np.argwhere(polymer > mrot)

        if direction:  # lager rotasjonsmatrise
            # - bytter om på x- og y-akse for å passe iterering gjennom 2D-array
            rot_matrix = np.matrix("0, -1; 1, 0")
        else:
            rot_matrix = np.matrix("0, 1; -1, 0")

        for vector in vectors:
            i, j = vector[0], vector[1]

            val = polymer[i, j]
            polymer[i, j] = 0
            rel_coord = vector - coord  # remove unnecessary parentheses
            rot_rel_coord = np.dot(rot_matrix, rel_coord)
            new_coord = rot_rel_coord + coord
            new_i, new_j = new_coord[0, 0], new_coord[0, 1]
            polymer[new_i, new_j] = val

        self.polymer = polymer
    
    def intact(self):
        """
        Checks if the polymer is intact.

        Returns:
            bool: True if the polymer is intact, False otherwise.
        """
        polymer = self.polymer
        n = self.n
        intact = True

        # check if polymer is intact
    
    def plot(self):
        """
        Plot the image.

        This method plots the image of the polymer grid using matplotlib.
        It uses the 'viridis' colormap for color mapping and 'nearest' interpolation
        for pixel display.
        The image is displayed with the origin at the lower left corner and
        the extent set to [0, self.n, 0, self.n].
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_aspect("equal")
        ax.set_xlim(0, self.n)
        ax.set_ylim(0, self.n)
        ax.set_xticks(np.arange(0, self.n + 1, np.floor(self.n / 10)))
        ax.set_yticks(np.arange(0, self.n + 1, np.floor(self.n / 10)))
        ax.set_xticklabels(np.arange(0, self.n + 1, np.floor(self.n / 10)))
        ax.set_yticklabels(np.arange(0, self.n + 1, np.floor(self.n / 10)))
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Polymer")
        if self.n < 50:
            ax.grid(True,linewidth=0.2)
        else:
            ax.grid(False)

        im = ax.pcolormesh(
            self.polymer,
            cmap="plasma",
            edgecolors="grey",
            linewidth=0.5,
            antialiased=True,
        )
        cbar = fig.colorbar(im, ticks=np.arange(1, self.n + 1, np.floor(self.n / 10)), boundaries=np.arange(1, self.n + 1, 1))
        cbar.set_label("monomer")
        plt.show()

    def print(self):
        """
        Print the polymer.
        """
        print(self.polymer)


def main():
    """
    Main function
    """
    polymer = Polymer(20)
    polymer.rotate((5, 5), True)
    polymer.print()
    polymer.plot()
    plt.show()


main()
