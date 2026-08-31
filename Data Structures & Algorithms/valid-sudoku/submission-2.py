class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(len(board))]
        col=[set() for _ in range(len(board))]
        box=[set() for _ in range(len(board))]

        for r in range(len(board)):
            for c in range(len(board[0])):
                val=board[r][c]

                if val==".":
                    continue
                
                boxId= (r//3)*3+(c//3)
                
                if val in row[r] or val in col[c] or val in box[boxId]:
                    return False
                
                row[r].add(val)
                col[c].add(val)
                box[boxId].add(val)
        
        return True