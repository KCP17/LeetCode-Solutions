class Solution {
public:
    int pivotInteger(int n) {
        float x = sqrt((n * (n + 1)) / 2);
        return ((int)x == x ? (int)x : -1);
    }
};
