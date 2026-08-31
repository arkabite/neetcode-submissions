class Solution:
    def isValid(self, s: str) -> bool:
        sett={")":"(","]":"[","}":"{"}
        stack=[]
        for i in s:
            cur=i
            if i in sett:
                if stack and stack[-1]==sett[cur]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cur)
        
        return not stack