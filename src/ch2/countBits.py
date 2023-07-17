
import math
from typing import List




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

def countBits_v2(n: int) -> List[int]:
    return [bin(i).count("1") for i in range(n+1)]

def convert_int_to_binary_list(i: int) -> int:
    # init array of binary to appropriate length
    result = [0 for _ in range(math.floor(math.log2(i))+1)]
    while i > 0:
        log = math.floor(math.log2(i))
        result[-(log+1)] = 1
        i -= 2**log
    return result


def convert_int_to_binary_list_v2(i: int) -> int:
    result = []
    while i:
        result.append(i & 1)
        i >>= 1
    return result[::-1] # Missy Elliott


