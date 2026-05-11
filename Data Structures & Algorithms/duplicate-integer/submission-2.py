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
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
        
