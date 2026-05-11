# ============================================================
# Valid Anagram
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/is-anagram
# ============================================================
# Runtime : 41 ms   | Beats 73.04%
# Memory  : 8.0 MB  | Beats 5.62%
# Submitted: 2026-05-10
# ============================================================
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i],0)

        for j in range(len(t)):
            count_t[t[j]] = 1 + count_t.get(t[j],0)
        
        for key in count_s:
            if count_s[key] != count_t.get(key,0):
                return False
        return True
