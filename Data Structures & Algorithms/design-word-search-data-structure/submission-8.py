class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root

        for i in word:
            if i not in cur.children:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
        
        cur.isEndOfWord=True
        

    def search(self, word: str) -> bool:
        cur=self.root

        def dfs(j,node):

            for i in range(j,len(word)):
                c=word[i]

                if c==".":
                    for val in node.children.values():
                        if dfs(i+1,val):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node=node.children[c]
            return node.isEndOfWord
        
        return dfs(0,cur)
        
