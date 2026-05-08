class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        arr = []
        for i in range(0, length):
            arr.append((position[i], speed[i]))

        sorted_arr = sorted(arr,key= lambda x: x[0], reverse=True ) 
        s = []   

        print(sorted_arr)
        for i in range(0, length):
            remaining = target - sorted_arr[i][0]
            fleet_num = remaining/sorted_arr[i][1]
            print(f"fleet_num:{fleet_num}")
            if i==0: 
                s.append(fleet_num)
            elif len(s) > 0 and s[-1]<fleet_num:
                s.append(fleet_num)   
        print(s)         
        return len(s)    
        