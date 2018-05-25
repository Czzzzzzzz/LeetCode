class Solution:
        
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            init_value = matrix[i][0]
            
            col = 0
            for row in range(i, rows):
                if col >= cols:
                    break
                
                if matrix[row][col] != init_value:
                    return False
                col = col + 1
        
        for i in range(cols):
            init_value = matrix[0][i];
            
            col = i;
            for row in range(0, rows):
                if col >= cols:
                    break;
                    
                if matrix[row][col] != init_value:
                    return False
                col = col + 1     
        return True;
        
#####concise solution#######
#solution 1
        
#    def isToeplitzMatrix(self, m):
#        for i in range(len(m) - 1):
#            for j in range(len(m[0]) - 1):
#                if m[i][j] != m[i + 1][j + 1]:
#                    return False
#        return True

#solution 1 - variation
#        def isToeplitzMatrix(self, m):
#        return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))
    
if __name__ == "__main__":
    s = Solution();
    a = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print(s.isToeplitzMatrix(a))