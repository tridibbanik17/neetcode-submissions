class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = dict() # dictionary to add all counts as values and each element of nums as keys

        for num in nums:
            counts[num] = counts.get(num, 0) + 1 # increment count after travering a new item in nums list
        for num, count in counts.items(): # key=num, value=count
                                          # counts.items() => [(key1,value1),(key2,value2)]
            if count == 1:
                return num

             