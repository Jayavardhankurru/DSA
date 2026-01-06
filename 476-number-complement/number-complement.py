class Solution:
    def findComplement(self, num: int) -> int:
        bit_count = num.bit_length()
        mask = (1 << bit_count) - 1
        return num ^ mask