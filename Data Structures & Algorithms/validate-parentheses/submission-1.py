class Solution:
    def isValid(self, s: str) -> bool:
        start=["(","{","["]
        end=[")","}","]"]
        brackets={"{":"}","[":"]","(":")"}
        sett1=set(start)
        sett2=set(end)
        stack=[]
        for i in range(len(s)):
            print(stack)
            cur=s[i]
            if cur in sett2:

                if not stack:
                    return False

                if stack:
                    if brackets[stack[-1]]!=cur:
                        return False

                while stack and brackets[stack[-1]]==cur:
                    stack.pop()
                    break
                    
            if cur in sett1:
                stack.append(cur)
        
        return len(stack)==0