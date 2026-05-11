# ============================================================
# Valid Anagram
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/is-anagram
# ============================================================
# Runtime : 30 ms   | Beats 100.00%
# Memory  : 8.0 MB  | Beats 96.28%
# Submitted: 2026-05-10
# ============================================================
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
