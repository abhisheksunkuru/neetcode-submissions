class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            arr = [0]*26
            for char in s:
                index = ord(char)-97
                arr[index] += 1
            key = tuple(arr)    
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return list(d.values())                    
        