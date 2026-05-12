class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list()
        s_rev = list()
        for c in s:
            if c == " ":
                c = ""
            s_list.append(c.lower())
            if not c.isalnum():
                s_list.remove(c)
        length = len(s_list)
        for iter in range(len(s_list)):
            s_rev.append(s_list[len(s_list) - iter - 1])
        for i in range(length):
            if s_list[i] != s_rev[i]:
                return False
        return True