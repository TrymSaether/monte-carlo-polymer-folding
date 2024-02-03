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

print(v_Matrix2(20))




