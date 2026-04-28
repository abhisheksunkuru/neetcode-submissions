class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = set(nums)
        p1 = 0
        pivot_arr = []
        for num in nums:
            if (num-1) not in set_list:
                pivot_arr.append(num)
        
        max_length = 0
        for num in pivot_arr:
            length = 0
            while num in set_list:
                length += 1
                num += 1
            if length > max_length:
                max_length = length
        return max_length        
