class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_int = []
        nums.sort()
        for i in range(len(nums)+1):
            all_int.append(i)
        for j in range(len(nums)+1):
            if nums[j-1] != all_int[j-1]:
                return all_int[j-1]