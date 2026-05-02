class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) - 1
        i = 0
        max_area = 0
        while i < j:
            min_height = min(heights[i], heights[j])
            distance = j-i
            area = distance*min_height
            if area > max_area:
                max_area = area
            if heights[i] < heights[j]:    
                i += 1 
            else:
                j -= 1       
        return max_area



        