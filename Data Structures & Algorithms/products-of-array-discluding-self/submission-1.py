class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        prefix_prod = []
        prefix_prod.append(nums[0])
        i += 1
        while i < len(nums):
            prefix_prod.append(nums[i]*prefix_prod[i-1])
            i += 1
        j = len(nums)-1
        suffix_prod = [None]*len(nums)
        suffix_prod[j] = nums[j]
        j -= 1
        while j >=0:
            suffix_prod[j] = nums[j]*suffix_prod[j+1]
            j -=1
        print(f"prefix_prod:{prefix_prod}")
        print(f"suffix_prod:{suffix_prod}")
        op = []
        arr_len = len(nums)
        for k in range(0,len(nums)):
            if k == 0:
                op.append(suffix_prod[1])
            elif k == len(nums)-1:
                op.append(prefix_prod[k-1])
            else:
                op.append(prefix_prod[k-1]*suffix_prod[k+1])  
        return op              

        