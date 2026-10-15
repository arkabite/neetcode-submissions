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
        n=len(word)

        def check(i,node):

            for j in range(i,n):
                char=word[j]
                if char==".":
                    for k in node.children.values():
                        if check(j+1,k):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node=node.children[char]

            return node.isEndOfWord

        return check(0,cur)