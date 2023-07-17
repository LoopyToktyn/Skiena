import unittest
from src.ch2.quadruplets import *

class TestQuads(unittest.TestCase):
    def test1(self):
        self.assertEqual(fourSum([1,0,-1,0,-2,2],0),[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
    def test2(self):
        self.assertEqual(fourSum([2,2,2,2,2],8),[[2,2,2,2]])
    def test3(self):
        self.assertEqual(fourSum([-1,0,1,2,-1,-4],-1),[[-4,0,1,2],[-1,-1,0,1]])

class TestTwos(unittest.TestCase):
    def test1(self):
        self.assertEqual(twoSum([1,2,3,4],7),[[3,4]])
    def test2(self):
        self.assertEqual(twoSum([1,2,2,3],4),[[1,3],[2,2]])
    def test3(self):
        self.assertEqual(twoSum([1,2,2,3],3),[[1,2]])
    def test4(self):
        self.assertEqual(twoSum([1,2,2,3],6),[])

class TestTwosV2(unittest.TestCase):
    def test1(self):
        self.assertEqual(twoSumv2([1,2,3,4],7),[[3,4]])
    def test2(self):
        self.assertEqual(twoSumv2([1,2,2,3],4),[[1,3],[2,2]])
    def test3(self):
        self.assertEqual(twoSumv2([1,2,2,3],3),[[1,2]])
    def test4(self):
        self.assertEqual(twoSumv2([1,2,2,3],6),[])



