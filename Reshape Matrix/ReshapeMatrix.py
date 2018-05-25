class Solution:
##    def matrixReshape(self, nums, r, c):
##        """
##        :type nums: List[List[int]]
##        :type r: int
##        :type c: int
##        :rtype: List[List[int]]
##        """
##        ori_r = len(nums)
##        ori_c = len(nums[0])
##        
##        if ori_r * ori_c != r * c:
##            return nums    
##        
##        reshaped_matrix = [[0 for i in range(c)] for j in range(r)];
##        
##        for r_index in range(r):
##            for c_index in range(c):
##                current_index = r_index * c + c_index
##                
##                ori_r_index = int(current_index / ori_c)
##                ori_c_index = current_index - ori_r_index * ori_c
##                
##                reshaped_matrix[r_index][c_index] = nums[ori_r_index][ori_c_index]
##        
##        return reshaped_matrix
#
#    def matrixReshape_2(self, nums, r, c):
#        """
#        :type nums: List[List[int]]
#        :type r: int
#        :type c: int
#        :rtype: List[List[int]]
#        """
#        ori_r = len(nums)
#        ori_c = len(nums[0])
#        
#        if ori_r * ori_c != r * c:
#            return nums    
#        
#        reshaped_matrix = [[0 for i in range(c)] for j in range(r)];
#        
#        for i in range(r*c):                
#                reshaped_matrix[ int(i/c) ][ i%c ] = nums[ int(i/ori_c) ][ i%ori_c ]
#        
#        return reshaped_matrix

    
#the method of using generator is amazing!!!!!!
    
    def matrixReshape_3(self, A, nR, nC):
        if len(A) * len(A[0]) != nR * nC:
            return A
            
        vals = (val for row in A for val in row)
        return [[next(vals) for c in range(nC)] for r in range(nR)]

#def test(n):
#    yield n * n
#    yield n * n + 1

if __name__ == "__main__":
    s = Solution()
    test = [[1, 3], [2, 2], [3, 5], [4, 6]]
    print(s.matrixReshape_3(test, 2, 4))

    