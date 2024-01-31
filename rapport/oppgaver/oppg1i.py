from main import rotate_test
import numpy as np
import matplotlib.pyplot as plt

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