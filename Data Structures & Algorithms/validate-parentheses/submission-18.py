class Solution:
    def isValid(self, s: str) -> bool:
        sett={"}":"{","]":"[",")":"("}
        stack=[]
        for i in s:
            if i in sett:
                if stack and stack[-1]==sett[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return not stack