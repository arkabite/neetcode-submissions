class Solution:
    def isValid(self, s: str) -> bool:
        seen={"}":"{","]":"[",")":"("}
        stack=[]
        for i in s:
            if i in seen:
                if stack and seen[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        
        return not stack