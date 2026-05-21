class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        area = 0
        for i in range(len(heights)-1):
            for j in range(i + 1, len(heights)):
                if heights[i] >= heights[j]:
                    area = heights[j]*(j-i)
                else:
                    area = heights[i]*(j-i)
                if area > max:
                    max = area           
        return max
