class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)[2:]
        string = str(x)
        cnt = 0
        for i in range(len(x)):
            if string[i] ==  '1':
                cnt += 1
        return cnt