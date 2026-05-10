class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = len(s)
        op = 1 if length > 0 else 0
        for i in range(length):
            h = {}
            h[s[i]] = 1
            max_chars =0
            for j in range(i+1, length):
                if s[j] not in h:
                    h[s[j]] = 1
                    max_chars = j-i+1
                    
                else:
                    #l = j-i    
                    # if l > max_chars:
                    #     max_chars = l
                    
                    print(op)
                    break
                op = max(op, max_chars)    
        return op                
