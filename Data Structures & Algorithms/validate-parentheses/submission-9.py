class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        close_to_open = {')':'(', '}': '{', ']': '['}

        for char in s:
            
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False
                last_open = stack.pop()
                if close_to_open.get(char,0) != last_open:
                    return False
        return len(stack) == 0

