import pytest

from app import sumatoria

def test_sum():
    n1 = 1
    n2 = 2
    assert sumatoria.suma(n1, n2) == 3

