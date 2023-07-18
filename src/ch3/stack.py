from src.util_classes import *
from typing import TypeVar,Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self, top: ListNode=None):
        self.top = top
        self.min = top

    def push(self, val: T) -> None:
        node = ListNode(val,None)
        node.next = self.top
        self.top = node
        if self.min == None or self.min.val >= node.val:
            node.next = self.min
            self.min = node
    
    def pop(self) -> ListNode:
        if self.top == None:
            return None
        if self.top.val == self.min.val:
            self.min = self.min.next
        result = self.top
        self.top = self.top.next
        return result
    
    # This will return just the minimum node, it will not return any of its links
    def findmin(self):
        result = self.min
        result.next = None
        return result