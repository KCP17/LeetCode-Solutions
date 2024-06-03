class Solution {
public:
    int appendCharacters(string s, string t) {
        int s_idx = 0, t_idx = 0;
        int s_len = s.size(), t_len = t.size();
        while (t_idx < t_len && s_idx < s_len) {
            if (s[s_idx] == t[t_idx]) {
                t_idx++;
            }
            s_idx++;
        }
        return t_len - t_idx;
    }
};
