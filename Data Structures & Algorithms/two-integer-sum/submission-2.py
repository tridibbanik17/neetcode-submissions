class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # value:index
    
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map.get(diff,0),i]
            prev_map[n] = i
        return