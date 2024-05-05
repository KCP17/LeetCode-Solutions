class Solution {
public:
    bool halvesAreAlike(string s) {
        int half = s.length() / 2;
        int count = 0;
        unordered_set<char>vowels = {'u', 'e', 'o', 'a', 'i'};
        for (int i=0; i < half; i++) {
            count += vowels.count(tolower(s[i]));
            count -= vowels.count(tolower(s[i + half]));
        }
        return count == 0;
    }
};
