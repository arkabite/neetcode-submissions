class Solution:
    def isValid(self, s: str) -> bool:
        sett={")":"(","}":"{","]":"["}
        stack=[]

        for i in s:
            cur=i
            if i in sett:
                if stack and sett[cur]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cur)
        return not stack
