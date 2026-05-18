# ============================================================
# Two Integer Sum II
# Category : Arrays, Two Pointers, Binary Search
# Difficulty: Medium 
# NeetCode : https://neetcode.io/problems/two-integer-sum-ii
# ============================================================
# Runtime : 27 ms   | Beats 100.00%
# Memory  : 8.0 MB  | Beats 81.59%
# Submitted: 2026-05-17
# ============================================================
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1,r+1]
