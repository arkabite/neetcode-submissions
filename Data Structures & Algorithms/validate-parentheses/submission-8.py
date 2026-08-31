class Solution:
    def isValid(self, s: str) -> bool:
        sett={"(":")","{":"}","[":"]"}

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
        
        return not stack