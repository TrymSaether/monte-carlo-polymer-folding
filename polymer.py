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

    def __init__(self, n, coord = (0,0), direction = True):
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
        self.coord = coord
        self.direction = direction
        self.rotate(coord, direction)

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
    
    def rotate(self, coord, direction):
        """
        Rotates the polymer around a given coordinate.

        Args:
            coord (tuple): The coordinate around which the rotation will occur.
            direction (bool): The direction of rotation. True for clockwise, False for counterclockwise.

        Returns:
            numpy.ndarray: The updated polymer grid after rotation.
        """

        polymer = self.grid
        n = len(polymer)

        i,j = coord[0], coord[1]
        
        # definerer om rotasjonen skal skje for verdiene over eller under mrot. 

        lower_vals = False
        
        mrot = polymer[i, j]
        if mrot <= int(n/2):                            # for mrot i midten vil den rotere monomerer med lavere nummer.
            lower_vals = True

        if lower_vals:                                  # lokaliserer monomerer som skal roteres
            vectors = np.argwhere(np.logical_and(polymer > 0, polymer < mrot))           
        else:
            vectors = np.argwhere(polymer > mrot)

        if direction:                                   # lager rotasjonsmatrise, bytter om på x- og y-akse for å passe iterering gjennom 2D-array
            rot_matrix =  np.matrix('0, -1; 1, 0')
        else:
            rot_matrix = np.matrix('0, 1; -1, 0')


        for vector in vectors:
            i , j = vector[0], vector[1]

            val = polymer[i,j]
            polymer[i, j] = 0
            rel_coord = (vector - coord)
            rot_rel_coord = np.dot(rot_matrix, rel_coord)
            new_coord = rot_rel_coord + coord
            new_i, new_j = new_coord[0,0], new_coord[0,1]
            polymer[new_i, new_j] = val


        self.grid = polymer


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
        Each monomer is labeled with its corresponding index.

        Returns:
        None
        """
        self.ax.imshow(
            self.grid,
            cmap="viridis",
            interpolation="nearest",
            origin="upper",
            extent=[0, self.n, 0, self.n],
        )

    def print(self):
        """
        Print the grid.
        """
        print(self.grid)
    

def main():
    """
    Main function
    """
    polymer = Polymer(15)
    polymer.rotate((7,7), True)
    polymer.plot_im()
    print(polymer)
    plt.show()


main()
