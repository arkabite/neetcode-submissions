class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        sett=set(t)
        l=0
        minReqMatches=0
        count2=Counter(t)
        count1=defaultdict(int)
        bestWindow=(0,0)
        minLen=float("inf")
        for r in range(n):
            count1[s[r]]+=1

            if s[r] in sett and count1[s[r]]==count2[s[r]]:
                minReqMatches+=1
            
            while minReqMatches==len(sett):
                if ((r-l)+1)<minLen:
                    minLen=(r-l)+1
                    bestWindow=(l,r+1)

                count1[s[l]]-=1

                if s[l] in sett and count1[s[l]]<count2[s[l]]:
                    minReqMatches-=1
                l+=1
        
        return "" if minLen==float("inf") else s[bestWindow[0]:bestWindow[1]]