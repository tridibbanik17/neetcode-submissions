# ============================================================
# 3Sum
# Category : Array & Two Pointers & Sorting
# Difficulty: Medium
# NeetCode : https://neetcode.io/problems/three-integer-sum
# ============================================================
# Runtime : 78 ms   | Beats 99.96%
# Memory  : 8.4 MB  | Beats 100.00%
# Submitted: 2026-05-18
# ============================================================
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else: 
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
