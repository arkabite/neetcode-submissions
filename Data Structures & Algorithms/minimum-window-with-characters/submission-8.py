class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        count1=Counter(t)
        count=defaultdict(int)
        sett=set(t)
        minReqMatches=len(sett)
        mon=0
        minLen=float("inf")
        bestWindow=(0,0)
        l=0
        for r in range(n):
            count[s[r]]+=1
            
            if count[s[r]]==count1[s[r]]:
                mon+=1
            
            while mon==minReqMatches:
                if ((r-l)+1)<minLen:
                    minLen=(r-l)+1
                    bestWindow=(l,r+1)
                
                count[s[l]]-=1
                if s[l] in sett and count[s[l]]<count1[s[l]]:
                    mon-=1
                l+=1
        
        return "" if minLen==float("inf") else s[bestWindow[0]:bestWindow[1]]