import time
import random
from polymer_utillties import create_initial_polymer, matrixV, polymer_energy, rotate, is_intact, metropolis, plot, rotate_test, expected_value
import numpy as np
from matplotlib import pyplot as plt




def test_valid_rotations():
    N = np.arange(10, 200, 50)
    percent_Ns1 = []
    percent_Ns2 = []
    percent_Ns3 = []

    N1 = 50
    N2 = 500
    N3 = 1000

    fig, ax = plt.subplots(figsize=(8, 5))
    for i in N:
        polymer1, c1, t1 = rotate_test(i, N1)
        polymer2, c2, t2 = rotate_test(i, N2)
        polymer3, c3, t3 = rotate_test(i, N3)

        percent_Ns1.append((c1/N1)*100)
        percent_Ns2.append((c2/N2)*100)
        percent_Ns3.append((c3/N3)*100)

    ax.plot(N, percent_Ns1, label = (f'Ns = {N1}'))
    ax.plot(N, percent_Ns2, label = (f'Ns = {N2}'))
    ax.plot(N, percent_Ns3, label = (f'Ns = {N3}'))
    ax.grid()
    ax.legend()
    ax.set_xlabel('Size of polymer, N')
    ax.set_ylabel('Valid rotations [%]')
    ax.set_title('Valid rotations with varying polymer size')
    plt.show()

    """
    Ved større N går prosentandelen gyldige rotasjoner ned ved.
    Når polymeren er stor er det større sannsynlighet for at rotasjonen forrårsaker kollisjon mellom
    monomerer, ettersom endene blir lange, og det er flere monomerer man kan velge å rotere om.
    Antall mulige rotasjoner går altså opp i takt med N, samtidig som gunstige/gyldige rotasjoner minker.
    Dette gjenspeiles også i grafen, som harvnokså kraftig fall med økende N for alle Ns.

    Grafene viser også at større verdier for forsøkte rotasjoner, Ns, typisk vil resultere i at ferre
    rotasjoner faktisk kan gjennomføres. I begynnelsen er det liten sannsynlighet for ugyldige rotasjoner,
    ettersom polymeren fremdeles ikke er så sammenkveilet. Ved liten Ns får disse større vekting i den totale
    sannsynligheten P = G/M, og den totale prosenten blir derfor høyere.
    """

    # ---------------- OPPGAVE 2b ----------------
def test_metropolis(c = 1):

    # Konstanter
    N, Ns = 25, 5000
    polymer = create_initial_polymer(N)
    k = 4e-21 # enhet: [J/K]
    V = k*matrixV(N)

    # Simulering 1
    T_lav = 50 # 50 K < T_lav < 100K
    polymer_1, E_1 = metropolis(polymer, V, Ns, T_lav)

    # Simulering 2
    T_hoy = 300 # [K] - 293 K < T_hoy < 373 K
    polymer_2, E_2 = metropolis(polymer, V, Ns, T_hoy)

    fig, (ax_e1, ax_e2) = plt.subplots(1, 2,figsize = (18, 9))
    # Plott
    ax_e1.plot(E_1, 'b', label=f'E1, (T_lav = {T_lav})')
    ax_e2.plot(E_2, 'r', label=f'E2 (T_hoy = {T_hoy})')
    #plt.xlabel('t')
    #plt.ylabel('E [J]')
    #plt.legend()
    #plt.grid()
    #plt.show()

    plot(polymer_1, N)
    plot(polymer_2, N)

def test_expectedvalue_and_standard_deviation():
    T = np.arange(10, 1001, 30)
    exp_val, std = expected_value(T)

    plt.title('Forventingsverdi $E$ og standardavvik $\sigma$', fontsize=13)
    plt.plot(T, exp_val, color = 'deepskyblue', label="$E$ ")
    plt.errorbar(T, std[:34], color = 'steelblue', label="$\sigma_{E}$")
    plt.xlabel('$T$')
    plt.ylabel('$E og \sigma_E$')
    plt.grid()
    plt.legend()
    plt.show()
