class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols=len(board),len(board[0])

        box1=[]
        seenbox1=set()
        box2=[]
        seenbox2=set()
        box3=[]
        seenbox3=set()
        box4=[]
        seenbox4=set()
        box5=[]
        seenbox5=set()
        box6=[]
        seenbox6=set()
        box7=[]
        seenbox7=set()
        box8=[]
        seenbox8=set()
        box9=[]
        seenbox9=set()

        #First row
        for r in range(0,3):
            for c in range(cols):
                if c<3:
                    val=board[r][c]
                    if val!="." and val not in seenbox1:
                        box1.append(val)
                        seenbox1.add(val)
                    elif val in seenbox1:
                        return False
                elif c>=3 and c<6:
                    val=board[r][c]
                    if val!="." and val not in seenbox2:
                        box2.append(val)
                        seenbox2.add(val)
                    elif val in seenbox2:
                        return False
                elif c>=6 and c<9:
                    val=board[r][c]
                    if val!="." and val not in seenbox3:
                        box3.append(val)
                        seenbox3.add(val)
                    elif val in seenbox3:
                        return False

        #Second row
        for r in range(3,6):
            for c in range(cols):
                if c<3:
                    val=board[r][c]
                    if val!="." and val not in seenbox4:
                        box4.append(val)
                        seenbox4.add(val)
                    elif val in seenbox4:
                        return False
                elif c>=3 and c<6:
                    val=board[r][c]
                    if val!="." and val not in seenbox5:
                        box5.append(val)
                        seenbox5.add(val)
                    elif val in seenbox5:
                        return False
                elif c>=6 and c<9:
                    val=board[r][c]
                    if val!="." and val not in seenbox6:
                        box6.append(val)
                        seenbox6.add(val)
                    elif val in seenbox6:
                        return False
        
        #Third row
        for r in range(6,9):
            for c in range(cols):
                if c<3:
                    val=board[r][c]
                    if val!="." and val not in seenbox7:
                        box7.append(val)
                        seenbox7.add(val)
                    elif val in seenbox7:
                        return False
                elif c>=3 and c<6:
                    val=board[r][c]
                    if val!="." and val not in seenbox8:
                        box8.append(val)
                        seenbox8.add(val)
                    elif val in seenbox8:
                        return False
                elif c>=6 and c<9:
                    val=board[r][c]
                    if val!="." and  val not in seenbox9:
                        box9.append(val)
                        seenbox9.add(val)
                    elif val in seenbox9:
                        return False
        
        #checking rows and columns:
        for r in range(rows):
            rowCheck=set()
            for c in range(cols):
                val=board[r][c]
                if val!=".":
                    if val in rowCheck:
                        return False
                    rowCheck.add(val)
        
        for c in range(cols):
            colCheck=set()
            for r in range(rows):
                val=board[r][c]
                if val!=".":
                    if val in colCheck:
                        return False
                    colCheck.add(val)
        
        return True