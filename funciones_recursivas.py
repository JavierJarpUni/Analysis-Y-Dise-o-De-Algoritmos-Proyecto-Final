import numpy as np

def divide_row(matrix, row, divisor):
    
    if len(matrix[row]) == 0:
        return matrix
    matrix[row, 0] /= divisor
    return divide_row(matrix, row, divisor)

def eliminate_variable(matrix, source_row, target_row, column):
    
    if column >= len(matrix[0]):
        return matrix
    matrix[target_row] -= matrix[source_row] * matrix[target_row, column] / matrix[source_row, column]
    return eliminate_variable(matrix, source_row, target_row, column + 1)

def gauss_jordan_2x2_recursive(matrix, row=0):
    if row >= len(matrix):
        
        return matrix
    if matrix[row, row] == 0:
        
        raise ValueError("Pivot is zero, cannot continue.")
    matrix = divide_row(matrix, row, matrix[row, row])
    if row < len(matrix) - 1:
        
        matrix = eliminate_variable(matrix, row, row + 1, row)
    return gauss_jordan_2x2_recursive(matrix, row + 1)


def gauss_jordan_3x3_recursive(matrix, row=0):
    if row >= len(matrix):
        
        return matrix
    if matrix[row, row] == 0:
        
        for i in range(row + 1, len(matrix)):
            if matrix[i, row] != 0:
                matrix[[row, i]] = matrix[[i, row]]
                break
        else:
            
            return None
    matrix = divide_row(matrix, row, matrix[row, row])
    for target_row in range(len(matrix)):
        if target_row != row:
            matrix = eliminate_variable(matrix, row, target_row, row)
    return gauss_jordan_3x3_recursive(matrix, row + 1)

