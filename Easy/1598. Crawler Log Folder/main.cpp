class Solution {
public:
    int minOperations(vector<string>& logs) {
        int res = 0;
        for (string operation : logs) {
            if (operation == "../") {
                res = (res > 0) ? res - 1 : 0;
            }
            else if (operation == "./") {NULL;}
            else {
                res++;
            }
        }
        return res;
    }
};
