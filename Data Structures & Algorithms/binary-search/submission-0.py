class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for num in nums:
            if target == num:
                return nums.index(num)
        return -1


# nums = [1,2,3,4,5]
# target = 4
# return 3

