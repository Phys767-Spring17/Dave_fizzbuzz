#file located in tests/
#filename = test_fizzbuzz.py

from fizzbuzz import fizzbuzz

def test_fizzbuzz_1():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_3():
    assert fizzbuzz(3) == 'fizz'
