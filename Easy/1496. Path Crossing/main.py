class Solution:
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        hashMap = set()
        x = y = 0
        hashMap.add((0,0))
        
        for direction in path:
            
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1

            coordinate = (x,y)

            if coordinate in hashMap:
                return True
            
            hashMap.add(coordinate)

        return False
