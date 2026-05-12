# ============================================================
# Valid Palindrome
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/is-palindrome
# ============================================================
# Runtime : 44 ms   | Beats 9.51%
# Memory  : 8.0 MB  | Beats 17.90%
# Submitted: 2026-05-12
# ============================================================
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while (l < r):
            while l < r and not self.isalnum(s[l]):
                l += 1
            while l < r and not self.isalnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isalnum(self, c:str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))



            
