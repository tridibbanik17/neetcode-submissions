# ============================================================
# Products of Array Except Self
# Category : Arrays & Prefix Sum
# Difficulty: Medium
# NeetCode : https://neetcode.io/problems/products-of-array-discluding-self
# ============================================================
# Runtime : 27 ms   | Beats 100.00%
# Memory  : 8.2 MB  | Beats 9.69%
# Submitted: 2026-05-15
# ============================================================

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = res[j] * postfix
            postfix = nums[j] * postfix
        return res
