import numpy as np

def v_Matrix(N):
    grid = np.zeros((N,N), dtype=int, order='F')
    for i in range(N):
        for j in range(N):
            if i == j:
                grid[i,j] = 0
            elif i == j + 1:
                grid[i,j+1] = 0
            elif i + 1 == j:
                grid[i + 1, j] = 0
            else:
                grid[i,j] = -1

    return grid



def v_Matrix2(N):
    grid = np.zeros((N,N), dtype=int, order='F')
    for i in range(N):
        for j in range(N):
            if i == j:    
                 grid[i,j] = 0
            elif i == j + 1:
                grid[i,j+1] = 0
            elif i + 1 == j:
                grid[i + 1, j] = 0
            else:
                grid[i,j] = i + j
    return grid

print(v_Matrix2(10))



'''
V-matisen indikerer hvor sterk vekselvirkning det er mellom polymer m og n.
Denne V-matrisen øker i både horisontal og vertikal retning, som indikerer
at vekselvirkningen øker jo lengre unna monomerene var før polymeren ble rotert.
Vekselvirkningen vil også øke med hver monomer som legges til i polymeret.
På grunnlag av disse påstandene kan polymeren forventes å kveile seg innover
mot seg selv.

'''
