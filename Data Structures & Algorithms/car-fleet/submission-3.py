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


# pos = [1,4]

# speed = [3,2]

# after 1 sec, pos = [1+3, 4+2] = [4, 6]
# after 2 sec, pos = [1+3+3, 4+2+2] = [7, 8]
# after 3 sec, pos = [1+3+3+3, 4+2+2+2] = [10, 10]

# pos = [1,2,3]
# speed = [4,5,6]

# zip([1,2,3], [4,5,6])
# [[1,4],[2,5],[3,6]]





