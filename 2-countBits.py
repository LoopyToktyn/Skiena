
import unittest
import math
from typing import List

class TestCountBits(unittest.TestCase):
    def test0(self):
        self.assertEqual(countBits(0),[0])
    def test2(self):
        self.assertEqual(countBits(2),[0,1,1])
    def test8(self):
        self.assertEqual(countBits(8),[0,1,1,2,1,2,2,3,1])

class TestConvertVal(unittest.TestCase):
    def test4(self):
        self.assertEqual(convert_int_to_binary_list(4),[1,0,0])
    def test5(self):
        self.assertEqual(convert_int_to_binary_list(5),[1,0,1])


# let's do the naive approach first. For each i in n, convert to binary representation, count the 1s
def countBits(n: int) -> List[int]:
    result = [0]
    for i in range(n):
        b = convert_int_to_binary_list(i+1)
        count = 0
        for bi in b:
            if bi: count+=1
        result.append(count)
    return result

def convert_int_to_binary_list(i: int) -> int:
    # init array of binary to appropriate length
    result = [0 for _ in range(math.floor(math.log2(i))+1)]
    while i > 0:
        log = math.floor(math.log2(i))
        result[-(log+1)] = 1
        i -= 2**log
    return result

if __name__ == '__main__':
    unittest.main()