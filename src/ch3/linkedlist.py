from util_classes.util_classes import *


def reverseListStack(head: ListNode) -> ListNode:
    stack = [None]
    while head is not None:
        stack.append(head)
        head = head.next

    result_head = stack[-1]
    result = result_head
    stack.pop()
    while stack:
        result.next = stack[-1]
        result = result.next
        stack.pop()
    return result_head

def reverseListIter(head: ListNode) -> ListNode:
    prev = None
    cur = head
    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def buildLinkedList(arr: List) -> ListNode:
    head = ListNode()
    current = head
    for i,val in enumerate(arr):
        current.val = val
        if i < len(arr)-1:
            current.next = ListNode()
        else:
            current.next = None
        current = current.next
    return head


print(buildLinkedList([1,2,3]))
print(reverseListStack(buildLinkedList([1,2,3])))
print(reverseListIter(buildLinkedList([1,2,3])))
