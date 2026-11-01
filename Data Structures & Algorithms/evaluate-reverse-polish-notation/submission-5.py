class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def apply(a, b, op):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return int(a / b)

        stack = []
        for tok in tokens:
            if tok in ('+', '-', '*', '/'):
                b = stack.pop()          # popped first = right operand
                a = stack.pop()          # popped second = left operand
                stack.append(apply(a, b, tok))
            else:
                stack.append(int(tok))

        return stack[0]