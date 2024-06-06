class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        num_of_grps = len(hand) // groupSize
        hand.sort()
        grps = [[] for _ in range(num_of_grps)]
        
        for n in hand:
            i = 0 # group index
            while grps[i] and (n - grps[i][-1] != 1 or len(grps[i]) == groupSize):
                i += 1
                if i == len(grps):
                    return False
            
            grps[i].append(n)
        
        return True
