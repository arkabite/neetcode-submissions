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
        def dfs(i):
            if i in seen:
                return seen[i]
            
            seen[i]=True
            for j in D[i]:
                if dfs(j):
                    return True
            seen[i]=False
            res.append(i)
            return seen[i]
        
        for i in D:
            if dfs(i):
                return ""
        
        res=res[::-1]
        return "".join(res)