import random
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colormaps as cm

# Konstanter
k_boltsmann = 1.38e-23

def create_initial_polymer(N):
    grid = np.zeros((N, N), dtype=int)  # to-dimansjonalt grid uten polymer
    grid[int(N / 2)] = np.arange(1, N + 1)  # legger inn horisontalt polymer
    return grid


# ------------- V Matrise --------------
def matrixV(N,k=-1, c=1):
    # N: Størrelse på V
    # k: konstant som fyller V
    # c: Offset fra V_diagonal som fylles med k
    return np.array([[-k if (j < i - c) or (j > i + c) else 0 for j in range(N)] for i in range(N)])

def rotate(polymer, coord, direction):
    rotated_polymer = np.copy(polymer)
    N = len(rotated_polymer)

    i, j = coord[0], coord[1]

    # definerer om rotasjonen skal skje for verdiene over eller under mrot.
    lower_vals = False

    mrot = rotated_polymer[i, j]

    if mrot <= int(
        N / 2
    ):  # for mrot i midten vil den rotere monomerer med lavere nummer.
        lower_vals = True

    if lower_vals:  # lokaliserer monomerer som skal roteres
        vectors = np.argwhere(np.logical_and(rotated_polymer > 0, polymer < mrot))
    else:
        vectors = np.argwhere(rotated_polymer > mrot)

    if (
        direction
    ):  # lager rotasjonsmatrise, bytter om på x- og y-akse for å passe iterering gjennom 2D-array
        rot_matrix = np.matrix("0, -1; 1, 0")
    else:
        rot_matrix = np.matrix("0, 1; -1, 0")

    for vector in vectors:
        i, j = vector[0], vector[1]

        val = rotated_polymer[i, j]
        rotated_polymer[i, j] = 0
        rel_coord = vector - coord
        rot_rel_coord = np.dot(rot_matrix, rel_coord)
        new_coord = rot_rel_coord + coord
        new_i, new_j = new_coord[0, 0], new_coord[0, 1]
        rotated_polymer[new_i, new_j] = val

    return polymer, rotated_polymer

"""
# ----------------- Surroundings (feat. Nina) -----------------
def surroundings(polymer, monomer):  # defines surrounding values
    # ikke så nice, men skrevet av meg:
    surroundings = np.zeros(4)

    try: 
        up = monomer+np.array([-1, 0])
        y,x = up[0], up[1]
        up_val = polymer[y,x]
        surroundings[0] = up_val
    except:
        pass

    try:
        down = monomer + np.array([1, 0])
        y,x = down[0], down[1]
        down_val = polymer[y,x]
        surroundings[1] = down_val
    except IndexError:
        pass

    try:
        left = monomer + np.array([0, -1])
        y,x = left[0], left[1]
        left_val = polymer[y,x]
        surroundings[2] = left_val
    except IndexError:
        pass

    try:
        right = monomer + np.array([0, 1])
        y,x = right[0], right[1]
        right_val = polymer[y,x]
        surroundings[3] = right_val
    except IndexError:
        pass
    # Jeg synes egentlig den var ganske fin - Trymmelymm

    return surroundings
"""


# ----------------- Surroundings (feat. GPT) -----------------
def surroundings_chatgpt(polymer, monomer):
    # sykt nice men skrevet av ChatGPT: ((-(-_(-_(-_-)_-)_-)-))
    y, x = monomer
    max_y, max_x = polymer.shape
    surrounding_values = []

    if y > 0:
        surrounding_values.append(polymer[y - 1, x])  # Up
    if y < max_y - 1:
        surrounding_values.append(polymer[y + 1, x])  # Down
    if x > 0:
        surrounding_values.append(polymer[y, x - 1])  # Left
    if x < max_x - 1:
        surrounding_values.append(polymer[y, x + 1])  # Right
    return surrounding_values


# ----------------- Intact -----------------
def is_intact(polymer, N):
    vectors = np.argwhere(polymer > 0)

    for monomer in vectors:
        surroundings_arr = surroundings_chatgpt(polymer, monomer)
        y, x = monomer[0], monomer[1]
        val = polymer[y, x]
        vals = []
        vals.append(val)

        if len(set(vals)) != len(vals):  # checking repeating vaalues
            return False

        if val == 1:
            elements = [2]
        elif val == N:
            elements = [N - 1]
        else:
            elements = [val - 1, val + 1]

        if not all(elem in surroundings_arr for elem in elements):  # sjekker naboer
            return False

    if len(vectors) != N:  # checking amount of numbers
        return False

    return True

