from src.ch3.anagram import *

def test_anagram_lower():
    w1 = "ranger"
    w2 = "rregan"
    assert is_anagram(w1,w2) is True

def test_anagram_upper():
    w1 = "RANGER"
    w2 = "rregan"
    assert is_anagram(w1,w2) is True

def test_anagram2():
    w1 = "abcdefghijklmnop"
    w2 = "aelekjflakjflajw"
    assert is_anagram(w1,w2) is False

def test_anagram3():
    w1 = "ranger"
    w2 = "rreganafaf"
    assert is_anagram(w1,w2) is False