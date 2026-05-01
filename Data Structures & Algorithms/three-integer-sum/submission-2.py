class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        sorted_nums = sorted(nums)
        op = []
        for i in range(0, length):
            j = i+1
            k = length-1
            target = -sorted_nums[i]
            while j < k:
                pair_sum = sorted_nums[j] + sorted_nums[k]
                if pair_sum < target:
                    j += 1
                elif pair_sum > target:
                    k -= 1
                elif pair_sum == target:
                    el = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
                    if el not in op:
                        op.append(el)
                    j += 1    
                    
        return op           

