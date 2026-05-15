class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        final_prod = 1
        new_prod = 1
        count = 0
        nc = nums.copy()
        for num in nums:
            final_prod *= num
        for num in nums:
            if num == 0:
                nc.remove(num)
                count += 1
                
        for n in nc:
            new_prod *= n       
        for num in nums:
            if num != 0:
                res.append(final_prod // num)
            elif num == 0 and count == 1:
                res.append(new_prod)
            else:
                res.append(0)

        return res