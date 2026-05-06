class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if token == '+':
                    op = operand1 + operand2
                elif token == '-':
                    op = operand1 - operand2
                elif token == '*':
                    op = operand1 * operand2
                elif token == '/':
                    op = operand1 / operand2
                stack.append(op)
            else:
                stack.append(token)  
        return int(stack.pop())              
