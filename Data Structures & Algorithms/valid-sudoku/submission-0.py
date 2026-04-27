class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row_box in range(3):
            for col_box in range(3):
                cubes_list = []
                for row in range(row_box*3, row_box*3 + 3):
                    for col in range(col_box*3, col_box*3 + 3):
                        if board[row][col] != '.':
                            cubes_list.append(board[row][col]) 
                if len(cubes_list) != len(set(cubes_list)):
                    return False 
            


        for row in range(0,9):    
            row_list = list(filter(lambda ele: ele !='.', board[row]))
            if len(row_list) != len(set(row_list)):
                return False 
                
            

        for col in range(0,9):        
            col_list = [row[col] for row in board if row[col] != '.']
            if len(col_list) != len(set(col_list)):
                return False
        return True        
