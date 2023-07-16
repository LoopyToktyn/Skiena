import unittest
from collections import deque

class TestRemoveDigits(unittest.TestCase):
    def test1(self):
        self.assertEqual(removeKdigits("1432219",3),"1219")
    def test2(self):
        self.assertEqual(removeKdigits("10200",1),"200")
    def test3(self):
        self.assertEqual(removeKdigits("10",2),"0")
    def test4(self):
        self.assertEqual(removeKdigits("12345",3),"12")
    def test5(self):
        self.assertEqual(removeKdigits("54321",3),"21")
    def test6(self):
        self.assertEqual(removeKdigits("1919191",3),"1111")
    def test7(self):
        self.assertEqual(removeKdigits("123321123321",3),"1211123321")
    def test7(self):
        self.assertEqual(removeKdigits("123675948821",3),"123548821")
    def test8(self):
        self.assertEqual(removeKdigits("10",1),"0")

# My idea that I'm coming to is that I want as many consecutively increasing smallest-possible digits as I can obtain within the limits of numbers I can remove
# We'll probably want to look at a window of k+1. When k0 is greater than any value in window, remove it.
# 123[6759]48821
# # def removeKdigits(num: str, k: int) -> str:
#     length = len(num)
#     if k >= len(num):
#         return "0"
    
#     indices_to_drop = []
    
#     for ci in range(length):
#         is_smallest = True
#         i = 1
#         while is_smallest and i <= k:
#             if ci + i >= length or num[ci] > num[ci+i]:
#                 # print(f"Removing {num[ci]} because it is greater than {num[ci+i]}")
#                 is_smallest = False
#                 indices_to_drop.append(ci)
#                 k -= 1 #reduce k-window
#             i += 1


#     new_str = num
#     while indices_to_drop:
#         new_str = new_str[:indices_to_drop[-1]] + new_str[indices_to_drop[-1]+1:]
#         indices_to_drop.pop()

#     # remove leading 0s
#     while len(new_str) > 1 and new_str[0] == "0":
#         new_str = new_str[1:]

#     return new_str


def removeKdigits(num: str, k: int) -> str:
    result = deque([])

    if k >= len(num):
        return "0"

    # Create a stack, add every number, remove numbers when a smaller value is found, decrement k
    for val in num:
        while len(result) > 0 and k > 0 and val < result[-1]:
            result.pop()
            k -= 1
        result.append(val)

  

    # If end of list is reached and there are still values to remove, remove them from end of string. 
    # All situations like this should only have numbers in ascending order from left to right at this point, never descending
    for _ in range(k):
        result.pop()

    # Remove leading 0s. This is the primary reason we're using a deque
    while len(result) > 1 and result[0] == "0":
        result.popleft()
    
    return ''.join(result)
    
            


if __name__ == '__main__':
    unittest.main()