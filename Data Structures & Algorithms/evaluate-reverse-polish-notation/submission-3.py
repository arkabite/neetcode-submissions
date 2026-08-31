class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        n=len(tokens)
        for i in range(n):
            cur=tokens[i]
            if cur in {"+","-","/","*"}:
                b=stack.pop()
                a=stack.pop()

                if cur=="+":
                    stack.append(a+b)
                elif cur=="-":
                    stack.append(a-b)
                elif cur=="/":
                    stack.append(int(a/b))
                elif cur=="*":
                    stack.append(a*b)
            else:
                stack.append(int(cur))
        
        return stack[0]
