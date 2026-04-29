class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(0, len(nums)):
            nums_map[nums[i]] = i
        for i in range(0, len(nums)):
            if target-nums[i] in nums_map and nums_map[target-nums[i]] != i :
                return [i, nums_map[target-nums[i]]]
