class Solution(object):
    def pacificAtlantic(self, matrix):
        
        if not matrix: return []
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        m, n = len(matrix), len(matrix[0])
        pac = [[False]*n for _ in range(m)]
        atl = [[False]*n for _ in range(m)]
        
        for i in range(m):
            self.dfs(matrix, i, 0, pac, m, n)
            self.dfs(matrix, i, n-1, atl, m, n)
            
        for j in range(n):
            self.dfs(matrix, 0, j, pac, m, n)
            self.dfs(matrix, m-1, j, atl, m, n)
            
        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
                    
        return res
    
    
    def dfs(self, matrix, i, j, visited, m, n):
        
        visited[i][j] = True
        
        for dir in self.directions:
            r, c = i+dir[0], j+dir[1]
            
            if r<0 or r==m or c<0 or c==n or visited[r][c] or matrix[r][c] < matrix[i][j]: continue
            self.dfs(matrix, r, c, visited, m, n)
            
