class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:].zfill(32)
        reversed_string = x[::-1]
        return int(reversed_string, 2)