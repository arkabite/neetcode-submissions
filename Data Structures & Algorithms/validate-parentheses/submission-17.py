class Solution:
    def isValid(self, s: str) -> bool:
        brack={"]":"[",")":"(","}":"{"}
        stack=[]
        for i in s:
            if i in brack:
                if stack and stack[-1]==brack[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return not stack