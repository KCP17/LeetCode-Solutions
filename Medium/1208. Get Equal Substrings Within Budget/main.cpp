class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int N = s.size();
        int res = 0;
        int cur_cost = 0;
        int l = 0;
        for (int r=0; r < N; r++) {
            cur_cost += abs(int(s[r]) - int(t[r]));
            while (cur_cost > maxCost) {
                cur_cost -= abs(int(s[l]) - int(t[l]));
                l++;
            }
            res = max(res, r - l + 1);
        }
        return res;
    }
};
