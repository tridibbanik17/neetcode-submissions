# ============================================================
# Two Sum
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/two-integer-sum
# ============================================================
# Runtime : 27 ms   | Beats 100.00%
# Memory  : 7.7 MB  | Beats 99.97%
# Submitted: 2026-05-10
# ============================================================
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # value:index
    
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map.get(diff,0),i]
            prev_map[n] = i
        return
