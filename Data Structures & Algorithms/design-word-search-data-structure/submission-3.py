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

        def check(j,node):
            for i in range(j,len(word)):
                c=word[i]

                if c==".":
                    for j in node.children.values():
                        if check(i+1,j): return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node=node.children[c]

            return node.isEndOfWord
        
        return check(0,cur)