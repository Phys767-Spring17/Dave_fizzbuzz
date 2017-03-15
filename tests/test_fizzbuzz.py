#file located in tests/
#filename = test_fizzbuzz.py

from fizzbuzz.fizzbuzz import *

def test_fizzbuzz_1():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_3():
    assert fizzbuzz(3) == 'fizz'
