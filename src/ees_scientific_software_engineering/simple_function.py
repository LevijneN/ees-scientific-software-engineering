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
    squared = np.square(input_array)  # Step 1: Square each element
    mean_of_squares = np.mean(squared)  # Step 2: Compute the mean of the squared values
    rms_result = np.sqrt(mean_of_squares)  # Step 3: Take the square root
    return rms_result
