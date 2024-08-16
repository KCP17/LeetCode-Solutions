class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for b in bills:
            change[b] += 1
            match b:
                case 10:
                    if change[5] > 0:
                        change[5] -= 1
                    else:
                        return False
                case 20:
                    if change[5] > 0 and change[10] > 0:
                        change[10] -= 1
                        change[5] -= 1
                    elif change[5] > 2:
                        change[5] -= 3
                    else:
                        return False
        return True
