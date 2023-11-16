class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # col reverse -> zip으로 symmetric?
        # row reverse -> symmetric 
        i, j = 0, len(matrix)-1
        while i < len(matrix)//2:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
        
        k = 0
        for i in zip(*matrix):
            matrix[k] = i
            k += 1