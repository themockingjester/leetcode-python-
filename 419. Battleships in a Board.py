class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ctr=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    if i and board[i-1][j]=='X':
                        continue
                    if j and board[i][j-1]=='X':
                        continue
                    ctr+=1
        return ctr
    
