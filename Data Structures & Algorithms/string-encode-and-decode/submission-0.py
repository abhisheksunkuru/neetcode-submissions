class Solution:

    def encode(self, strs: List[str]) -> str:
        op = ''
        for string in strs:
            op += str(len(string)) + "#" + string
        return op                

    def decode(self, s: str) -> List[str]:
        op, i = [], 0
        while i < len(s):
            j = i
            while s[j] !="#":
                j += 1
            str_len = int(s[i:j])
            i = j+1
            op.append(s[i:i+str_len])
            i += str_len
        return op        

