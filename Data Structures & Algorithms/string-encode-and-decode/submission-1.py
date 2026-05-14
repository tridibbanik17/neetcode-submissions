# ============================================================
# Encode and Decode Strings
# Category : Array, String and Design
# Difficulty: Medium
# NeetCode : https://neetcode.io/problems/string-encode-and-decode
# ============================================================
# Runtime : 28 ms   | Beats 99.89%
# Memory  : 8.0 MB  | Beats 99.05%
# Submitted: 2026-05-14
# ============================================================

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # initialize an empty string
        for string in strs:
            res = res + str(len(string)) + '#' + string # ["neet","code"] -> "4#neet4#code"
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s): 
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # extract the length of a list item
            res.append(s[j+1:j+length+1]) 
            i = j+length+1 # bring pointer to the next item's length represented by an integer
        return res
