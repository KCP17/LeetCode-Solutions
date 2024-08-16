class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        unordered_map<int, int>change;
        for (int b : bills) {
            change[b]++;
            switch (b) {
                case 10:
                    if (change[5] > 0) {
                        change[5]--;
                    }
                    else {
                        return false;
                    }
                    break;
                case 20:
                    if ((change[5] > 0) && (change[10] > 0)) {
                        change[10]--;
                        change[5]--;
                    }
                    else if (change[5] > 2) {
                        change[5] -= 3;
                    }
                    else {
                        return false;
                    }
                    break;
            }
        }
        return true;
    }
};
