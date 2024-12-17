"""
A module with simple function
"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve


def add(a: int, b: int) -> int:
    """Add two numbers

    Args:
        a: number a
        b: number b

    Returns:
        added number
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Arguments should be integers!")
    return a + b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


def rms(input_array: np.ndarray) -> float:
    """enable doc. check"""
    if not isinstance(input_array, np.ndarray):
        raise TypeError("Arguments should be np.ndarray!")
    if np.ndim(input_array) != 1:
        raise TypeError("Dimension of array should be 1")
    if input_array.dtype != np.float64:
        raise TypeError("Array must only contain float64")
    if len(input_array) == 0:
        raise TypeError("The size of input_array should be at least 1!")
    if np.any(np.isnan(input_array)):
        raise TypeError("Array must not have NaN!")

    if np.any(np.isinf(input_array)):
        raise ValueError("The input_array should not contain any infinite (inf) values!")

    squared = np.square(input_array)  # Step 1: Square each element
    mean_of_squares = np.mean(squared)  # Step 2: Compute the mean of the squared values
    rms_result = np.sqrt(mean_of_squares)  # Step 3: Take the square root
    return rms_result

class LUSolver:
    def __init__(self, input_matrix: np.ndarray):
        """
        Constructor of the class. It takes the input matrix and decomposes it into LU factorization.
        Stores the LU decomposition and permutation matrix.
        """
        if not isinstance(input_matrix, np.ndarray):
            raise TypeError("Arguments should be np.ndarray!")
        self.lu, self.piv = lu_factor(input_matrix)  # Perform LU decomposition and store LU and pivot indices

    def solve(self, b: np.ndarray) -> np.ndarray:
        """
        Solve the linear equation Ax = b using the stored LU decomposition.
        :param b: Right-hand side vector
        :return: Solution vector x
        """
        x = lu_solve((self.lu, self.piv), b)  # Solve for x using LU decomposition and b
        return x
