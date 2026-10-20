class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols=len(board),len(board[0])
        seen=set()

        for r in range(rows):
            for c in range(cols):
                val=board[r][c]
                if val==".":
                    continue
                
                rowKey = ("row", r, val)
                colKey = ("col", c, val)
                boxKey = ("box", r // 3, c // 3, val)
                if rowKey in seen or colKey in seen or boxKey in seen:
                    return False
                
                seen.add(rowKey)
                seen.add(colKey)
                seen.add(boxKey)
        
        return True