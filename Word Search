#BackTracking

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for y in range(len(board)):
            for x in range(len(board[0])):
                if(self.dfs(board,word,0,x,y)):
                    return True
        return False

    def dfs(self,board,word,i,x,y):
        if(i == len(word)):
            return True
        if(x < 0 or x >= len(board[0]) or y < 0 or y >= len(board)): #邊界
            return False
        if(board[y][x]!=word[i]):
            return False
        
        board[y][x] = board[y][x].swapcase()
        isexit =  (self.dfs(board, word, i + 1, x + 1, y) or 
                  self.dfs(board, word, i + 1, x, y + 1) or 
                  self.dfs(board, word, i + 1, x - 1, y) or 
                  self.dfs(board, word, i + 1, x, y - 1))
        board[y][x] = board[y][x].swapcase()   # 代表走過的路線 
 
        return isexit

                    
  
                
            
