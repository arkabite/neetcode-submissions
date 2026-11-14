class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        check={"+","-","/","*"}
        for i in tokens:
            if i in check:
                val1=int(stack.pop())
                val2=int(stack.pop())
                res=0
                if i=="+":
                    res=val1+val2
                elif i=="/":
                    res=int(val2/val1)
                elif i=="-":
                    res=val2-val1
                elif i=="*":
                    res=val1*val2
                stack.append(str(res))
            else:
                stack.append(i)
        
        print(6//-132)
        return int(stack[-1])
