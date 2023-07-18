from src.ch3.stack import *

def test_push_true():
    stack = Stack[int]()
    stack.push(1)
    assert stack.top == ListNode(1,None)

def test_push_false():
    stack = Stack[int]()
    stack.push(1)
    assert stack.top != ListNode(2,None)

def test_pop():
    stack = Stack[int]()
    stack.push(1)
    pop = stack.pop()
    assert pop == ListNode(1,None)

def test_pop_empty():
    stack = Stack[int]()
    pop = stack.pop()
    assert pop == None

def test_findmin():
    stack = Stack[int]()
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(2)
    min = stack.findmin()
    assert min == ListNode(1,None)

def test_findmin_afterminpop():
    stack = Stack[int]()
    stack.push(4)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.pop()
    min = stack.findmin()
    assert min == ListNode(2,None)