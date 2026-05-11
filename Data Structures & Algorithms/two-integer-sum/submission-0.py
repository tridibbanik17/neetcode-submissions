# ============================================================
# Two Sum
# Category : Arrays & Hashing
# Difficulty: Easy
# NeetCode : https://neetcode.io/problems/two-integer-sum
# ============================================================
# Runtime : 36 ms   | Beats 21.50%
# Memory  : 8.0 MB  | Beats 21.64%
# Submitted: 2026-05-10
# ============================================================
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    if i < j:
                        output_list.append(i)
                        output_list.append(j)
                    else:
                        output_list.append(j)
                        output_list.append(i)
        return output_list
