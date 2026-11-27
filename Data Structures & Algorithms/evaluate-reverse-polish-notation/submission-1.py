class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                else:
                    stack.append(int(operand1 / operand2))
            else:
                stack.append(token)
        if len(stack) == 1:
            return int(stack[0])
        else:
            return None