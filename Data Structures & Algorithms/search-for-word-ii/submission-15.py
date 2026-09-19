class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False
    
    def addWord(self,word):
        cur=self

        for i in word:
            if i not in cur.children:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
        
        cur.isEndOfWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows,cols=len(board),len(board[0])
        root=TrieNode()

        for i in words:
            root.addWord(i)
        
        seen=set()
        res=set()

        def dfs(r,c,node,word):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] not in node.children or (r,c) in seen:
                return 
            
            seen.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isEndOfWord:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            seen.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        
        return list(res)