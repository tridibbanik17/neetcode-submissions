class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[]
        for p, s in zip(position, speed): # zip([1,2,3],[4,5,6])=[1,4],[2,5],[3,6]
            pair.append([p, s])
        stack = []
        for p, s in sorted(pair)[::-1]: # descending order of position
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)




