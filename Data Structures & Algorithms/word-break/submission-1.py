class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words=set(wordDict)

        maxWord=max(len(w) for w in wordDict) if wordDict else 0
        
        memo={}
        def dfs(i):
            if i==len(s):
                return True
            if i in memo:
                return memo[i]
            
            for end in range(i+1,min(len(s)+1,i+maxWord+1)):
                val=s[i:end]

                if val in words:
                    if dfs(end):
                        memo[i]=True
                        return True

            memo[i]=False
            return False

        return dfs(0)