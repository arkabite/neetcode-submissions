class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for cur in s:
            # If it's a closing bracket
            if cur in brackets:
                # Pop the top element if stack isn't empty, else use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the popped element, it's invalid
                if brackets[cur] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(cur)
                
        # If the stack is empty, all brackets were properly closed
        return not stack