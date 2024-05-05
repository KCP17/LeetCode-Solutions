class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': operator.add,
                     '-': operator.sub,
                     '*': operator.mul,
                     '/': operator.floordiv}
        
        for sym in tokens:
            if sym not in operators:
                stack.append(int(sym))
            else:
                right_oprd = stack.pop()
                left_oprd = stack.pop()
                res = operators[sym](left_oprd, right_oprd)
                res += 1 if sym == '/' and left_oprd % right_oprd != 0 and res < 0 else 0 # truncates towards 0
                
                stack.append(res)

        return stack[-1]
