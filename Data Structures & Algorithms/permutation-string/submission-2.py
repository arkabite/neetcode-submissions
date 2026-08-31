class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        count1=Counter(s1)
        count2=defaultdict(int)
        l=0
        for r in range(n2):
            count2[s2[r]]+=1
            if ((r-l)+1)==n1:
                check=0
                for i in count1:
                    if count1[i]!=count2[i]:
                        count2[s2[l]]-=1
                        l+=1
                        break
                    else:
                        check+=count1[i]
                if check==n1:
                    return True
        
        return False
                
