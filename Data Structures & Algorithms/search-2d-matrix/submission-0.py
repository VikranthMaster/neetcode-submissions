class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in range(len(matrix)):
            l = 0
            h = len(matrix[x]) - 1
            while l <= h:
                mid = (l+h)//2
                if matrix[x][mid] == target:
                    return True
                elif matrix[x][mid] > target:
                    h = mid - 1
                elif matrix[x][mid] < target:
                    l = mid + 1
                
                else:
                    continue
            
        
        return False
                
