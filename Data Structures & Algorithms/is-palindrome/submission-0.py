# ============================================================
# Contains Duplicate
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/is-palindrome
# ============================================================
# Runtime : 43 ms   | Beats 11.77%
# Memory  : 7.7 MB  | Beats 99.66%
# Submitted: 2026-05-12
# ============================================================
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list() # create new list
        s_rev = list() # create new list
        for c in s:
            if c == " ": # string cleaning: remove all whitespace
                c = ""
            s_list.append(c.lower()) # all char must be lowercase to be comparable
            if not c.isalnum(): # remove any character that is not alphanumeric
                s_list.remove(c)
        length = len(s_list)
        for iter in range(length):
            s_rev.append(s_list[length - iter - 1]) # generate reversed list
        for i in range(length):
            if s_list[i] != s_rev[i]: # find inconsistency between normal and reversed list
                return False
        return True
