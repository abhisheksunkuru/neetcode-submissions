class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        i = 0
        j = length-1
        if length == 1 and target != nums[0]:
            return -1
        if length == 1 and target == nums[0]:
            return 0    
        while i < j :
            mid = (j+i)//2
            if i == mid or j == mid:
                if nums[i] == target:
                    return i
                if nums[j] == target:
                    return j    
                break
            if nums[mid] == target:
                return mid 
                break
            elif nums[mid] > target:
                j = mid
            elif nums[mid] < target:
                i = mid
        return -1                
