import numpy as np

# def solve_2x2_systems(a1, b1, c1, a2, b2, c2):
#     """
#     Solves a system of 2 linear equations:
#     a1*x + b1*y = c1
#     a2*x + b2*y = c2
#     Returns the solution as (x, y).
#     """
#     coefficients = np.array([[a1, b1], [a2, b2]])
#     constants = np.array([c1, c2])

#     # Check if the system has a unique solution
#     if np.linalg.det(coefficients) != 0:
#         solution = np.linalg.solve(coefficients, constants)
#         return solution.tolist()  # Return the solution as a list
#     else:
#         return None  # The system has no unique solution

def gauss_jordan_2x2(a, b):
    
    print(a)
    print(b)   
    matrix = np.array([a, b], dtype=np.float64)

    # Ensure the leading coefficient of the first equation is not zero
    if matrix[0, 0] == 0:
        # Swap rows or add a multiple of one row to another to fix
        pass  # This should be replaced with actual code to handle the zero coefficient

    # Divide the first row by the leading coefficient to get a leading 1
    matrix[0] = matrix[0] / matrix[0, 0]
    
    # Eliminate the first variable from the second row
    matrix[1] -= matrix[1, 0] * matrix[0]

    # Ensure the leading coefficient of the second equation is not zero (after elimination)
    if matrix[1, 1] == 0:
        # This system is either dependent or inconsistent
        pass  # This should be replaced with actual code to handle the zero coefficient

    # Divide the second row by the leading coefficient to get a leading 1
    matrix[1] = matrix[1] / matrix[1, 1]

    # Eliminate the second variable from the first row
    matrix[0] -= matrix[0, 1] * matrix[1]

    # The solutions are now the constants in the last column
    return matrix[0, 2], matrix[1, 2]

def gauss_jordan_3x3(a, b, c):
    """
    Solves a system of 3 linear equations using the Gauss-Jordan method:
    a[0]*x + a[1]*y + a[2]*z = a[3]
    b[0]*x + b[1]*y + b[2]*z = b[3]
    c[0]*x + c[1]*y + c[2]*z = c[3]
    Each parameter a, b, c is a list of coefficients for its respective equation.
    Returns the solution as (x, y, z).
    """
    matrix = np.array([a, b, c], dtype=np.float64)
    
    # The number of variables should match the number of equations
    num_vars = 3
    for i in range(num_vars):
        # Make the diagonal contain all 1s
        pivot = matrix[i, i]
        if pivot == 0:
            # Search for a non-zero pivot and swap rows
            for j in range(i+1, num_vars):
                if matrix[j, i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]  # Swap the rows
                    pivot = matrix[i, i]
                    break
            else:
                # No non-zero pivot was found; the system is singular
                return None
        
        matrix[i] /= pivot  # Normalize the pivot row

        # Make all other entries in the column 0
        for j in range(num_vars):
            if i != j:
                matrix[j] -= matrix[i] * matrix[j, i]
    
    # The last column contains the solutions
    return matrix[:, -1].tolist()