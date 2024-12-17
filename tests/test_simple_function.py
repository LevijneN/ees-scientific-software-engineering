import numpy as np
import pytest

from ees_scientific_software_engineering.simple_function import add, multiply, rms


def test_add():
    assert add(1, 1) == 2


def test_multiply():
    assert multiply(2, 2) == 4


def test_add_error():
    a = 1.0
    b = 1
    with pytest.raises(TypeError, match="Arguments should be integers!"):
        add(a, b)


def test_rms():
    array_test = np.array([1.0, 1.0, 1.0])
    assert rms(array_test) == 1.0


def test_rms_error_ndarray():
    array_test = 1.0
    with pytest.raises(TypeError, match="Arguments should be np.ndarray!"):
        rms(array_test)


def test_rms_error_dimension():
    array_dimension_test = np.array([[1.0, 1.0], [1.0, 1.0]])
    with pytest.raises(TypeError, match="Dimension of array should be 1"):
        rms(array_dimension_test)


def test_rms_error_float():
    array_test = np.array([1, 1], dtype="int32")
    with pytest.raises(TypeError, match="Array must only contain float64"):
        rms(array_test)


def test_rms_error_float():
    array_test = np.array([1, 1], dtype="int32")
    with pytest.raises(TypeError, match="Array must only contain float64"):
        rms(array_test)


def test_rms_error_size_at_least_1():
    input_array = np.array([])
    with pytest.raises(TypeError, match="The size of input_array should be at least 1!"):
        rms(input_array)


def test_rms_has_NaN():
    input_array = np.array([np.nan, 1])
    with pytest.raises(TypeError, match="Array must not have NaN!"):
        rms(input_array)
