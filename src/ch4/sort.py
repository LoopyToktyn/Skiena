import sys
sys.path.insert(0, r'F:\ws-py3\Skiena')
from typing import List
"""
. [5] Given a set S of n integers and an integer T, give an O(n^k-1 log n) algorithm
to test whether k of the integers in S add up to T.
"""

def n_sum(s: List[int], T: int, k: int) -> bool:
    s.sort()
    return len(k_sum(s,T,k)) > 0

def k_sum(s: List[int], T: int, k: int) -> List[List[int]]:
    res = []
    if len(s) == 0 or s[0]*k > T or s[-1]*k < T:
        return res
    if k == 2:
        return two_sum(s,T)
    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1]:
            for subset in k_sum(s[i+1:], T- s[i], k-1):
                res.append([s[i]] + subset)

    return res


def two_sum(s: List[int], T: int) -> List[List[int]]:
    i = 0
    j = len(s) - 1
    res = []
    while i < j:
        if s[i] + s[j] > T:
            j -= 1
        elif s[i] + s[j] < T:
            i += 1
        else: # s[i] + s[j] == T
            res.append([s[i],s[j]])
            i += 1
            j -= 1
    return res

print(k_sum([1,2,3,4,5,6],10,4))