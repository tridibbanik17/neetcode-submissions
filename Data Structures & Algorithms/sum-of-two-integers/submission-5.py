class Solution:
    def getSum(self, a: int, b: int) -> int: 
        # 32-bit mask to mimic 32-bit integer behavior
        mask = 0xFFFFFFFF
        while b != 0: # continue the loop until carry is 0 within 32 bits
            tmp = ((a & b) << 1) & mask # carry-out
            a = (a ^ b) & mask
            b = tmp
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)

