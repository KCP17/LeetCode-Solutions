class Solution:
    def maxDepth(self, s: str) -> int: # Stack
        res = 0
        stack = [] # Consists of opening brackets
        for c in s:
            if c == "(":
                stack.append(c) # Push the opening bracket
            elif c == ")": # If we see a closing bracket
                res = max(res, len(stack)) # That means the number of remaining opening brackets available on stack is also the depth. We get the max depth.
                stack.pop() # Remember to pop "(" to mark finished counting a depth. E.g with "()()" if we don't pop it'll count the depth as 2.
        return res
