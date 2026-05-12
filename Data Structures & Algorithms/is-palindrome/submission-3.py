# ============================================================
# Valid Palindrome
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/is-palindrome
# ============================================================
# Runtime : 44 ms   | Beats 9.50%
# Memory  : 7.7 MB  | Beats 99.66%
# Submitted: 2026-05-12
# ============================================================
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # initialize one left pointer and one right pointer
        while (l < r): # while loop runs until left and right pointers are about to cross over
            while l < r and not s[l].isalnum(): # until an alphanumeric character is found, increment 
                l += 1
            while l < r and not s[r].isalnum(): # until an alphanumeric character is found, decrement 
                r -= 1
            if s[l].lower() != s[r].lower(): # if left pointer value and right pointer value are not the same, return False immediately
                return False
            l += 1 # mover the pointers
            r -= 1
        return True



            
