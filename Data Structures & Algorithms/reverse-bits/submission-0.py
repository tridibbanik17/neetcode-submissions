class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # get rightmost bit (get bit at position i)
            res = res | (bit << (31 - i)) # set leftmost bit

        return res
