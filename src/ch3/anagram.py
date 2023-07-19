"""
3-10. [3] Two strings X and Y are anagrams if the letters of X can be rearranged
to form Y . For example, silent/listen, and incest/insect are anagrams. Give an
efficient algorithm to determine whether strings X and Y are anagrams.
"""

# works best if we convert to lowercase. We don't care about case for this problem.
def char_to_num(c:str) -> int:
    return ord(c) - ord('a')

def is_anagram(str1:str, str2:str) -> bool:
    if len(str1) != len(str2): return False

    word1 = [0 for _ in range(26)]
    word2 = [0 for _ in range(26)]

    for c in str1.lower():
        word1[char_to_num(c)] += 1
    for c in str2.lower():
        word2[char_to_num(c)] += 1

    return word1 == word2


def is_anagram_v2(str1: str, str2: str) -> bool:
    if len(str1) != len(str2): return False

    counts = [0 for _ in range(26)]

    for c1, c2 in zip(str1.lower(), str2.lower()):
        if not c1.isalpha() or not c2.isalpha(): continue
        counts[char_to_num(c1)] += 1
        counts[char_to_num(c2)] -= 1

    return all(count == 0 for count in counts)