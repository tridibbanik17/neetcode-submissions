class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 1
        counter_list = [1]
        nums.sort()
        if len(nums) == 0:
            return 0      
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) == 0:
                continue
            elif abs(nums[i] - nums[i - 1]) == 1:
                counter += 1
                counter_list.append(counter)
            elif abs(nums[i] - nums[i - 1]) > 1:
                counter_list.append(counter)
                counter = 1 
        return max(counter_list)
