class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sett=set(t)
        minReqMatches=len(sett)
        count1=Counter(t)
        count2=defaultdict(int)
        l=0
        mon=0
        minLen=float("inf")
        bestWindow=(0,0)
        for r in range(len(s)):
            count2[s[r]]+=1
            if s[r] in sett and count2[s[r]]==count1[s[r]]:
                mon+=1
            
            while mon==minReqMatches:
                if ((r-l)+1)<minLen:
                    minLen=(r-l)+1
                    bestWindow=(l,r+1)
                
                count2[s[l]]-=1
                if s[l] in sett and count2[s[l]]<count1[s[l]]:
                    mon-=1
                l+=1
        
        return "" if minLen==float("inf") else s[bestWindow[0]:bestWindow[1]]
