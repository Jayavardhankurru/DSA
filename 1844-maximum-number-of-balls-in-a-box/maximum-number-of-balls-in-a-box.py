class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        mpp = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            digitSum = 0
            while i > 0:
                digit = i % 10
                digitSum += digit
                i = i // 10
            mpp[digitSum] += 1
        maxi = 0
        for num, freq in mpp.items():
            maxi = max(maxi, freq)
        return maxi