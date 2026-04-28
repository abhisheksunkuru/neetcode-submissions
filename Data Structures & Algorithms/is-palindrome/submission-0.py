class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_str = s.lower()
        p1 = 0
        p2 = len(lower_str) - 1
        while p1 < p2:
            if (lower_str[p1] >= 'a' and lower_str[p1] <= 'z') or (lower_str[p1] >= '0' and lower_str[p1] <= '9'):
                p1_char = lower_str[p1]
            else: 
                p1 += 1
                continue 

            if (lower_str[p2] >= 'a' and lower_str[p2] <= 'z') or (lower_str[p2] >= '0' and lower_str[p2] <= '9'):
                p2_char = lower_str[p2]
            else:
                p2 -=1
                continue

            if p1_char != p2_char:
                return False
                break
            
            p1 += 1
            p2 -= 1

        return True