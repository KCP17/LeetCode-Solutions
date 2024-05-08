class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pairs = []
        ans = [None] * len(score)
        
        # For each pair: pair[0] is the athlete, pair[1] is the corresponding score
        for i, s in enumerate(score):
            pairs.append((i, s))
        
        # Sort the pairs in decreasing scores order (p[1])
        pairs.sort(key=lambda pair : pair[1], reverse=True)
        
        # Assign the award for each athlete
        for rank, pair in enumerate(pairs):
            match rank:
                case 0:
                    ans[pair[0]] = "Gold Medal"
                case 1:
                    ans[pair[0]] = "Silver Medal"
                case 2:
                    ans[pair[0]] = "Bronze Medal"
                case _: # Other rankings
                    ans[pair[0]] = str(rank + 1)

        return ans
