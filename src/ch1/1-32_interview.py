from typing import List, Optional
import math
def dailyTemperatures(temperatures: List[int]) -> List[int]:
        result = []
        list_size = len(temperatures)
        for i in range(list_size):
            cur = temperatures[i]
            for j in range(list_size-i):
                if temperatures[i+j] > cur:
                    result.append(j)
                    break
                if j==list_size-i-1:
                    result.append(0)
        return result

# After a few hours of no progress finding a faster solution, I needed help with this
def dailyTemperatures2(temperatures: List[int]) -> List[int]:
    ans = [0 for _ in range(len(temperatures))]
    stack = []
    for cur_pos,cur_val in enumerate(temperatures):
        while stack and cur_val > stack[-1][1]:
            top_pos,top_val = stack.pop()
            ans[top_pos] = cur_pos-top_pos
        stack.append((cur_pos,cur_val))
    return ans

# print(dailyTemperatures2([73,74,75,71,69,72,76,73]))
# print(dailyTemperatures2([30,40,50,60]))
# print(dailyTemperatures2([30,60,90]))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# We can use modulo here to reduce the rotate value of k to a value less than the length of the list
# if post-modulo k == 0, return original list
# If empty list, return empty list
# Slice 
def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k==0:
        return head
    n = 1
    old_tail = head
    while old_tail.next is not None:
        old_tail = old_tail.next
        n += 1
    old_tail.next = head
    k %= n
    new_tail = head
    for i in range(n-k-1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head


# print(rotateRight(ListNode(1,ListNode(2,ListNode(3))),1))


# sort list in ascending order
# split list down the middle
# interleave the lists
def wiggleSort(nums: List[int]) -> None:
    nums.sort()
    half = len(nums[::2])
    nums[::2],nums[1::2] = nums[:half],nums[half:][::-1]

nums = [1,2,3,4,5,6,7]
wiggleSort(nums)
print(nums)

4556
5564

5645

def fast_wiggle_sort(nums: List[int]) -> None:
