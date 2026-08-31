class Solution:
    def __init__(self):
        self.res=[]

    def encode(self, strs: List[str]) -> str:
        val=""
        for i in strs:
            lenOfStr=len(i)
            val+=str(lenOfStr)+"#"+i
        return val

    def decode(self, s: str) -> List[str]:
        print(s)
        val=""
        i=0
        while i<len(s):
            if s[i]=="#":
                length=int(val)
                val=""
                self.res.append(s[i+1:i+length+1])
                i+=length+1
            else:
                val+=s[i]
                i+=1
        return self.res
                

