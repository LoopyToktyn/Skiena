from src.ch4.sort import *

def test_two_sum1():
    assert two_sum([1,2,3,4],5) == [[1,4],[2,3]]

def test_k_sum1():
    assert k_sum([1,2,3,4,5,6],9,3) == [[1,2,6],[1,3,5],[2,3,4]]

def test_n_sum1():
    assert n_sum([1,2,3,4,5,6],9,4) == False

def test_interval_p():
    assert interval_p([(1,5),(2,6),(3,4),(4,10),(5,6),(6,9)]) == 4