import pytest
from calculator import add,sub,mul,div

def test_add():
    assert add(2,3) == 4   # Actual is == expected (If match  then test case will pass)

def test_sub():
    assert sub(4,3) == 1   