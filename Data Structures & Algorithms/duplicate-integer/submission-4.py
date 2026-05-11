# ============================================================
# Contains Duplicate
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/duplicate-integer
# ============================================================
# Runtime : 37 ms   | Beats 25.99%
# Memory  : 13.7 MB  | Beats 1.62%
# Submitted: 2026-05-10
# ============================================================
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True

        return False
        