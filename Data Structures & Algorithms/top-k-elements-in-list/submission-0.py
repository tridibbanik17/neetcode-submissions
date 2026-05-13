# ============================================================
# Top K Frequent Elements
# Category : Arrays & Hashing
# Difficulty: Medium
# NeetCode : https://neetcode.io/problems/top-k-elements-in-list
# ============================================================
# Runtime : 31 ms   | Beats 37.44%
# Memory  : 7.9 MB  | Beats 99.33%
# Submitted: 2026-05-12
# ============================================================
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # {n:c} where n = each distinct element of nums, c = counted number of element n
        freq = [[] for i in range(len(nums) + 1)] # initialize empty sublists 
        for num in nums: 
            count[num] = count.get(num, 0) + 1 # find the total count of each distinct element of nums
        for n, c in count.items(): # count.items = dict_items[(n1,c1), (n2,c2)]
            freq[c].append(n) # in each sublist, when applicable, add element 

        res = []
        for i in range(len(freq) - 1, 0, -1): # start iterating from the end and gradually move left
            for n in freq[i]: 
                res.append(n)
                if len(res) == k:
                    return res

            
