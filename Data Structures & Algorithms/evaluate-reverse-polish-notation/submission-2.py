class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        n=len(tokens)
        for i in range(n):
            cur=tokens[i]
            j=0
            store=[]
            if cur not in {"+", "-", "*", "/"}:
                stack.append(int(cur))
            else:
                j=0
                store=[]
                while stack and j<2:
                    store.append(stack.pop())
                    j+=1
                
                if cur=="+":
                    val=store[1]+store[0]
                elif cur=="-":
                    val=store[1]-store[0]
                elif cur=="/":
                    val=int(store[1]/store[0])
                elif cur=="*":
                    val=store[1]*store[0]
                stack.append(val)
        
        return stack[0]
