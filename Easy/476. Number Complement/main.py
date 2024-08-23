class Solution:
    def findComplement(self, num: int) -> int:
        # Suppose the number of bits in binary representation of `num` is `n`
        # So `n = len(bin(num)) - 2` (subtract by 2 to omit "0b")
        # We perform 2**n to get the value of the bit at index `n`
        # Then subtract by 1 to get the total values where all `n` bits are `1`
        # Finally, we subtract that by `num` to get its complement
        return (2**(len(bin(num)) - 2) - 1) - num
