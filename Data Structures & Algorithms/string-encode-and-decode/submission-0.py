class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += '~!@' + string 
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = s.split('~!@')
        strs.remove(strs[0])
        return strs
