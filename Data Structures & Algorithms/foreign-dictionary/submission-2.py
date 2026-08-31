class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        check={c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minLen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    check[w1[j]].add(w2[j])
                    break
            
        
        seen={} #visited=False,currentpath+True
        res=[]
        def dfs(c):
            if c in seen:
                return seen[c]
            
            seen[c]=True
            for i in check[c]:
                if dfs(i):
                    return True
            seen[c]=False
            res.append(c)
        
        for i in check:
            if dfs(i):
                return ""
                
        res=res[::-1]
        return "".join(res)