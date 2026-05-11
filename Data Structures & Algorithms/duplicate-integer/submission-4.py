# ============================================================
# Contains Duplicate
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/duplicate-integer
# ============================================================
# Runtime : 43 ms   | Beats 26.00%
# Memory  : 11.2 MB  | Beats 2.18%
# Submitted: 2026-05-10
# ============================================================
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True

        return False
        
