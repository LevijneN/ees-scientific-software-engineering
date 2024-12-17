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
    array_test=1.0
    with pytest.raises(TypeError, match="Arguments should be np.ndarray!"):
        rms(array_test)
