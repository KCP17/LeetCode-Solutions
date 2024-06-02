class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = s.size() - 1, tmp = 0;
        while (l < r) {
            tmp = s[l];
            s[l] = s[r];
            s[r] = tmp;
            l++;
            r--;
        }
    }
};
