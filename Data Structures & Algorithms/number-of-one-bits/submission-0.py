class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        n=str(bin(n))
        for i in n:
            print(i)
            if i=="1":
                res+=1
        return res