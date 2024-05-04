class Solution {
public:
    int maxDepth(string s) { // Stack
        int res = 0;
        stack<char>stack; // Consists of opening brackets
        for (char c : s) {
            if (c == '(') {
                stack.push(c); // Push the opening bracket
            }
            else if (c == ')') { // If we see a closing bracket
                res = max(res, static_cast<int>(stack.size())); // # That means the number of remaining opening brackets available on stack is also the depth. We get the max depth.
                stack.pop(); // # Remember to pop "(" to mark finished counting a depth. E.g with "()()" if we don't pop it'll count the depth as 2.
            }
        }
        return res;
    }
};
