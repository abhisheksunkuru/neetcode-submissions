class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. Initialize result with 0s
        res = [0] * len(temperatures)
        stack = [] # Stores pairs: [temp, index]
        
        for i, t in enumerate(temperatures):
            # 2. While the current temp is warmer than the temp at the top of the stack
            while stack and t > stack[-1][0]:
                stack_temp, stack_ind = stack.pop()
                # 3. Calculate the distance and update the result
                res[stack_ind] = i - stack_ind
            
            # 4. Push current temp and its index onto the stack
            stack.append([t, i])
            
        return res
        