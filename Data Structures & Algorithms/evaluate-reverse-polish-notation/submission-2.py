class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            
            if ch in {"+", "-", "*", "/"}:
                right = stack.pop()
                left = stack.pop()

                if ch == "+":
                    stack.append(left + right)
                elif ch == "-":
                    stack.append(left - right)
                elif ch == "*":
                    stack.append(left * right)
                elif ch == "/":
                    
                    stack.append(int(left / right))
            else:
                
                stack.append(int(ch))
            
        return stack[0]