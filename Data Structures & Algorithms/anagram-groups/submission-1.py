# ============================================================
# Group Anagrams
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/anagram-groups
# ============================================================
# Runtime : 59 ms   | Beats 100.00%
# Memory  : 8.5 MB  | Beats 94.67%
# Submitted: 2026-05-11
# ============================================================
# Optimal solution: O(m*n), where m = each string size, n = strs list size
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map character count to list of anagrams
        for string in strs:
            count = [0]*26 # a list of 26 0s
            for char in string:
                count[ord(char) - ord("a")] += 1 # after reading each char in s string, increment the counter for that string
            res[tuple(count)].append(string) # passing count as the key will raise TypeError because count is a list and list is mutable and key can never be mutable
        return list(res.values()) # return hashmap values
