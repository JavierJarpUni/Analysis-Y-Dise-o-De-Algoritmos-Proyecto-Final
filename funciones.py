import numpy as np

def gauss_jordan_2x2(a, b):
    
    print(a)
    print(b)   
    matrix = np.array([a, b], dtype=np.float64)
    
    if matrix[0, 0] == 0:
        pass
    
    matrix[0] = matrix[0] / matrix[0, 0]
    
    matrix[1] -= matrix[1, 0] * matrix[0]
    
    if matrix[1, 1] == 0:
        pass
    
    matrix[1] = matrix[1] / matrix[1, 1]
    
    matrix[0] -= matrix[0, 1] * matrix[1]
    
    return matrix[0, 2], matrix[1, 2]

def gauss_jordan_3x3(a, b, c):
    
    matrix = np.array([a, b, c], dtype=np.float64)
    
    num_vars = 3
    for i in range(num_vars):
        
        pivot = matrix[i, i]
        if pivot == 0:
            
            for j in range(i+1, num_vars):
                if matrix[j, i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    pivot = matrix[i, i]
                    break
            else:
                
                return None
        
        matrix[i] /= pivot
        
        for j in range(num_vars):
            if i != j:
                matrix[j] -= matrix[i] * matrix[j, i]
    
    return matrix[:, -1].tolist()