class Solution:
    def isValid(self, s: str) -> bool:
        sett={"(":")","{":"}","[":"]"}
        if len(s)==0:
            return False
        elif len(s)==1:
            return False
        stack=[]
        for i in range(len(s)):
            cur=s[i]
            if cur not in sett:
                if stack and sett[stack[-1]]==cur:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cur)
        
        return len(stack)==0