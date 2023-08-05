class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origincolor = image[sr][sc]
        
        def dfs(i,j):
            if i<0 or i>=len(image) or j<0 or j>=len(image[0]):
                return
            if image[i][j] == color or image[i][j] != origincolor:
                return
#            if 0<=i<len(image) and 0<=j<len(image[0]) and image[i][j] == origincolor:
            image[i][j] = color
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        dfs(sr,sc)
                
        return image
    