def rotate_test(N, Ns):
    """
    Utfører en Monte Carlo-simulering av polymerfolding ved å rotere polymeren.

    Parametere:
    N (int): Antall monomerer i polymeren.
    Ns (int): Antall Monte Carlo-steg som skal utføres.

    Returnerer:
    tuple: En tuple bestående av den resulterende polymeren, antall vellykkede rotasjoner og total tid brukt.

    """
    start = time.time()
    c = 1
    temp_polymer = create_initial_polymer(N)
    for i in range(1, Ns):
        monomer = np.argwhere(temp_polymer > 0)
        coord = monomer[np.random.randint(0, N)]
        rot = random.randint(0, 1)
        old_polymer, rot_polymer = rotate(temp_polymer,coord,rot)
        
        if is_intact(rot_polymer, N):
            c += 1
            temp_polymer = rot_polymer
        else:
            temp_polymer = old_polymer
    slutt = time.time()
    total_time = slutt-start
    return temp_polymer, c, total_time

# ----------------- Metropolis algorithms 1 -----------------
def polymer_energy(polymer, vMatrix):
    vectors = np.argwhere(polymer > 0)
    N = len(polymer)
    E = 0
    for monomer in vectors:
        surroundings_arr = surroundings_chatgpt(polymer, monomer)
        y, x = monomer[0], monomer[1]
        val = polymer[y, x]
        for i in range(N):
            m = val
            n = i + 1
            if n in surroundings_arr:
                b = 1
                E += 1 / 2 * vMatrix[m - 1, i]
            else:
                b = 0
            # E += 1/2 * vMatrix[m-1,i] * b
    return E


# ----------------- Metropolis algorithms 2 -----------------
def metropolis(polymer, V, Ns, T):
    """
    Utfører Metropolis Monte Carlo-simulering for polymerfolding.

    Args:
        polymer (numpy.ndarray): En array som representerer polymeren.
        V (numpy.ndarray): En array som representerer potensialet.
        Ns (int): Antall Monte Carlo-steg som skal utføres.
        T (float): Temperaturen i systemet.
        beta (float, optional): Invers temperatur. Standardverdi er 1.

    Returns:
        numpy.ndarray: En array med energiverdiene for hvert Monte Carlo-steg.
    """
    beta=1/(k_boltsmann * T)
    N = len(polymer)
    E_array = np.zeros(Ns+1)
    E = polymer_energy(polymer, V)
    i = 0
    while i < Ns:
        monomer = np.argwhere(polymer > 0)
        coord = monomer[np.random.randint(0, N)]
        dir = random.randint(0, 1)
        polymer, rot_polymer = rotate(polymer, coord, dir)
        if is_intact(rot_polymer, N):
            i += 1
            E_new = polymer_energy(rot_polymer, V)

            if E_new < E:
                polymer = rot_polymer
                E = E_new
            elif np.random.random() < np.exp(-beta * (E_new - E)):
                polymer = rot_polymer
                E = E_new
            E_array[i] = E
    return polymer, E_array

def expected_value(T):
    Ns_exclude, Ns = 1000, 3000
    V = matrixV(N, k = k_boltsmann)
    EXP = np.array([])
    STD = np.array([])
    for t in T:
        polymer = create_initial_polymer(N)
        polymer, _, _= rotate_test(N, Ns_exclude)
        _, E_temp = metropolis(polymer, V, Ns, t)
        EXP = np.append(EXP, np.mean(E_temp))
        STD = np.append(EXP, np.std(E_temp))
    # std_wtf = np.sqrt((T - exp_val)**2)
    return EXP, STD

# ----------------- Plotting -----------------
def plot(polymer, N):
    """
    Plot the image.
    """
    polymer = polymer[~np.all(polymer == 0, axis=1)]
    polymer = polymer[:, ~np.all(polymer == 0, axis=0)]
    nx, ny = np.shape(polymer)
    polymer = np.ma.masked_where(polymer == 0, polymer)
    cmap = cm.get_cmap("plasma").copy()
    cmap.set_bad(color="white")

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Polymer")
    ax.grid(True, linewidth=0.2)
    for i in range(nx):
        for j in range(ny):
            c = polymer[i, j]
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
    

    
    im = ax.pcolormesh(
        polymer,
        cmap=cmap,
        linewidth=0.5,
        antialiased=True,
    )
    cbar = fig.colorbar(
        im,
        ticks=np.arange(1, N + 1, np.floor(N / 10)),
        boundaries=np.arange(1, N + 1, 1),
    )
    cbar.set_label("monomer")
    plt.show()



def euclidean_distance(a , b):

    coord_a = np.array(a)
    coord_b = np.array(b)

    diff = (coord_a - coord_b)**2   #Square difference

    sum_diff = np.sum(diff)

    d = np.sqrt(sum_diff)

    return d



def largest_euclidean_distance(polymer):

    distances = []
    
    monomer = np.argwhere(polymer > 0)
    
    for i in range(len(monomer)):
        for j in range(len(monomer)):
            distances.append(euclidean_distance(monomer[i], monomer[j]))
    
    sorted_distances = np.sort(distances)


    return sorted_distances[-1]

