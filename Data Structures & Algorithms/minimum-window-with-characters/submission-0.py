class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c2 = {}
        for char in t:
            c2[char] = 1 + c2.get(char, 0)

        have, need = 0, len(c2)
        c1 = {}
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            c1[char] = 1 + c1.get(char, 0)
            
            # If the current character's frequency matches what we NEED
            if char in c2 and c1[char] == c2[char]:
                have += 1
            
            # While the window is valid, try to shrink it from the left
            while have == need:
                # Update result if this window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                # Pop from left
                c1[s[l]] -= 1
                if s[l] in c2 and c1[s[l]] < c2[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""               
        