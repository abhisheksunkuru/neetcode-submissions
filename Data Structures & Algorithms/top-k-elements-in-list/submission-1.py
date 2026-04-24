class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        sorted_keys = sorted(d.keys(), key=lambda x: d[x], reverse=True)            
        return sorted_keys[:k]
