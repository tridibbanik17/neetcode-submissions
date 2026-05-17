# ============================================================
# Longest Consecutive Sequence
# Category : Arrays & Hash Tables & Union Find
# Difficulty: Medium
# NeetCode : https://neetcode.io/problems/longest-consecutive-sequence
# ============================================================
# Runtime : 40 ms   | Beats 34.53%
# Memory  : 7.7 MB  | Beats 100.00%
# Submitted: 2026-05-17
# ============================================================
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for n in nums:
            if n-1 not in nums_set:
                length = 0
                while n+length in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest
