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
        count = {} # map count of each element to a list of elements that occurs that mant times
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

            
