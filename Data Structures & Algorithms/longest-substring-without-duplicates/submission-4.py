class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        length = len(s)
        left = 0
        res = 0
        for right in range(length):
            while s[right] in se:
                se.remove(s[left])
                left +=1
            se.add(s[right])
            res = max(res, right-left+1)    
        return res    
