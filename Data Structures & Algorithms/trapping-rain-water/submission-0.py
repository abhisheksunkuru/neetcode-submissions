class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_heights = [0]*length
        right_heights = [0]*length
        
        lmax = 0
        water_sum = 0
        for i in range(0, length):
            if i == 0:
                left_heights[i] = 0
            left_heights[i] = lmax    
            if height[i] > lmax:
                lmax = height[i]
        print(left_heights)  
        j = length-1
        rmax = 0
        while j >= 0:
            if j == length-1:
                right_heights[j] = 0
            right_heights[j] = rmax
            if height[j] > rmax:
                rmax = height[j]
            j -= 1
        print(right_heights)    

        for i in range(0, length):
            capacity = min(left_heights[i], right_heights[i])-height[i]  
            if capacity > 0:
                water_sum += capacity  

        return water_sum    
                         