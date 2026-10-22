class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sett=set(t)
        minReqMatches=len(sett)
        count1={}

        for i in t:
            count1[i]=count1.get(i,0)+1

        track=0
        l=0
        count2={}
        minLen=float("inf")
        bestWindow=(0,0)

        for r in range(len(s)):
            count2[s[r]]=count2.get(s[r],0)+1

            if s[r] in sett and count2[s[r]]==count1[s[r]]:
                track+=1

            while track==minReqMatches:
                if ((r-l)+1)<minLen:
                    minLen=(r-l)+1
                    bestWindow=(l,r+1)
                count2[s[l]]-=1
                if s[l] in sett and count2[s[l]]<count1[s[l]]:
                    track-=1
                l+=1
        
        return "" if minLen==float("inf") else s[bestWindow[0]:bestWindow[1]]
