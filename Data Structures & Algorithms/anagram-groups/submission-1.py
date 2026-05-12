class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map character count to list of anagrams
        for string in strs:
            count = [0]*26 # a list of 26 0s
            for char in string:
                count[ord(char) - ord("a")] += 1 # after reading each char in s string, increment the counter for that string
            res[tuple(count)].append(string) # passing count as the key will raise TypeError because count is a list and list is mutable and key can never be mutable
        return list(res.values()) # return hashmap values