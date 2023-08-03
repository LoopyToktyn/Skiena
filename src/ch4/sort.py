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


"""
4-13. [5] A camera at the door tracks the entry time ai and exit time bi (assume
bi > ai) for each of n persons pi attending a party. Give an O(n log n) algorithm that analyzes this data to determine the time when the most people were
simultaneously present at the party. You may assume that all entry and exit
times are distinct (no ties).

Could sort the data as tuples based on time with the pair value being entry or exit. Then step through the sort, increment count for each entry, decrement count for each exit,
maintain a pointer at max.
"""

"""
4-15. [5] You are given a set S of n intervals on a line, with the ith interval described
by its left and right endpoints (li, ri). Give an O(n log n) algorithm to identify
a point p on the line that is in the largest number of intervals.
As an example, for S = {(10, 40),(20, 60),(50, 90),(15, 70)} no point exists in
all four intervals, but p = 50 is an example of a point in three intervals. You
can assume an endpoint counts as being in its interval.
"""

def interval_p(s: set[tuple[int,int]]) -> int:
    ordered = []
    for start,end in s:
        ordered.append((start,1))
        ordered.append((end,-1))

    ordered.sort(key=lambda o: (o[0],-o[1])) # this sort will make sure that for any ties, the positive/increment value is considered first
    count = 0
    max = (0,0)
    for val,action in ordered:
        count += action
        if count > max[1]:
            max = (val,count)
    return max[0]