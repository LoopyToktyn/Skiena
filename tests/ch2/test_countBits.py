import unittest
from src.ch2.countBits import *

class TestCountBits(unittest.TestCase):
    def test0(self):
        self.assertEqual(countBits(0),[0])
    def test2(self):
        self.assertEqual(countBits(2),[0,1,1])
    def test8(self):
        self.assertEqual(countBits(8),[0,1,1,2,1,2,2,3,1])

class TestCountBitsV2(unittest.TestCase):
    def test0(self):
        self.assertEqual(countBits_v2(0),[0])
    def test2(self):
        self.assertEqual(countBits_v2(2),[0,1,1])
    def test8(self):
        self.assertEqual(countBits_v2(8),[0,1,1,2,1,2,2,3,1])

class TestCountBitsMemo(unittest.TestCase):
    def test0(self):
        self.assertEqual(countBits_memo(0),[0])
    def test2(self):
        self.assertEqual(countBits_memo(2),[0,1,1])
    def test8(self):
        self.assertEqual(countBits_memo(8),[0,1,1,2,1,2,2,3,1])

class TestConvertVal(unittest.TestCase):
    def test4(self):
        self.assertEqual(convert_int_to_binary_list(4),[1,0,0])
    def test5(self):
        self.assertEqual(convert_int_to_binary_list(5),[1,0,1])

class TestConvertValV2(unittest.TestCase):
    def test4(self):
        self.assertEqual(convert_int_to_binary_list_v2(4),[1,0,0])
    def test5(self):
        self.assertEqual(convert_int_to_binary_list_v2(5),[1,0,1])


if __name__ == "__main__":
    unittest.main()