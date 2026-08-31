class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        D={c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minLen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    D[w1[j]].add(w2[j])
                    break
        
        seen={}
        res=[]
        def dfs(node):
            if node in seen:
                return seen[node]
            
            seen[node]=True
            for i in D[node]:
                if dfs(i):
                    return True
            res.append(node)
            seen[node]=False
            return seen[node]
        
        for i in D:
            if dfs(i):
                return ""
        
        res=res[::-1]
        return "".join(res)
            