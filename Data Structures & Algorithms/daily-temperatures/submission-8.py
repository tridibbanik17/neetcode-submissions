class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            min_wait = 0
            for j in range(i+1,len(temperatures)):
                if min_wait > 0:
                    continue
                if temperatures[j] > temperatures[i]:
                    min_wait = j - i
            result.append(min_wait)
        return result
