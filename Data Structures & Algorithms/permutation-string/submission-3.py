class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False
        count1=Counter(s1)
        count2=defaultdict(int)
        l=0
        for r in range(n2):
            count2[s2[r]]+=1
            if ((r-l)+1)==n1:
                if count1==count2:
                    return True
                else:
                    count2[s2[l]]-=1
                    if count2[s2[l]]==0:
                        del count2[s2[l]]
                    l+=1
        
        return False
                
