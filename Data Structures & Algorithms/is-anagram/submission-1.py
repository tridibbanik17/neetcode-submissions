# ============================================================
# Valid Anagram
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/is-anagram
# ============================================================
# Runtime : 44 ms   | Beats 73.04%
# Memory  : 9.0 MB  | Beats 5.62%
# Submitted: 2026-05-10
# ============================================================
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
