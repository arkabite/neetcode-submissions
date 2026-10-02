class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            val=len(i)
            res+=str(val)+"#"+i
        
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        val=""
        i=0
        while i<len(s):
            if s[i]=="#":
                res.append(s[i+1:i+1+int(val)])
                i+=int(val)+1
                val=""
            else:
                val+=s[i]
                i+=1
        
        return res