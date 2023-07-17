from src.ch3.parens import *

def test_is_balanced1():
    assert isBalanced("") == True

def test_is_balanced2():
    assert isBalanced("()()()()") == True

def test_is_balanced3():
    assert isBalanced("(())(())") == True

def test_is_balanced4():
    assert isBalanced("()(())()") == True

def test_is_balanced5():
    assert isBalanced(")()(())()") == False

def test_is_balanced6():
    assert isBalanced("()((())()") == False

def test_is_balanced7():
    assert isBalanced("())()(())(()") == False