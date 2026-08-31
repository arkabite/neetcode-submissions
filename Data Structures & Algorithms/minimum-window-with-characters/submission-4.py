class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        n=len(s)
        count1=Counter(t)
        count=defaultdict(int)
        sett=set(t)
        minLen=float("inf")
        bestWindow=(0,0)
        mon=0
        l=0
        for r in range(n):
            count[s[r]]+=1

            if s[r] in sett:
                if count[s[r]]==count1[s[r]]:
                    mon+=1
            
            while mon==len(sett):
                if ((r-l)+1)<minLen:
                    minLen=(r-l)+1
                    bestWindow=(l,r+1)
                    print("hello",bestWindow)               
                val=s[l]
                count[s[l]]-=1
                if val in sett:
                    if count[val]<count1[val]:
                        mon-=1
                l+=1

        return "" if minLen==float("inf") else s[bestWindow[0]:bestWindow[1]]