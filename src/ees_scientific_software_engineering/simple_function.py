"""
A module with simple function
"""

import numpy as np


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

    squared = np.square(input_array)  # Step 1: Square each element
    mean_of_squares = np.mean(squared)  # Step 2: Compute the mean of the squared values
    rms_result = np.sqrt(mean_of_squares)  # Step 3: Take the square root
    return rms_result
