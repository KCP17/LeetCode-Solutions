class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1 and digits[0] == 9: return [1,0]
        
        if digits[len(digits)-1] == 9:
            digits[len(digits)-1] = 0
            digits[len(digits)-2] += 1
        else:
            digits[len(digits)-1] += 1

        for i in reversed(range(1, len(digits)-1)):
            if digits[i] > 9:
                digits[i] = 0
                digits[i-1] += 1

        if digits[0] > 9:
            digits[0] = 0
            digits.insert(0, 1)

        return digits
