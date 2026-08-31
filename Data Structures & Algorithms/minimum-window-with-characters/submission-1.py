class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1=Counter(t)
        count2=Counter(s)
        sett=set(t)
        n=len(s)
        res=""
        restot=float("inf")
        tot=[]
        li=[]
        l=0
        for k,v in count1.items():
            if k not in count2:
                return ""
            else:
                val=count2[k]
                if v>val:
                    return ""
        
        for i in range(n):
            if s[i] in sett:
                li.append(i)
        
        l=li[0]
        r=l
        mon=0
        count=defaultdict(int)
        while r<n:
            tot.append(s[r])
            count[s[r]]+=1
            if s[r] in sett:
                if count1[s[r]]==count[s[r]]:
                    mon+=1
            while mon==len(sett):
                if restot>len(tot):
                    restot=len(tot)
                    res=tot.copy()
                val1=tot.pop(0)
                count[val1]-=1
                if count[val1]<count1[val1]:
                    mon-=1
            r+=1
        return "".join(res)

        
        
