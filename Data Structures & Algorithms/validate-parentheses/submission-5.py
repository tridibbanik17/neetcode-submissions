class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if s[0] in ')}]':
            return False
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if stack:
                    last_open = stack.pop()
                else:
                    return False
                if char == ')' and last_open != '(' or char == '}' and last_open != '{' or char == ']' and last_open != '[':
                    return False
        return len(stack)==0

