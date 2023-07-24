from __future__ import annotations

class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next
    def __str__(self):
        next_val = self.next
        return f"ListNode({self.val}, {next_val})"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next
    
