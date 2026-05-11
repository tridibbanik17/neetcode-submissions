# ============================================================
# Valid Anagram
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/is-anagram
# ============================================================
# Runtime : 49 ms   | Beats 73.04%
# Memory  : 8.7 MB  | Beats 23.06%
# Submitted: 2026-05-10
# ============================================================
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        for char_s in s:
            s_list.append(char_s)
        t_list = []
        for char_t in t:
            t_list.append(char_t)
        s_list.sort()
        t_list.sort()
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s_list)):
                if s_list[i] != t_list[i]:
                    return False
        return True
