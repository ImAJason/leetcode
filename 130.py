class Solution(object):
    def solve(self, board):
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if (i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1) and board[i][j] == 'O':
                    self.dfs(board, i, j)
                    
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j]!='#':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

                    
    def dfs(self, board, i, j):
        
        if board[i][j] == 'O':
            board[i][j] = '#'
        
        if i>= 1 and board[i-1][j] == 'O': self.dfs(board, i-1, j)
        if i< len(board)-1 and board[i+1][j] == 'O': self.dfs(board, i+1, j)
        
        if j>= 1 and board[i][j-1] == 'O': self.dfs(board, i, j-1) 
        if j< len(board[0])-1 and board[i][j+1] == 'O': self.dfs(board, i, j+1)
